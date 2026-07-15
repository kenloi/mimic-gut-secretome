# REVIEW.md — Pre-Ship Checklist (MIMIC)

Run this before shipping any deliverable: a results table, a figure, a deck, the
paper, or a repo push. Each item is a verifiable assertion. Check it only when it
is true. Grouped by deliverable type. Every item is grounded in a mistake this
project already made or a rule it already adopted.

The unit of observation is a peptide–human-protein pair. A result is a scored pair,
never a peptide in isolation. Claims are candidate interactions, never causation.

---

## SCIENCE / STATS

- [ ] Every enrichment or depletion claim states its null construction in the text: the background source AND the shuffle method (block vs residue-order, dinucleotide vs Markov). A number without a named null does not ship.
- [ ] Every enrichment or depletion claim reports an empirical p, computed as `fraction(background >= observed)`, plus percentile and rank — not a bare point estimate.
- [ ] The matched background is drawn the same way as the candidate feature, and thin backgrounds are filtered (e.g. `n_prod >= 5`). A saturated or biased background is flagged, because it flips the interpretation.
- [ ] The decoy-calibrated interface gate scores a receptor-specific robust z-score of interface confidence, not raw ipTM (ipTM is length/size-biased against short peptides).
- [ ] The null is pooled per target across all query decoys into ONE distribution (`n = K × #peptides`), scaled with median/MAD — never a single peptide's own K=5 shuffles (sd from ~5 points is too noisy).
- [ ] The pooled null's N is logged alongside the cutoff.
- [ ] The FDR-null (query-side sequence shuffles) and the selectivity-null (target-side receptor decoys) are kept as SEPARATE columns. They are combined only at ranking. The same axis is never double-normalized.
- [ ] Empirical FDR is reported from the query-shuffle null with BH applied once against one global null.
- [ ] The wide screen is K=1 (a real binder shows single-shot) and the decoy-calibrated confirm is K=5. K1-for-triage / K5-for-FDR is not inverted.
- [ ] All discriminative CPU filters are applied upstream of any GPU fold (the disease pre-filter and prune step run BEFORE structure prediction, never after). Fold count and GPU-hours are reported per stage.
- [ ] A cognate/bacterial partner is ruled out only if it fails BOTH tests: it does not co-travel (conserved + adjacent) across the peptide's homolog loci AND it loses the cofold-preference test (host iPTM > cognate iPTM). One test alone is insufficient.
- [ ] The synteny-vs-function caveat is stated wherever a consistency score is used: homologs drawn from close isolates inflate consistency because the score partly measures genomic relatedness.
- [ ] Every biological claim cites a primary source. Speculation is flagged explicitly. Unknown values are stated as unknown, never fabricated.

---

## REPRODUCIBILITY

- [ ] Every `results/` table and every `figures/` figure maps to a named, committed script in `src/`. Run a `src/` ↔ `results/` coverage audit before each push — this project once shipped a repo whose `src/` held exactly one script while folding, z-scoring, occlusion, Kabsch, and mimicry code lived only in workspace cells.
- [ ] Every table linked in the README or the paper is ACTUALLY PRESENT in the pushed repo. This miss recurred: `reranked_candidates_full.tsv` was README-linked but absent from the published snapshot. The GitHub snapshot is manual and point-in-time; new artifacts do not auto-sync.
- [ ] Every results table regenerates from a single named script plus its inputs. No table depends on ad-hoc cross-session cells.
- [ ] Dataset version and access date are logged per source (GMSC, AMPSphere, disease cohort, UniProt, PDB). No source was substituted silently; if one was unreachable, that is reported, not papered over.
- [ ] Random seeds are fixed. Model-weights version and all tool versions are recorded.
- [ ] Every figure carries the exact code + environment that produced it (lineage intact: `fig.savefig`, not `plt.savefig`).

---

## FIGURES

- [ ] Organism / species labels on every published figure are verified against the GenBank / source record. A species was mislabeled once (B. breve shown as Vescimonas; a Firmicutes→2-phyla retitle) and required a corrective commit.
- [ ] One canonical color scheme is used across the published figure set. Two schemes are not allowed to coexist (loci vs lovis drift). Convention: hero = magenta, color only functional categories, grey + unlabeled everything else.
- [ ] Every schematic receptor glyph is concave-up (a cup, ∪) with the binding groove opening toward the peptide/ligand. A dome bulging toward the ligand is wrong. Check every glyph and report a per-glyph count + verdict.
- [ ] Dotted connector lines converge INTO the concave groove, not past it (human ligand teal, microbial mimic orange). The ligand is seated in the cup.

---

## HTML / PUBLISH

- [ ] `grep -c '{{artifact' *.html` returns 0 for every `<img src>`. Markers resolve only inside Claude Science and break on static hosting. Note the trap: `save_artifacts` runs a basename auto-linker that silently reverts a correct relative `figures/x.png` back to a marker when the basename matches a project artifact — defeat it with non-colliding filenames or by `&#46;`-encoding the extension dot (`figures/peptide_funnel&#46;png`).
- [ ] Every inline SVG intended to scale carries `viewBox` + `width=100%` + explicit `preserveAspectRatio="xMidYMid meet"` (with `height:auto`). Embedded raster `<image>` elements carry the same, or they distort on resize.
- [ ] Large single-file HTML (inlined 3Dmol/webpack) was edited surgically by anchored regex injection, made idempotent by stripping any prior injected block first. It was never full-parsed. Re-runs converge instead of stacking duplicates.
- [ ] After a Pages push, publication is verified by grepping a known content signature (title / iPTM value / 3dmol marker) at the LIVE URL — NOT by HTTP 200. Pages serves `max-age=600`, so a stale or deleted file still returns 200 for ~10 minutes. Pages whose content-at-URL changes carry a `Cache-Control:no-cache` meta.
- [ ] The push used SSL-verify-off with a tokenized HTTPS URL, and the token was scrubbed from the remote URL afterward. No token is left embedded in `.git/config` or any committed file.

---

## COMPUTE

- [ ] Before dispatching a GPU sweep, GPU-hours were estimated and queue wait was compared against a metered burst (Modal/RunPod/Vast). Free academic GPU queues are not assumed to deliver on a deadline — the bt H200 node sat PENDING behind unlimited jobs and a full sweep was TERMed partial by a timeout ceiling.
- [ ] Partition idleness was probed and CPU-only work (DIAMOND, NCBI fetch, neighborhood) was routed to whichever partition actually has idle cores (often the GPU partition, no `--gres`).
- [ ] The submit script contains NO host-managed sbatch directives (`--array`, `--output`, `--error`, `--chdir`, `--wrap`) — `submit_job` rejects them. Arrays run as N separate single-GPU shard jobs.
- [ ] The output directory is created inside the command (`mkdir -p out && ...`); `./out/` is not pre-created by the provider.
- [ ] Large inputs are staged via `inputs=[{src}]` or base64-through-`call_command` (SFTP upload is path-jailed for `/groups` and `/global/scratch`). `download()` is treated as a dict and the nested file is copied out before `save_artifacts`.
- [ ] `scratch_root` is registered for the target host before the first submit (a missing one is a hard blocker fixable only in Customize → Compute).
- [ ] GPU-hours are logged.
