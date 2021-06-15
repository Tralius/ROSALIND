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


def gc_content(dna_database):
    fasta_id = ""
    max_percentage = 0.0
    for key in dna_database:
        g_nr = dna_database[key].count('G')
        c_nr = dna_database[key].count("C")
        total = g_nr + c_nr
        temp_percentage = (total/len(dna_database[key]))*100
        if max_percentage < temp_percentage:
            max_percentage = temp_percentage
            fasta_id = key

    return fasta_id, max_percentage


def rabbit_reproduction(gen, k):
    if gen == 1 or gen == 2:
        return k
    else:
        r1 = rabbit_reproduction(gen - 1, k)
        r2 = rabbit_reproduction(gen - 2, k)
        return r1 + r2
