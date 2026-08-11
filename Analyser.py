# ==============================================================================
# Project: Automated DNA Sequence Analyzer & Mutation Tracker
# Author: Class 12 Student (PCB) & Aspiring Genomic Data Scientist
# Purpose: Educational prototype demonstrating basic computational biology logic
# ==============================================================================

# Codon map for translation
CODON_TABLE = {
    "AUG": "Methionine (START)", "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}

def analyze_sequence(dna):
    """Transcribes DNA to RNA and calculates GC content percentage."""
    dna = dna.upper().strip()
    rna = dna.replace("T", "U")
    
    # Calculate GC Content
    g_count = dna.count('G')
    c_count = dna.count('C')
    gc_content = ((g_count + c_count) / len(dna)) * 100 if len(dna) > 0 else 0
    
    return rna, round(gc_content, 2)

def find_mutations(healthy_dna, patient_dna):
    """Compares two DNA sequences to detect single nucleotide polymorphisms (SNPs)."""
    healthy = healthy_dna.upper().strip()
    patient = patient_dna.upper().strip()
    mutations = []
    
    # Check minimum length to avoid index errors
    min_length = min(len(healthy), len(patient))
    
    for i in range(min_length):
        if healthy[i] != patient[i]:
            mutations.append(f"Position {i+1}: Healthy base '{healthy[i]}' mutated to '{patient[i]}'")
            
    return mutations

# Execution Example
if __name__ == "__main__":
    print("--- Genomic Analysis Tool Launching ---")
    
    # Sample Test Data (6-letter sequences)
    normal_dna = "ATGTTT"
    mutated_dna = "ATGTTG"
    
    rna_seq, gc_pct = analyze_sequence(normal_dna)
    detected_mutations = find_mutations(normal_dna, mutated_dna)
    
    print(f"Original DNA: {normal_dna}")
    print(f"Transcribed RNA: {rna_seq}")
    print(f"GC Content Stability Score: {gc_pct}%")
    print(f"Detected Variant Alterations: {detected_mutations}")
