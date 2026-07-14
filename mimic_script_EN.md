# MIMIC — 3-Minute Presentation Script (English)
### For the current 8-slide `deck.html` (8 numbered + 1 backup) · Research Track, Built with Claude: Life Sciences
### Kenneth Loi, Zhaojun Wang

**Delivery:** ~150 wpm. `/` = breath. `(click)` = advance one on-slide animation. Follows Kenneth's own spoken take — let the slides carry the visuals. Backup slide is Q&A, not spoken.
**Timing:** 8 spoken slides ≈ 2:27 of narration (369 words @150 wpm); the S4 structure clicks, the S7 assay reveal, and natural pauses fill the 3:00 slot. Slow down rather than pad. Protect S3–S7.
**Before recording:** S3 shows **7,408 of 7,425**. If you say the number, say "seven thousand four hundred eight" — the "of 7,425" is on the slide.

---

**[S1 · Title — "Listen to your gut"]**
Hello, everyone — I'm **Kenneth Loi**, and with **Zhaojun Wang**, / this is our discovery of a mobile microbial peptide that binds a human immune receptor. *(0:12)*

**[S2 · 100× more microbial genes — what do they do?]**
Your gut carries a hundred times more microbial genes than human genes — / and it's an open question what they all do. / We know microbes secrete metabolites that engage our receptors, / but there are many predicted secreted *proteins* whose function we have no idea about. / *(click)* So we set out to use computational biology to infer what these small ORFs might be doing. *(0:24)*

**[S3 · A billion smORFs, filtered to one candidate — PROTECT]**
After filtering about a billion sequences, / performing structure prediction, and ranking the candidates, / we found a microbial peptide that engages **interleukin-7 receptor**. / One honest note along the way: our first hit scored the *precursor*; a human caught it, and with Claude Science we re-derived every *mature* peptide, refolded the shortlist in one session, and reranked — which surfaced this lead. *(0:26)*

**[S4 · A gut peptide lands on the IL-7 site — name MIMIC — PROTECT · staged structure]**
The IL-7 receptor is important for T-cell development — it's what keeps our T cells alive; lose it, and you lose your T cells. / And here's what's interesting: when we predicted the interface, / *(click)* the residues where immune-deficiency mutations cluster / *(click)* the native IL-7 ligand / *(click)* and our peptide — bound to the *same position* IL-7 does. / We named this gut peptide **MIMIC**. / Honestly: this is *co-location* with the functional interface, not enrichment. *(0:30)*

**[S5 · It picks IL-7Rα out of its own family — PROTECT]**
Then we asked how IL-7's related family members compare. / Against its five closest relatives, / MIMIC preferentially binds IL-7Rα — the real target lights up, the look-alikes stay dark. / AlphaFold3 agrees independently. *(0:17)*

**[S6 · It rides a mobile element into a pathogen — PROTECT]**
Intrigued, we did some comparative microbiome genomics. / MIMIC tends to be encoded by a **conjugative transposon** — a mobile element that may be moving it between microbes — / across two hundred thirty-nine gut species, including fifteen strains of *Clostridioides difficile*, a colitis pathogen. *(0:22)*

**[S7 · A shield you can trade — MIMIC hypothesis + testable — PROTECT]**
Our leading hypothesis, one of two: / IL-7 keeps lymphocytes alive, and this microbe carries a peptide that engages the same receptor — / so commensals may be *trading* this gene across the community, / with the peptide supporting and protecting these microbes from immune recognition. / *(click)* And it's testable in a week: add MIMIC with IL-7, read STAT5 — / suppressed, it's a shielding *antagonist*; firing alone, an *agonist*. / A hypothesis, not yet function. *(0:30)*

**[S8 · Close — single takeaway]**
This suggests the gut may encode a whole *library* of human-receptor ligands — / waiting to be discovered. / Thank you. *(0:11)*

*(Backup — "Six independent lines of evidence" — leave up for Q&A; do not narrate. "Every panel is computational; none measures binding.")*

---
**Timing (verified against this file):** 8 spoken slides = **369 words ≈ 2:27** of narration at 150 wpm — the S4 structure clicks, the S7 assay reveal, and natural pauses land you near 3:00. Slow down rather than pad; drop the S3 Claude-correction clause if you need ~15 s back.

**Number consistency:** S3 shows **7,408 of 7,425** — 7,408 mature interfaces refolded, one family folded partially. Say "seven thousand four hundred eight." Voice, slide, paper, and browser agree.

**Pronunciation:** *Clostridioides difficile* — "klos-TRID-ee-OY-deez dif-uh-SEEL." On S7, give the MIMIC letters a half-beat so **I**mmuno + **M**odulatory reads as one word.

**Animation cues:** S2 = 1 click (open question / "so we set out…"). S4 = 3 clicks (SCID residues → native IL-7 → MIMIC). S7 = 1 click (pSTAT5 test strip). All other slides static. The Claude turning-point is spoken on S3, not shown — the full trail lives in the paper.
