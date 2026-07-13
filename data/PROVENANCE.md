# Data provenance

- **Peptide catalog:** Global Microbial smORF Catalog (GMSC), gut habitat, high-quality,
  predicted-secreted family representatives. Accessed 2026-07.
- **Human receptors:** UniProt (sequences), PDB (reference structures).
- **Experimental IL-7 complex:** PDB 3DI2 (IL-7 . IL7R).
- **Homolog loci:** DIAMOND/MMseqs hits -> NCBI nuccore windows (Entrez).
- **ClinVar variants:** EBI Proteins API variation endpoint.

Large intermediate files (full fold matrices) are not committed; pointers only.
Every table under results/ is regenerable from these sources plus src/.
