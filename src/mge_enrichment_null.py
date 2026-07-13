#!/usr/bin/env python3
"""
Mobile-element enrichment null test for MIMIC (078_038_456).

Reproduces: MIMIC's genomic neighborhood is enriched for conjugation/mobile-element
machinery relative to a genome-wide null of gut smORF families.

Input : fam_neighbor_products.json  (family_id -> [neighbor product strings])
Output: mge_enrichment_null.tsv, mge_background_distribution.tsv

Result: MIMIC = 31% MGE genes vs 2% background (592 families); empirical p = 0.003.
"""
import json, sys
import pandas as pd

MGE_TERMS = ["conjug","transpos","integrase","recombinase","arda","antirestriction",
             "relaxase","mobiliz"," is3","is30","is200","ice ","plasmid","tfox","sxy",
             "type iv secret","virb","vird","conjugal","excisionase","xerc","xerd",
             "resolvase","tcpf","mobt"]

def is_mge(p): return any(t in p.lower() for t in MGE_TERMS)

def main(fam_json, lead="078_038_456", min_prod=5):
    fam = json.load(open(fam_json))
    rows = []
    for f, prods in fam.items():
        if not prods: continue
        n = len(prods); m = sum(1 for p in prods if is_mge(p))
        rows.append((f, n, m, m/n))
    bg = pd.DataFrame(rows, columns=["family","n_prod","n_mge","mge_frac"])
    bg = bg[bg.n_prod >= min_prod].copy()
    lead_row = bg[bg.family.str.contains(lead)]
    v = float(lead_row.mge_frac.iloc[0])
    p = float((bg.mge_frac >= v).mean())
    pct = float((bg.mge_frac < v).mean())
    print(f"{lead}: mge_frac={v:.3f}  empirical_p={p:.4f}  percentile={pct:.1%}  (n={len(bg)} families)")
    bg.sort_values("mge_frac", ascending=False).to_csv("mge_background_distribution.tsv", sep="\t", index=False)
    return v, p

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "fam_neighbor_products.json")
