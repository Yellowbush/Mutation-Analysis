# Jason Sy
# B Bio 340: Intro to Bioinformatics
# 12/10/2022
#
# dictionary for chemical classes


def get_class(sequence):
    chemical_dict = {
        "Arg" : "Elecetrically Charged Side Chains, Positive",
        "His" : "Elecetrically Charged Side Chains, Positive",
        "Lys" : "Elecetrically Charged Side Chains, Positive",
        "Asp" : "Elecetrically Charged Side Chains, Positive",
        "Glu" : "Elecetrically Charged Side Chains, Negative",
        "Ser" : "Polar Uncharged Side Chains",
        "Thr" : "Polar Uncharged Side Chains",
        "Asn" : "Polar Uncharged Side Chains",
        "Gln" : "Polar Uncharged Side Chains",
        "Cys" : "Special Cases",
        "Gly" : "Special Cases",
        "Pro" : "Special Cases",
        "Ala" : "Hydrophobic Side Chains",
        "Val" : "Hydrophobic Side Chains",
        "Ile" : "Hydrophobic Side Chains",
        "Leu" : "Hydrophobic Side Chains",
        "Met" : "Hydrophobic Side Chains",
        "Phe" : "Hydrophobic Side Chains",
        "Tyr" : "Hydrophobic Side Chains",
        "Trp" : "Hydrophobic Side Chains",
    }

    chemical_class = ""
    amino_acid = [sequence]

    for chemical in amino_acid:
        chem_class = chemical
        if chemical in chemical_dict.keys():
            chem_class = chemical_dict[chemical]
        chemical_class += chem_class
            
    return chemical_class
