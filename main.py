import biolib

def readFromFile(type, file):
    f = open(file, "r")
    if type == 0:
        string =

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    string = readFromFile(0, "")
    """ Rosalind Counting nucleotides
    
    nucleotides_counted = biolib.count_nucleotides(string)
    for nucleotide in nucleotides_counted:
        print(nucleotides_counted[nucleotide], end= ' ')
        
    """

    """ Rosalind Transcribing DNA into RNA
    
    rna_string = biolib.dna_to_rna(string)
    print(rna_string)
    
    """

    """ Rosalind Complementing a Strand of DNA 
    
    print(biolib.build_complement(string))
    
    """

    """ Wascally Wabbits  """

    print(biolib.rabbit_reproduction(5, 3))

