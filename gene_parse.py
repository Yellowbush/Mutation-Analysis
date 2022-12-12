# Jason Sy
# B Bio 340: Intro to Bioinformatics
# 11/25/2022
#
# Parses FASTA File

class GeneParse:

    #Parse text file or FASTA
    def parser(infile):
        seqs = []
        headers = []
        with open(infile) as f:
            sequence = ""
            header = None
            for line in f:
                if line.startswith('>'):
                    headers.append(line[1:-1])
                    if header:
                        seqs.append([sequence])
                    sequence = ""
                    header = line[1:]
                else:
                    sequence += line.rstrip()
            seqs.append([sequence])
        return headers, seqs

    #Count Nucleotides
    def count_nucelotides(sequence):
        nuc_dict = {
            "g" : "Guanine ", "G" : "Guanine",
            "c" : "Cytosine ", "C" : "Cytosine",
            "a" : "Adenine ", "A" : "Adenine",
            "t" : "Thymine ", "T" : "Thymine "}

        

        firstthree = sequence[:3]
        g = sequence.upper().count('G') 
        c = sequence.upper().count('C')
        a = sequence.upper().count('A')
        t = sequence.upper().count('T')

        gc = (g + c)
    
        total = (g + c + a + t)
        
        gc_content = (gc/total * 100)

        codons = (total//3)

    
        name_of_first_three = nuc_dict[firstthree[0]]
        name_of_first_three += nuc_dict[firstthree[1]]
        name_of_first_three += nuc_dict[firstthree[2]]

        return '\n Total = {}\n Codons = {} \n First Three Nucleotides = {}\n Name of First Three Nucleotides = {} \n GCs = {} %\n G = {}, C = {}, A = {}, T = {}.'.format(total, codons, firstthree, name_of_first_three, round(gc_content, 2), g, c, a, t, )