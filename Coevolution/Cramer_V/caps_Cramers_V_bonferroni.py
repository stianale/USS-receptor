import numpy as np
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from scipy.stats import chi2_contingency
import itertools
import os
import glob
from typing import Dict, List, Tuple

def cramers_v(uss_chars: List[str], protein_chars: List[str]) -> Tuple[float, float]:
    """
    Compute Cramér's V for two categorical variables.
    """
    
    contingency_table = np.zeros((len(set(uss_chars)), len(set(protein_chars))))
    uss_map = {char: i for i, char in enumerate(set(uss_chars))}
    protein_map = {char: i for i, char in enumerate(set(protein_chars))}
    
    for u, p in zip(uss_chars, protein_chars):
        contingency_table[uss_map[u], protein_map[p]] += 1
    
    chi2, p_value, _, _ = chi2_contingency(contingency_table, correction=False)
    n = sum(sum(contingency_table))
    k = min(contingency_table.shape) - 1
    cramers_v = np.sqrt(chi2 / (n * k)) if k > 0 else 0
    
    return cramers_v, p_value

def calculate_caps_score(uss_alignment: MultipleSeqAlignment, protein_alignment: MultipleSeqAlignment) -> Dict:
    """
    Calculate CAPS scores using Cramér's V between USS and protein alignments.
    """
    uss_length = uss_alignment.get_alignment_length()
    protein_length = protein_alignment.get_alignment_length()
    
    results = {'scores': [], 'p_values': [], 'positions': []}
    
    for i in range(uss_length):
        for j in range(protein_length):
            uss_chars = [rec.seq[i] for rec in uss_alignment]
            protein_chars = [rec.seq[j] for rec in protein_alignment]
            
            if len(set(uss_chars)) > 1 and len(set(protein_chars)) > 1:
                v_score, p_val = cramers_v(uss_chars, protein_chars)
                results['scores'].append(v_score)
                results['p_values'].append(p_val)
                results['positions'].append((i, j))
    
    return results

def filter_significant_pairs(results: Dict, alpha: float = 0.05, min_effect: float = 0.3) -> List[Dict]:
    """
    Apply Bonferroni correction and filter significant co-evolving pairs.
    """
    significant_pairs = []
    n_tests = len(results['p_values'])
    corrected_alpha = alpha / n_tests if n_tests > 0 else alpha
    
    for i in range(len(results['p_values'])):
        if results['p_values'][i] < corrected_alpha and results['scores'][i] >= min_effect:
            significant_pairs.append({
                'uss_pos': results['positions'][i][0],
                'protein_pos': results['positions'][i][1],
                'cramers_v': results['scores'][i],
                'p_value': results['p_values'][i]
            })
    
    return significant_pairs

def main():
    uss_files = {os.path.basename(f).split('_USS')[0]: f for f in glob.glob("*_USS.fa")}
    protein_files = {os.path.basename(f).split('.fa')[0]: f for f in glob.glob("*.fa") if '_USS' not in f}
    matching_ogs = set(uss_files.keys()).intersection(protein_files.keys())
    
    if not matching_ogs:
        print("No matching OG files found.")
        return
    
    for og in matching_ogs:
        print(f"Processing {og}")
        uss_alignment = AlignIO.read(uss_files[og], "fasta")
        protein_alignment = AlignIO.read(protein_files[og], "fasta")
        
        if len(uss_alignment) != len(protein_alignment):
            print(f"Sequence count mismatch for {og}")
            continue
        
        results = calculate_caps_score(uss_alignment, protein_alignment)
        significant_pairs = filter_significant_pairs(results)
        
        with open(f"{og}_coevo_Cramers_V_bonferroni_results.txt", "w") as f:
            f.write("USS_Position\tProtein_Position\tCramers_V\tP_value\n")
            for pair in significant_pairs:
                f.write(f"{pair['uss_pos']}\t{pair['protein_pos']}\t{pair['cramers_v']:.3f}\t{pair['p_value']:.2e}\n")
        
        print(f"Results saved for {og}")

if __name__ == "__main__":
    main()