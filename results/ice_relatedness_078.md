# Are the MIMIC-carrying ICEs related?  — Yes.

**Question (Kenneth):** are the ICE elements themselves related, or just the peptide? Would
be interesting to see conservation beyond the peptide.

**Answer, from the flanking-gene annotations (results/mge_context_078.tsv):** the four
mobile loci carrying MIMIC are not independent captures — they share the same conjugative
machinery.

| Locus (species) | MGE frac | ICE signature |
|---|---|---|
| MBH7027273 (C. difficile) | 0.34 | integrase + excisionase + IS3 + **ArdA** + **Tcp** |
| WP_005428625 (V. fastidiosa) | 0.18 | **MobT relaxase** + **Tcp** + **ArdA** + recombinase |
| WP_055258568 (A. hadrus) | 0.20 | **Tcp** + **ArdA** + recombinase |
| WP_131022233 (C. difficile) | 0.20 | **MobT relaxase** + **Tcp** + **ArdA** + Tyr-recombinase |
| WP_052829451 (B. breve) | 0.00 | chromosomal (the one non-mobile copy) |

**Shared core:** **Tcp** (conjugative transfer proteins) and **ArdA** (anti-restriction,
protects incoming DNA from host restriction on transfer) appear in **4/4** ICE loci; MobT
relaxase in 2/4. This is the conserved backbone of a **Tn916 / Tcp-type conjugative
transposon** — the same ICE family, carried across genera, not convergent independent
mobilization.

**Interpretation.** The peptide is conserved (96% MSA), and so is its *vehicle*. MIMIC is
cargo on a recognizable, self-transmissible conjugative element whose transfer and
anti-restriction machinery travel with it. That is exactly the architecture required for the
"mobile immune-shield trait" hypothesis: a functional peptide + the apparatus to move it
between hosts, including into *C. difficile*.

**Caveat.** This is annotation-level (product names from the locus windows), not a
nucleotide alignment of the elements end-to-end. A full ICE alignment (element boundaries,
oriT, synteny of the transfer operon) would firm up "same element" vs "same ICE family" — a
clean next step, but the shared Tcp+ArdA+relaxase core already rules out independent capture.
