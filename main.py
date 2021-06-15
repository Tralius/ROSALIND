import biolib


def readFromFile(type, file):
    f = open(file, "r")
    if type == 0:
        dna_string = f.read()
        return dna_string
    elif type == 1:
        temp_database = {}
        id = ""
        for line in f:
            if line.find('>') > -1:
                id = line[1:-1]
                temp_database[id] = ""
            else:
                temp_database[id] += line[:-1]

        return temp_database


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    """ Rosalind Counting nucleotides
    
    string = readFromFile(0, "input.txt")
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

    """ Wascally Wabbits 

    print(biolib.rabbit_reproduction(5, 3))
    
    """

    dna_database = readFromFile(1, "input.txt")
    id, percentage = biolib.gc_content(dna_database)
    print(id, percentage, sep="\n")