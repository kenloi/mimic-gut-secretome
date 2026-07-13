# MIMIC — 3-Minute Demo Script
### Gut secretome × host-receptor screen · Kenneth Loi, Zhaojun Wang · Built with Claude: Life Sciences

**Target: ~430 spoken words / 3:00. Bracketed cues = slide + action.**

---

**[S1 · Title — the scope]**
Your gut carries a hundred times more microbial genes than human genes. It's the largest reservoir of coding potential in your body — and most of what it does to you, we've never read. (0:15)

**[S2 · Scale]**
Roughly as many microbial cells as human cells, but their genes outnumber ours a hundred to one. That's the coding potential we're walking around with. (0:12)

**[S3 · The partnership runs on signals]**
This is an ancient partnership, and it already runs on molecular signals. Microbes talk to us in chemistry — short-chain fatty acids, bile acids — and some molecules even *mimic* our own ligands. That's established. (0:18)

**[S4 · The gap — proteins]**
But we've mapped the metabolites. The secreted *proteins* are the gap. Commensals secrete thousands of small proteins, and almost none have a known human target. So we asked: do microbes also signal in protein — miniproteins that engage our own receptors directly? (0:22)

**[S5 · How we did it + Claude]**
We screened by structure. ~2,000 gut-secreted miniprotein families, co-folded against human immune receptors plus sequence-matched decoys — every hit has to beat a null. And here's the moment: our first hit scored the *precursor*, not the secreted form. A human caught the smell of it — and Claude Science re-derived every mature peptide, refolded **7,408 structures in one session**, and reranked the whole screen. (0:35)

**[S6 · The lead — live, staged structure]**
This is the corrected lead, on **IL7R** — the interleukin-7 receptor. *(Click once)* here's the receptor and the SCID immune-deficiency residues. *(Click again)* native IL-7, bound in its groove. *(Click again)* and our peptide — landing on the exact same surface, 65% overlap. *(drag to rotate)* (0:35)

**[S7 · The twist — mobile & pathogenic]**
Then the neighborhood told a story. This peptide isn't fixed to one genome — it **rides a conjugative element**, traded across gut bacteria in two different phyla. Enrichment p = 0.003. And the carriers include *Clostridioides difficile* — a major gut pathogen. The same mobile cassette bridges harmless commensals and a colitis pathogen. (0:28)

**[S8 · The system — MIMIC]**
So we name it: **MIMIC** — a Mobile, ImmunoModulatory, ICE-borne Commensal peptide. It engages IL-7's receptor with *no* sequence homology to IL-7 — a structural mimic on a mobile element. (0:15)

**[S9 · The implications — the shield]**
Here's what we think it's *for*. IL-7 keeps your lymphocytes alive and expanding. A peptide that blocks it would dampen the immune response to whatever microbe is wearing it — an **immune shield**. That reframes everything: the same cassette in commensals *and* in *C. difficile* isn't a coincidence — the trait being traded is *invisibility*. In a friendly bug it buys quiet coexistence; carried into a pathogen, the same shield helps it persist. (0:25)

**[S10 · The go/no-go assay]**
And it's testable in a week. Readout: STAT5 phosphorylation in IL-7-responsive T cells. Arm A — MIMIC alone: does it fire the receptor? Arm B, the real test — MIMIC against IL-7: does it *block* the signal? Positive controls: native IL-7, an anti-IL7R antibody. Negatives: scrambled peptide, an IL-2 line for specificity. If MIMIC suppresses IL-7 with no agonism, the shield hypothesis holds. (0:22)

**[S11 · Close — the axis]**
MIMIC is one peptide. But if commensals shield themselves by speaking to our immune receptors — and trade that shield on mobile elements — the gut holds a whole *library* of human-receptor ligands. Mobile, disease-linked, almost entirely unread. There's an axis of microbe–host communication here we've barely begun to explore. (0:15)

---
**Total ≈ 3:00** (11 slides). Protect S6 (staged structure), S9 (shield), S10 (assay); trim S2 if long. Backup if WebGL fails: static structure figure `struct_078_vs_il7.png`.
