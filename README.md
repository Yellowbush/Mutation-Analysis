# Mutation-Analysis

### Introduction:
The purpose of this project is to understand more about the relationship between mutation and protein structures. Mutation are random changes in the structure of a gene, that can result in variant forms transmitted to subsequent generations [1]. They are random in the sense that they can’t be predicted exactly when and where a specific mutation will occur. There are many different ways for mutation to occur and certain mutations are deemed deleterious. Deleterious mutations are chances in DNA sequences that puts an individual at risk of developing certain genetic disorder or disease [2]. In the article by Yuan, et al., describes how recurrent deletions at 30 genomics regions are likely to drive recessive diseases [4]. And in the article by Ruan, et al. discusses usage of simulations to predict traits and disease risk [3]. Which brings to question: To what extent are we able to predict deleterious mutations? We know that mutations are random in the sense that we do not know if the fitness effect will be either adaptive, neutral, or deleterious. Mutations such as frameshift and missense are more likely to have deleterious effects than mutations like silent mutations because the structure of the protein changes.

### Sources:
[1] Brian Charlesworth, The Effects of Deleterious Mutations on Evolution at Linked Sites, Genetics, Volume 190, Issue 1, 1 January 2012, Pages 5–22, https://doi.org/10.1534/genetics.111.134288

[2] MULLER HJ. Our load of mutations. Am J Hum Genet. 1950 Jun;2(2):111-76. PMID: 14771033; PMCID: PMC1716299.

[3] Ruan, Y., et al. Improving polygenic prediction in ancestrally diverse populations. Nature Genetics 54, 573–580 (2022). https://scholar.harvard.edu/tge/publications/improving-polygenic-prediction-ancestrally-diverse-populations.

[4] Yuan B, Schulze KV, Assia Batzir N, Sinson J, Dai H, Zhu W, Bocanegra F, Fong CT, Holder J, Nguyen J, Schaaf CP, Yang Y, Bi W, Eng C, Shaw C, Lupski JR, Liu P. Sequencing individual genomes with recurrent genomic disorder deletions: an approach to characterize genes for autosomal recessive rare disease traits. Genome Med. 2022 Sep 30;14(1):113. doi: 10.1186/s13073-022-01113-y. PMID: 36180924; PMCID: PMC9526336.

### Data Sources
FASTA files of genomes retrieved from The National Center for Biotechnology Information.
Example data as references to test code.

### Hypothesis and analytical approach
Hypothesis: Deleterious mutations will have a significant effect on protein structure.

Null Hypothesis: Deleterious mutation will not have a significant effect on protein structure.
The purpose of the hypothesis is to test the relationship between mutations and protein structures. And I plan to test this by creating a random mutator on python that involves insertion, deletion, missense, silent, nonsense, and duplication mutation. Then use a predictor created with python to see if predictions are possible to detect changes to protein structure and what type of mutation occurred.

Parse files

Transcription

Translator

Dictionaries for Codon Table, and Chemical Class

Gene Comparison

Database: UniProt, NCBI

See if differences in protein structure contribute to diseases
