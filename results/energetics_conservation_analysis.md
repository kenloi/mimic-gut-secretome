# ΔΔG energetics + γc panel score & interface-conservation analysis

## 1. ΔΔG / interface energetics (PRODIGY) — what it revealed

**First, an honest correction:** the ΔΔG calculation had been *scoped* in the evidence-ladder
planning but was never actually run in prior sessions. It has now been run here (PRODIGY
contact-based ΔG, single-process, on the ESMFold2 + your AF3 complexes and the native
IL-7·IL7R reference from 3DI2).

### The lead vs the native ligand
| Complex | PRODIGY ΔG (kcal/mol) | contacts |
|---|---|---|
| **MIMIC × IL7R** (ESMFold2) | **-9.00** | 62 |
| MIMIC × IL7R (AF3) | -7.47 | 35 |
| MIMIC × IL7R (superposed) | -8.96 | 62 |
| **Native IL-7 × IL7R** (3DI2 reference) | **-9.15** | 58 |

**ΔΔG(MIMIC − native IL-7) = +0.15 kcal/mol.** MIMIC's predicted interface is
energetically indistinguishable from native IL-7's on the same receptor — the peptide makes
a comparable number of contacts (62 vs 58) with essentially the same predicted ΔG. This is
consistent with a *bona fide* ligand-competitive interface, not a weak/incidental one. (AF3
gives a slightly weaker −7.5; the ~1.5 kcal/mol engine spread is within PRODIGY's own error.)

### The critical caveat — ΔG does NOT reproduce the specificity
Across the six γc receptors, **PRODIGY ΔG is flat and does not rank IL-7Rα first** — it even
favours IL-4Rα (−11.4 ESMFold2 / −10.9 AF3). iPTM-vs-ΔG Spearman is ~0 on both engines.

**Why:** PRODIGY counts interface contacts on whatever pose it is given; it has *no model of
whether the pose is correct*. Feed it a low-confidence, high-PAE decoy pose (IL-4Rα iPTM 0.21,
PAE 23 Å) and it still counts contacts and reports a favourable ΔG. So contact-energetics is
**not a specificity discriminator** for predicted complexes — iPTM/PAE (which encode pose
confidence) are. The honest reading: **ΔG tells us the IL7R interface, once assumed, is as
substantial as native IL-7's; it does NOT independently confirm IL7R is the target.** That job
belongs to iPTM (0.91 vs ≤0.28) and, ultimately, SPR.

## 2. γc panel scores — two engines agree on the target

| Receptor | ESMFold2 iPTM | ESMFold2 PAE | AF3 iPTM | AF3 iface-PAE |
|---|---|---|---|---|
| **IL-7Rα** | **0.91** | 7.5 | **0.68** | **2.7** |
| TSLPR/CRLF2 | 0.28 | 22.0 | 0.29 | 12.9 |
| IL-4Rα | 0.22 | 23.5 | 0.24 | 13.2 |
| IL-21R | 0.21 | 23.0 | 0.24 | 11.8 |
| IL-2Rα | 0.10 | 28.9 | 0.19 | 13.6 |
| IL-15Rα | 0.07 | 30.8 | 0.42 | 10.6 |

**Both engines rank IL-7Rα #1 with a wide margin**, and — the stronger cross-engine signal —
AF3 gives the IL7R interface a **2.7 Å min-PAE**, extremely confident, versus >10 Å for every
paralog. One honest discrepancy: AF3 lifts IL-15Rα to 0.42 (ESMFold2 gave 0.07); no other
paralog exceeds 0.29 on either engine, and IL-15Rα's PAE (10.6 Å) is still far worse than
IL7R's. The engines disagree on the *ordering of the losers*, never on the winner.

## 3. Native-interface conservation — the interface IS the conserved surface

Which MIMIC residues touch IL-7Rα, and are those the conserved ones across the family?
- **20 of 45 mature residues contact IL7R** (<5 Å).
- **Contact-residue conservation = 96% (18/20 fully invariant across the 7-member family incl.
  3 C. difficile strains + cross-phylum B. breve); non-contact = 93%.** The two variable
  contacts (pos 43 T/K, 44 V/A/K) are at the flexible C-terminus.

**This is the opposite of the old hero (281).** For 281 the interface was *less* conserved
than the fold core (moonlighting: conserved job = operon role, receptor use = opportunistic).
For MIMIC-078 the IL7R-binding surface is the most conserved part of the peptide — consistent
with receptor engagement being *the* conserved function, not a side activity.

**Caveat:** the family is near-identical (7 sequences, 93–97% id), so per-residue conservation
has low dynamic range and the contact-vs-noncontact difference is not statistically separable
(Mann-Whitney p = 0.18). The qualitative statement — the interface is fully conserved, not a
variable patch — holds; the enrichment test is underpowered at this family depth. A deeper MSA
(the 557-homolog set) would give the dN/dS resolution to test selection on the interface.

## Bottom line
- ΔΔG: MIMIC's IL7R interface ≈ native IL-7's (ΔΔG +0.15 kcal/mol) — substantial, not weak.
- ΔG is NOT a specificity filter for predicted poses; iPTM/PAE are, and both engines put IL7R
  first by a wide margin.
- The IL7R-binding surface is the conserved core of the peptide family — receptor engagement
  looks like the conserved function.
- None of this measures binding. SPR against IL7R + the γc paralogs remains the decisive test.
