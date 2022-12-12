# Jason Sy
# B Bio 340: Intro to Bioinformatics
# 11/25/2022
#
# Program transcripts DNA to RNA or translates RNA to Protein



class Convert:

    #constructor
    def __init__(self, sequence):
        self._sequence = sequence
    
    #getter
    def get_sequence(self):
        return self._sequence
    
    #setter
    def set_sequence(self, sequence):
        self._sequence = sequence

    #determine if sequence is RNA or DNA
    def read_sequence(self):
        if "U" in self._sequence or "u" in self._sequence:
            print("\nRNA Detected.")
            return "RNA"
        else:
            print("\nDNA Detected.")
            return "DNA"

    # Transcribes DNA to RNA
    def transcription(self):
        dna_rna = {
            "A" : "U",
            "G" : "C",
            "C" : "G",
            "T" : "A"}
        rna = "Transcribed RNA: \t"
        for dna in self._sequence:
            rna += dna_rna[dna]
        return rna

    # Translates RNA to DNA
    def translation(self):
        codons = {
            "UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
            "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
            "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",
            "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",
            "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
            "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
            "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
            "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
            "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
            "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
            "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
            "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
            "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
            "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
            "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
            "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}
        
        aa_profile = "Translated Protein: \t"

        #Break RNA into List of 3 nucleotides
        rna = [self._sequence[i:i+3] for i in range(0, len(self._sequence), 3)]

        if not len(rna) % 3 == 0:
            error = "RNA is not divisible by three!"
            return error

        #For loop to begin defining protein
        for codon in rna:
            profile = codon
            if codon in codons.keys():
                profile = codons[codon]
            aa_profile += profile
            
        return aa_profile
    
    

    def __str__(self):
        read = self.read_sequence()
        if read == "DNA":
            return self.transcription()
        if read == "RNA":
            return self.translation()
        
    def __repr__(self):
        read = self.read_sequence()
        if read == "DNA":
            return self.transcription()
        if read == "RNA":
            return self.translation()