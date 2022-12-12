# Jason Sy
# B Bio 340: Intro to Bioinformatics
# 11/25/2022
#
# Detects mutation type


from difflib import SequenceMatcher

class Mutation:

    #Constructor
    def __init__(self, original, mutation, similarity, mtype):
        self._original = original
        self._mutation = mutation
        self._similarity = similarity
        self._mtype = mtype


    #Getters
    def get_original(self):
        return self._original
    
    def get_mutation(self):
        return self._mutation
    
    def get_similarity(self):
        return self._similarity
    
    def get_mtype(self):
        return self._mtype
    
    #Setters
    def set_original(self, original):
        self._original = original

    def set_mutation(self, mutation):
        self._mutation = mutation

    def set_similarity(self, similarity):
        self._similarity = similarity

    def set_mtype(self, mtype):
        self._mtype = mtype

    #Calculate similarity between nucleotides
    def calculate_similar(self):
        s = "Protein Similarity Percentage: \t"
        self._similarity = s
        self._similarity += str(round(SequenceMatcher(None, self._original, self._mutation).ratio() * 100, 2))
        return self._similarity

    #Find Mutation types
    def find_mutation_type(self):
        s = "\nMutation Type is: \t"
        self._mtype = ""
        if self._original == self._mutation:
            self._mtype += "Silent"
            return self._mtype
        if len(self._original) > len(self._mutation):
            self._mtype += "Frameshift-Deletion "
        if len(self._original) < len(self._mutation):
            self._mtype += "Frameshift-Insertion "
        if not self._original == self._mutation:
            self._mtype += "Missense "
        self._mtype = self._mtype.split(" ", 1)
        result = s + " + ".join(self._mtype)
        return result
    
    def deleterious(self):
        if not self._mtype == "Silent":
            return True
        else:
            return False
    

    def __str__(self):
        self._mtype = self.find_mutation_type()
        self._similarity = self.calculate_similar()
        if self.deleterious() == True:
            self._mtype += "\n(Mutation has the likelihood of being deleterious)"
        else:
            self._mtype += "\n(Mutation is unlikely to be deleterious)"
        return self._mtype + "\n" + str(self._similarity)
    
    def __repr__(self):
        self._mtype = self.find_mutation_type()
        self._similarity = self.calculate_similar()
        if self.deleterious() == True:
            self._mtype += "\n(Mutation has the likelihood of being deleterious)"
        else:
            self._mtype += "\n(Mutation is unlikely to be deleterious)"
        return self._mtype + "\n" + str(self._similarity)