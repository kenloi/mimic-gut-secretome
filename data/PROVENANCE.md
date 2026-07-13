# Data provenance

- **Peptide catalog:** Global Microbial smORF Catalog (GMSC), gut habitat, high-quality,
  predicted-secreted family representatives. Accessed 2026-07.
- **Human receptors:** UniProt (sequences), PDB (reference structures).
- **Experimental IL-7 complex:** PDB 3DI2 (IL-7 . IL7R).
- **Homolog loci:** DIAMOND/MMseqs hits -> NCBI nuccore windows (Entrez).
- **ClinVar variants:** EBI Proteins API variation endpoint.

Large intermediate files (the full 7,408-fold matrices) are not committed; pointers only.

## Per-table reproducibility (honest status)

| Table | How it was produced | Committed code? |
|---|---|---|
| `mge_enrichment_null.tsv` | permutation null over 592 families | **yes** — `src/mge_enrichment_null.py`, runs on the committed input |
| `mmseqs_breadth_078.tsv` | MMseqs 3-iter search of 078 mature vs UniProtKB | command documented (below); DB is cluster-resident |
| `reranked_candidate_table.tsv`, `reranked_candidates_full.tsv` | ESMFold2-Fast co-fold matrix → decoy-z gate → occlusion/expression axes | derived from the fold matrix (a pointer, not committed — 7,408 GPU folds); scoring logic described in the README |
| `clinvar_finding_078.tsv` | EBI Proteins variation API → epitope overlap + permutation null | API + method described; driver not committed |
| `agonist_vs_antagonist_078.tsv` | hand-curated hypothesis/decision table | n/a (not computed) |

**Honest statement:** one result (`mge_enrichment_null`) regenerates out-of-the-box from
committed code and input. The rest depend on the GPU fold matrix (too large to commit; a
stable pointer) and on analysis steps described in the README rather than shipped as scripts.
We flag this rather than claim full one-command reproducibility we don't yet have. The fold
matrix and the per-step drivers can be provided on request.

**MMseqs breadth command** (DB is cluster-resident UniProtKB 2025_01):
`mmseqs easy-search q078_mature.faa <uniprot_kb_db> hits.tsv tmp --num-iterations 3
--format-output "query,target,pident,alnlen,evalue,bits,taxid,taxname,theader"`
