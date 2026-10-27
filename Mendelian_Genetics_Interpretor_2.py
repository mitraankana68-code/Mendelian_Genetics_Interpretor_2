# MENDELIAN GENETICS INTERPRETOR

# Parent Genotypes
parent1 = input("Enter the genotype of Parent 1: ")
parent2 = input("Enter the genotype of Parent 2: ")

print("Parent 1: ", parent1)
print("Parent 2: ", parent2)

# Validation
if len(parent1) == 4 and len(parent2) == 4:
    print("Valid genotype entered.")
else:
    print("Invalid genotype entered. Program stopped.")
    quit()

# Allele Extraction
alleles_parent1 = [parent1[0], parent1[1], parent1[2], parent1[3]]
alleles_parent2 = [parent2[0], parent2[1], parent2[2], parent2[3]]

print("Alleles of Parent 1:", alleles_parent1)
print("Alleles of Parent 2:", alleles_parent2)

# Gamete Generation for Parent 1
gene1_parent1 = [parent1[0], parent1[1]]
gene2_parent1 = [parent1[2], parent1[3]]

gametes_parent1 = []

for allele1 in gene1_parent1:
    for allele2 in gene2_parent1:
        gamete = allele1 + allele2
        if gamete not in gametes_parent1:
            gametes_parent1.append(gamete)

# Gamete Generation for Parent 2
gene1_parent2 = [parent2[0], parent2[1]]
gene2_parent2 = [parent2[2], parent2[3]]

gametes_parent2 = []

for allele1 in gene1_parent2:
    for allele2 in gene2_parent2:
        gamete = allele1 + allele2
        if gamete not in gametes_parent2:
            gametes_parent2.append(gamete)

print("Gametes of Parent 1:", gametes_parent1)
print("Gametes of Parent 2:", gametes_parent2)
      
# Punnett Square Generation
punnett_square = []
for gamete_parent1 in gametes_parent1:
    row = []
    for gamete_parent2 in gametes_parent2:
        gene1 = gamete_parent1[0] + gamete_parent2[0]
        gene2 = gamete_parent1[1] + gamete_parent2[1]
        if gene1[0].islower() and gene1[1].isupper():
            gene1 = gene1[1] + gene1[0]
        if gene2[0].islower() and gene2[1].isupper():
            gene2 = gene2[1] + gene2[0]

        offspring_genotype = gene1 + gene2
        row.append(offspring_genotype)
    punnett_square.append(row)

print("Punnett Square:")
for row in punnett_square:
    print(row)

# Offspring Genotype Generation
offspring = []
for row in punnett_square:
    for genotype in row:
        offspring.append(genotype)
print("Offspring Genotype: ", offspring)

# Genotype Counting
counts = {}

for genotype in offspring:
    if genotype not in counts:
        counts[genotype] = 1
    else:
        counts[genotype] = counts[genotype] + 1

print("Genotype Counts:", counts)

# Genotype Percentage
total_offspring = len(offspring)
for genotype in counts:
    percentage = counts[genotype]/ total_offspring * 100
    print("Percentage of ", genotype,":", percentage)

# Phenotype Determination
phenotypes = []
for genotype in offspring:
    phenotypes.append("Dominant" if genotype[0].isupper() else "Recessive")

print("Phenotypes of offsprings: ", phenotypes)

# Phenotype Counting
phenotype_counts = {
    "Dominant": phenotypes.count("Dominant"),
    "Recessive": phenotypes.count("Recessive")
}

print("Dominant phenotype =", phenotype_counts["Dominant"])
print("Recessive phenotype =", phenotype_counts["Recessive"])

# Phenotype Percentage
phenotype_percentage_dominant = phenotype_counts["Dominant"]/total_offspring * 100
phenotype_percentage_recessive = phenotype_counts["Recessive"]/total_offspring * 100


print("Precentage of Dominant: ", phenotype_percentage_dominant)
print("Percentage of Recessive: ", phenotype_percentage_recessive)

# Genotypic Ratio
counts = {}
for genotype in offspring:
    if genotype not in counts:
        counts[genotype] = 1
    else:
        counts[genotype] = counts[genotype] + 1

print("Genotype Counts: ", counts)

# Phenotypic Ratio
phenotypic_counts = {}
for phenotype in offspring:
    if phenotype not in phenotypic_counts:
        phenotypic_counts[phenotype] = 1
    else:
        phenotypic_counts[phenotype] = phenotypic_counts[phenotype] + 1

print("Phenotypic Counts: ", phenotypic_counts)

print("Offspring list: ", offspring)

# Homozygous and Heterozygous Analysis
homozygous_both = []
heterozygous_both = []
mixed = []
for genotype in offspring:
    gene1 = genotype[0:2]
    gene2 = genotype[2:4]
    gene1_homozygous = gene1[0] == gene1[1]
    gene2_homozygous = gene2[0] == gene2[1]
    if gene1_homozygous and gene2_homozygous:
        homozygous_both.append(genotype)
    elif not gene1_homozygous and not gene2_homozygous:
        heterozygous_both.append(genotype)
    else:
        mixed.append(genotype)
print("Homozygous for both genes: ", homozygous_both)
print("Heterozygous for both genes: ", heterozygous_both)
print("Homozygous for one and heterzygous for the other: ", mixed)

# Possible offspring analysis
possible_offspring = set()
for genotype in offspring:
    possible_offspring.add(genotype)
print("Possible offspring genotypes: ", possible_offspring)

