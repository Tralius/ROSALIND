def count_nucleotides(dna_string):
    nucleotides = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    for nucleotide in dna_string:
        nucleotides[nucleotide] += 1
    return nucleotides


def dna_to_rna(dna_string):
    rna_string = ''
    for nucleotide in dna_string:
        if nucleotide == 'T':
            rna_string += 'U'
        else:
            rna_string += nucleotide
    return rna_string


def build_complement(dna_string):
    complement_string = ''
    complement_nucleotides = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    for nucleotide in dna_string:
        complement_string += complement_nucleotides[nucleotide]
    return complement_string[::-1]