# Go / no-go: does MIMIC engage IL7R, and does it block IL-7?

**Central hypothesis (sharpened).** MIMIC is an **anti-inflammatory / immune-shielding**
peptide. It occupies the IL-7 binding site on IL7R (ligand-competitive geometry, 65%
overlap) to **dampen IL-7-driven lymphocyte signaling** — reducing the host's ability to
mount and maintain a T/B/ILC response against the microbe that displays it. This predicts
an **IL-7 antagonist**. The conservation of the same cassette across benign commensals
*and* a pathogen follows directly: the selective advantage is **immune invisibility**, a
trait useful to any gut resident, and the mobile element spreads it — including into
pathogens, where the same shield aids persistence.

This is a hypothesis. The assays below are built to confirm or kill it, in order.

---

## The readout
IL-7 → IL7R/γc → JAK1/JAK3 → **STAT5 phosphorylation (pSTAT5)** in an IL-7-responsive
lymphoid line (e.g. primary human CD4⁺ T cells, or an IL7R⁺/γc⁺ reporter line). pSTAT5 is
the proximal, quantitative, well-validated IL-7 readout (flow cytometry or a STAT5-luc
reporter).

## Assay 1 — Binding (go/no-go on the interaction itself)
**Question:** does MIMIC bind IL7R at all?
**Method:** biolayer interferometry or SPR — immobilized IL7R ectodomain, titrated
synthetic MIMIC (mature 45-aa peptide). Read K_D.
- **Positive control:** native IL-7 (must bind, low-nM K_D).
- **Negative control:** a scrambled-sequence MIMIC (same composition, shuffled) and an
  unrelated similar-size peptide — neither should bind.
- **GO if** MIMIC binds IL7R specifically and dose-dependently; **NO-GO if** no binding
  above scrambled control → the structural prediction is a false positive, stop here.

## Assay 2 — Direction (antagonist vs agonist), the decisive experiment
**Question:** does MIMIC *block* IL-7 (antagonist, our hypothesis) or *mimic* it (agonist)?
Run two arms on the same pSTAT5 readout.

**Arm A — agonism.** MIMIC alone, dose-titrated, no IL-7.
- **Positive control:** IL-7 alone (full pSTAT5).
- **Negative control:** vehicle / scrambled peptide (no pSTAT5).
- *Agonist* → MIMIC alone drives pSTAT5. *Antagonist* → MIMIC alone does nothing here.

**Arm B — antagonism (the hypothesis test).** Fixed EC₈₀ IL-7 + a MIMIC dose–response
(competition).
- **Positive control for blockade:** a neutralizing anti-IL7R antibody (should suppress
  pSTAT5) and/or unlabeled IL-7 self-competition.
- **Negative control:** scrambled MIMIC at top dose (IL-7 signal intact).
- **GO (hypothesis supported) if** MIMIC dose-dependently **suppresses** IL-7-induced
  pSTAT5 with no agonism in Arm A → **anti-inflammatory / immune-shielding antagonist.**
- **Agonist branch if** Arm A is positive → still a microbial cytokine-receptor ligand,
  but the "shield" framing is wrong; reframe as an IL-7 *mimic*.
- **NO-GO if** neither arm moves → binds but functionally silent at this site.

## Assay 3 — Specificity & mechanism (confirmatory)
- **Receptor specificity:** repeat pSTAT5 on a receptor MIMIC should *not* touch
  (e.g. IL-2/IL-15 via a shared-γc but distinct-α line) — blockade should be IL7R-specific.
- **Epitope test:** IL7R point mutants at the predicted MIMIC contact residues (the
  SCID-cluster positions) should **abolish** MIMIC binding but retain IL-7 binding if the
  footprints only partially overlap — ties function back to the predicted structure.
- **Cellular consequence:** IL-7-dependent T-cell survival/proliferation ± MIMIC (does the
  shield actually reduce the lymphocyte response?).

## Controls summary
| Role | Reagent | Expected |
|---|---|---|
| Positive (signal) | native IL-7 | full pSTAT5 / binding |
| Positive (blockade) | anti-IL7R mAb; unlabeled IL-7 | suppresses pSTAT5 |
| Negative (sequence) | scrambled-MIMIC (same aa composition) | no binding, no effect |
| Negative (vehicle) | buffer | baseline |
| Specificity | IL-2/IL-15 line; off-target receptor | MIMIC has no effect |
| Structure link | IL7R contact-residue mutants | binding abolished |

**Bottom line.** Assay 1 tells us if the prediction is real. Assay 2, Arm B is the
go/no-go on the anti-inflammatory hypothesis. Both are a week of bench work with
off-the-shelf reagents.
