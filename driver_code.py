# Jason Sy
# B Bio 340: Intro to Bioinformatics
# 11/25/2022
#
# Driver code requires: detect_mutation.py, gene_parse.py, transcription_translate.py

import transcription_translate
import detect_mutation
import gene_parse
from pathlib import Path


d_mutate = detect_mutation.Mutation
g_count = gene_parse.GeneParse
tt = transcription_translate.Convert


if __name__ == '__main__':
    while True:
        option = input("T : Transcribe/Translate \nD : Detect Mutation \nC : Count Nucleotides \
            \nE : Exit \nChoose an Option (T, D, C, E): ")

        #Assumes DNA file or RNA file
        #inherits parser from gene_parse.py
        #Uses Convert class to convert DNA to RNA or RNA to protein
        if option == "T" or option == "T".lower():
            d = input("Enter File Location: ")
            headers, seqs = g_count.parser(d)
            dna = ''.join([item for sublist in seqs for item in sublist])
            for header, seq in zip(headers, dna):
                print(headers, tt(dna))
            break

        #Assumes protein file
        #inherits parser from gene_parse.py
        #Uses mutation class to detect mutation type and similairty
        if option == "D" or option == "D".lower():
            original = ""
            mutation = ""

            #orignal sequence
            o = input("\nEnter Original Sequence Location: ")
            o_headers, o_seqs = g_count.parser(o)
            original = ''.join([item for sublist in o_seqs for item in sublist])
            
            #mutated sequence
            m = input("\nEnter Mutation Sequence Location: ")
            m_headers, m_seqs = g_count.parser(m)
            mutation = ''.join([item for sublist in m_seqs for item in sublist])

            print(d_mutate(original, mutation, 0, ""))
            break
                
            
        #Assumes DNA file
        #inherits parser + count_nucleotide from gene_parse.py
        if option == "C".upper().lower():
            fasta = input("\nEnter File Location: ")
            headers, seqs = g_count.parser(fasta)
            flat_seqs = [item for sublist in seqs for item in sublist]
            for header, seq in zip(headers, flat_seqs):
                print(header, g_count.count_nucelotides(seq))
            break

        if option == "E" or option == "E".lower():
            break

        print("\nInvalid Please Enter Valid Option!")