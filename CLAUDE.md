# CLAUDE.md — MIMIC operating manual

How we work on this project. Durable procedures a future session follows. Rules are
procedures, not this project's result values. When a rule cites a number, the number is a
convention (e.g. K=1 vs K=5), not a finding.

Register: short declarative sentences, engineering tone. Flag speculation and data gaps.
Cite primary sources for biological claims. Never fabricate values, citations, or identifiers.

---

## A. Research strategy

### A1. Prune before you fold
Sequence the screen as cheap-filter → cheap-fold → expensive-confirm. Spend every
discriminative CPU filter upstream of any GPU spend, because a fold is ~10–100× the cost of a
filter. Run the wide screen at K=1 (a real binder shows single-shot), and reserve
multi-seed K (K=5) for the decoy-calibrated confirm on the promoted shortlist. K is the
linear cost multiplier — K1 for triage, K5 for FDR on survivors. Report the fold count and
GPU-hours at each stage. Never run naive all-to-all.

### A2. Broad screen, then enrich on lock-on (loci-expansion trigger)
Work in two modes and switch deliberately.
1. **Broad screen** for candidates sharing a general feature — a structure-based search
   against a compressed/clustered structure DB (e.g. clustered AFDB) for a domain, or a
   general functional feature such as "expressed in the gut context." Cast wide first.
2. **Enrich on lock-on**: once you lock focus onto a specific gene or family whose function
   you want to nail down, trigger sequence-based nearest-neighbor enrichment
   (MMseqs / HMMER / BLAST) to pull close homologs, then measure how conserved the gene AND
   its genomic neighbors are — operon/synteny matters for microbial comparative genomics.

Concrete trigger to go wider on loci: you have locked focus onto a specific interesting
gene, AND the in-hand loci are too few (<~5) or all from near-identical isolates (can't
separate conservation from relatedness), AND/OR the claim itself depends on breadth across
taxa. When those coincide, enrich; otherwise stay put. The reason: breadth-dependent claims
and orphan/cognate conservation tests are only meaningful across diverse taxa.

### A3. Gut-check execution rule
Decide whether to act or ask by cost and reversibility.
- **GO without asking** when a quick experiment is cheap (<~5 min / a few folds / one small
  script) AND settles a fork in what we do next. A cheap, decisive test beats a question.
- **GO freely** for read-only checks on data or structures already in hand.
- **ASK FIRST** before launching anything that consumes NEW compute — GPU, scheduler queue,
  or a large fetch. New compute is the expensive/irreversible boundary; per project rules,
  summarize the plan and wait for confirmation before large batches.

---

## B. Remote compute contract

### B1. Batch GPU folding: one job streams N complexes
For any embarrassingly-parallel structure/inference sweep on a scheduler, keep the model
resident and iterate the work list inside the process — this amortizes the model-load cost
(~15–21s here) that dominates a per-pair job. Shard the work list and submit one single-GPU
task per shard; single-GPU tasks backfill into gaps that multi-GPU reservations cannot. Size
each task to the cluster's core:GPU ratio (bt/lrc wanted exactly 14 cores/GPU; 16 backfilled
worse). Never submit one job per pair.

### B2. The six host.compute SSH/SLURM gotchas
Every one cost at least one failed submit. Check them before the first submit on a new host.
1. **No host-managed sbatch directives.** submit_job rejects `#SBATCH --array/--output/
   --error/--chdir/--wrap` — the provider manages these. Run arrays as N separate single-GPU
   jobs, not one array job.
2. **Stage large inputs by base64, not upload.** `c.upload` is SFTP path-jailed and
   unreliable for `/groups` and `/global/scratch`; stage by base64-piping through
   `call_command`, or pass `inputs=[{src}]`.
3. **download() returns a dict, and the file is nested.** `c.download` returns
   `{local_path, bytes, sha256}` with the file at a nested `hpc/scp-<hash>/` path, not the
   workspace root. Copy the nested file out before `save_artifacts`.
4. **Make your own output dir.** `./out/` is not pre-created; put `mkdir -p out && cp ...`
   inside the command or the job fails at write time.
5. **Recover lost jobs via the scratch dir.** `attach_job` fails after a daemon/kernel state
   reset; recover by `call_command('ls <scratch>')` then download by absolute path.
6. **Verify scratch_root is registered before submitting.** A host with no scratch_root is a
   hard blocker only fixable in Customize → Compute — check first (ssh:bt had none).

### B3. Size in GPU-hours; free queues are unreliable for deadlines
Don't assume shared academic GPU queues deliver on a timeline — nodes get fully allocated to
other users' unlimited/multi-day jobs and your shards sit PENDING indefinitely, and
timeout_ceiling can TERM a long sweep partial. Estimate GPU-hours first; if the job is small
(this screen was tens of GPU-h, ~$50–130), a metered burst (Modal / RunPod / Vast) is more
predictable and trivially cheap versus waiting. Burst to Modal for deadline work.

### B4. Route CPU-only jobs to idle GPU-partition cores
Probe partition idleness before routing. On bt the standard/standard-shared CPU partitions
ran chronically 0-idle while the GPU partition had 150–200 idle CPUs; route CPU-only work
(DIAMOND, NCBI fetch, neighborhood analysis) to `--partition=gpu` with no `--gres`, because
that is where the idle cores actually are.

### B5. Single-sequence folder for orphan/short sequences
MSA is the fragile, slow, GPU-idling part of AF-family cofolding at scale (remote MMseqs2
servers queue and error; a shared local MSA DB index can SIGABRT on an mmseqs build
mismatch). For orphan/short sequences prefer a single-sequence folder (ESMFold2-Fast) — it
removes the entire MSA failure surface. If you must use a shared MSA DB, verify the mmseqs
build that created the index matches the container's mmseqs. See C4 for validating the swap.

---

## C. Scoring discipline

### C1. Gate on a decoy-calibrated statistic, not raw iPTM
Raw iPTM is length/size-biased — worst for a <100aa peptide against a large receptor — so a
raw-iPTM gate rewards size, not binding. Gate instead on a receptor-specific z-score of the
pair's interface confidence against a shuffled-peptide null.

### C2. One pooled, robust null per target
Do NOT z-score a pair against that single peptide's own K=5 shuffles — an SD from ~5 points
is too noisy. Pool all peptides' shuffled decoys per receptor into one null
(n = K × #peptides) and use median/MAD, not mean/SD. This pooled-robust null was the single
biggest result-changing correction in the project.

### C3. Keep FDR-null and selectivity-null separate
Two controls, two axes, never double-normalized.
- **FDR-null** = query-side shuffled-peptide null → empirical FDR (BH once, one global null,
  log N).
- **Selectivity-null** = target-side architecture-matched receptor decoys → an orthogonal
  selectivity layer (rank on selectivity ratio; flag promiscuity if a peptide binds ≥3
  unrelated decoys).
Keep them as separate columns. Combine only at the ranking step; never normalize the same
axis twice.

### C4. Validate any folder swap by cross-method iPTM correlation
Before dropping one folder for another, run both on identical pairs and check the iPTM
correlation (ColabFold↔ESMFold2 was Pearson r=0.94, which justified the swap). A folder swap
without a cross-method correlation is unvalidated.

---

## D. Analysis conventions

### D1. Orphan vs cognate decision rule + the synteny caveat
If a peptide genuinely signals to a bacterial partner, that partner should be conserved and
adjacent across the peptide's homolog loci AND should out-cofold the host target. Rule the
cognate OUT only when the candidate partner fails BOTH tests: it does not co-travel across
loci, and the host target out-cofolds it. Absence of a co-traveling partner plus a
host>cognate cofold preference ⇒ classify "orphan," which strengthens a host-mimicry
hypothesis. This is a conservation-of-context test, distinct from single-locus annotation.

**Mandatory caveat, state it every time:** a synteny/consistency score partly measures
genomic relatedness, not function, when the homologs came from near-identical isolates. Do
not present conservation-of-context as conservation-of-function without noting that
close-isolate loci inflate the consistency score. (This is why A2's loci-expansion trigger
fires on "all from near-identical isolates.")

### D2. Empirical-enrichment-null discipline
For any "is my candidate unusual?" claim: compute the feature identically on the candidate
and on a large background set drawn the same way, then report empirical percentile and
p = fraction(background ≥ observed). Never report a point estimate without its matched null.
Filter thin backgrounds (e.g. require n_products ≥ 5). Always state the shuffle/background
construction explicitly — background source, and shuffle method (block vs residue-order,
dinucleotide vs Markov, position permutation). An unstated null construction is a correctness
gap a reviewer will flag. A saturated or biased background can flip the interpretation, so
inspect the background before trusting the p.

### D3. Reranking-table schema
Merge heterogeneous evidence into one table keyed on the pair `{peptide}__{target}` — one row
per pair, one join per evidence layer. Ranking is multi-signal, never iPTM-alone. Columns
span: structure (mature_iptm, iface_pae), decoy z-score, expression (metaP/metaT),
locus_context, and occlusion/accessibility. Derive a rule-based `interest_class` label (e.g.
"orphan + hit + expressed") from the columns. Accessibility/occlusion can VETO a high-iPTM
hit — a buried interface is not a binding interface, so a strong iPTM with an occluded epitope
does not rank.

---

## E. Build / edit conventions

### E1. Edit large single-file HTML surgically, never full-parse
deck/browser/paper HTML files are ~600KB–1.4MB single-file with inlined 3Dmol/webpack
bundles; parsing them (BeautifulSoup etc.) is unsafe and slow. Instead locate an anchor
(`<body>`, a marker comment) by regex, strip any previously injected block of the same
signature, then re-insert — so re-runs converge instead of stacking duplicates
(idempotent-by-construction). Verify by content-signature grep, not visual diff.

### E2. Make inline SVG scale-proof
Any inline SVG meant to scale with its container carries all three: `viewBox`, `width=100%`,
AND an explicit `preserveAspectRatio="xMidYMid meet"` (with `height:auto`). viewBox +
width=100% alone still distorts on resize. Apply the same to embedded raster `<image>`
elements (base64 structure snapshots) to stop raster distortion. Cheap, idempotent, prevents
a whole class of resize bugs.

### E3. Never emit {{artifact:...}} markers in HTML bound for static hosting
`{{artifact:art_...}}` markers resolve only inside Claude Science and break on any static
host (GitHub Pages). All `<img src>` in a leaving-the-platform deliverable must be relative
paths. The subtler trap: `save_artifacts` runs a basename auto-linker that silently rewrites
a relative `figures/<name>.png` back into an artifact marker whenever the basename matches a
project artifact — reverting a correct save unnoticed. Defeat it by encoding the extension dot
as an HTML entity (`figures/peptide_funnel&#46;png`): the browser decodes the correct relative
URL, while the auto-linker's `.png` matcher no longer fires. Pre-publish, assert
`grep -c '{{artifact' *.html` is 0 in img src.

### E4. Receptor-glyph convention: concave-up cup
In schematic receptor/ligand cartoons, draw the receptor as a concave-up cup (∪) with the
binding groove opening toward the peptide/ligand. A dome bulging toward the ligand is wrong.
Dotted connector lines (human ligand teal, microbial mimic orange) must converge INTO the
concave groove, not miss it. Check every glyph — count them and report a per-glyph verdict —
because a single mis-oriented glyph misrepresents the binding geometry.

---

## Cross-cutting invariants

- **Every result-bearing artifact has a committed, named script in `src/`.** A multi-session
  campaign silently accumulates results whose generating code never lands in the repo. Treat
  src↔results coverage as a periodically-audited invariant, not an aspiration.
- **The GitHub snapshot is manual and point-in-time.** New artifacts do NOT auto-sync;
  updating the published repo requires an explicit push. Every table linked in the README must
  actually be present in the repo and regenerable from a single script plus its inputs.
- **Verify organism labels against the GenBank source before publishing any loci figure.** A
  species was mislabeled once and caught only in audit; keep one canonical color scheme.
- **Contact email comes only from `host.get_user_email()`** for services that ask for one
  (NCBI ENTREZ_EMAIL, etc.). Never fabricate or hardcode one.
