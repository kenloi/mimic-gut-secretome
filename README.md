# MIMIC

**A mobile microbial peptide that engages a human cytokine receptor.**

*A structure-first screen of the gut secretome against human immune receptors.*

**Kenneth Loi, Zhaojun Wang** · Built with Claude Science

**▶ [Live site](https://kenloi.github.io/mimic-gut-secretome/)** — hub linking the full mini-paper, the interactive deck, and the co-fold database browser.

---

## What this is

The human gut microbiome encodes far more protein than the human genome. Most of its
secreted miniproteins (<100 aa) are uncharacterized. Some may mimic host ligands and
engage human receptors directly — protein signaling, alongside the well-mapped metabolite
signaling (short-chain fatty acids, bile acids). We built a structure-first screen to look
for them: co-fold gut-secreted miniprotein families against a frozen panel of human immune
receptors plus decoys, and score each interface against a null. The unit of observation is
a peptide–human-protein pair. The output is a ranked list of structurally supported
candidate interactions — hypothesis prioritization, not causation.

## The headline finding

**MIMIC-078** (family representative `078_038_456`, mature 45 aa) folds a confident
interface on **IL-7Rα** — iPTM 0.911, interface PAE 7.4 Å, z 6.0 against decoys — and lands
on the exact surface where interleukin-7 binds, with no sequence homology to IL-7 (a
structural mimic, not a captured gene). The interaction is specific: MIMIC selects IL-7Rα
(0.91) over all five γc-family paralogs (≤0.28) on ESMFold2, and an independent AlphaFold3
cross-check agrees (IL-7Rα ranked #1, 2.7 Å interface PAE). The peptide is horizontally
mobile — 557 homologs across 239 species and 80 genera, riding a Tn916/Tcp-type conjugative
element (mobile-element enrichment p = 0.003, #2 of 592 families) into 15 independent
*Clostridioides difficile* strains.

The hypothesis is an **immune-shielding IL-7 antagonist**: by occupying the IL-7 site, MIMIC
could blunt IL-7-driven T-cell survival in the gut where it is secreted. Direction is
unresolved — co-folding gives geometry, not function — and is testable by a pSTAT5
competition assay. The full argument, figures, and evidence ledger are in the mini-paper.

## Links — the real resources

| Resource | Where |
|---|---|
| **Full mini-paper** (the science, all figures, evidence ledger) | [paper.html](https://kenloi.github.io/mimic-gut-secretome/paper.html) |
| **Interactive deck** (live, manipulable 3D structure of MIMIC on IL-7Rα) | [deck.html](https://kenloi.github.io/mimic-gut-secretome/deck.html) |
| **Co-fold database browser** (all 7,408 interfaces) | [cofold_browser.html](https://kenloi.github.io/mimic-gut-secretome/cofold_browser.html) |
| **3-min demo video** (2:50, with narration) | [`media/mimic_demo_video.mp4`](media/mimic_demo_video.mp4) |
| Ranked candidate families (297) | [`results/reranked_candidates_full.tsv`](results/reranked_candidates_full.tsv) |
| Complete mature-form scores (7,408 folds) | [`results/mature_scores_complete.tsv`](results/mature_scores_complete.tsv) |
| Key figures | [`figures/`](figures/) |
| Methods | in the mini-paper ([paper.html](https://kenloi.github.io/mimic-gut-secretome/paper.html)) |

## Method in one paragraph

From the Global Microbial smORF Catalog (GMSC), filter to gut habitat + predicted secreted
+ high-quality, collapse to family representatives. Co-fold each family against a frozen
panel of 15 human immune receptors plus 10 decoy receptors (25 targets) with ESMFold2-Fast,
recording iPTM and interface PAE per pair. Convert each interface confidence to a
decoy-calibrated z-score. A provenance audit re-derived every mature peptide (post-signal-
peptide cleavage) and refolded 7,408 of a possible 7,425 interfaces (297 families × 25 targets, one family folded partially) in one session,
which reranked the whole screen and moved the lead onto MIMIC-078 × IL-7Rα. Full detail,
including the audit, in the mini-paper.

## Repository layout

```
results/   score tables (reranked candidates, complete mature scores, MGE null test, γc specificity, energetics)
figures/   structural overlay, ICE synteny, family MSA, specificity panel
data/      target panel, homolog sequences, predicted complex (CIF), superposed model (PDB)
src/       analysis scripts
paper.html         full mini-paper (also served on the Pages site)
deck.html          interactive slide deck
cofold_browser.html  7,408-cofold interactive database
```

## License & citation

MIT License (Kenneth Loi, Zhaojun Wang). Open-source throughout; no proprietary data or
assets.

Structure prediction: ESMFold2-Fast (Chan Zuckerberg Biohub). Peptide catalog: GMSC.
Executed with Claude Science.
