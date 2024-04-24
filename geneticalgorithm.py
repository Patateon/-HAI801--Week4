import random

# Fonction de création de la population initiale
def initialiser_population(taille_population, longueur_chromosome):
    population = []
    for _ in range(taille_population):
        chromosome = [random.randint(0, 1) for _ in range(longueur_chromosome)]
        population.append(chromosome)
    return population

# Fonction d'évaluation des performances d'un individu (ici, la fonction de fitness)
def evaluer_fitness(chromosome):
    # Code pour évaluer les performances du programme d'échecs avec les paramètres du chromosome
    fitness = random.randint(0, 100) # Calcule la performance du programme d'échecs avec les paramètres du chromosome
    return fitness

# Opérateur de sélection des individus pour la reproduction
def selection(population, taille_selection):
    parents = random.sample(population, taille_selection)
    return parents

# Opérateur de croisement (crossover)
def croisement(parent1, parent2):
    point_croisement = random.randint(1, len(parent1) - 1)
    enfant1 = parent1[:point_croisement] + parent2[point_croisement:]
    enfant2 = parent2[:point_croisement] + parent1[point_croisement:]
    return enfant1, enfant2

# Opérateur de mutation
def mutation(chromosome, taux_mutation):
    for i in range(len(chromosome)):
        if random.random() < taux_mutation:
            chromosome[i] = 1 - chromosome[i]  # Mutation en inversant le bit
    return chromosome

# Algorithme génétique principal
def algorithme_genetique(taille_population, longueur_chromosome, nb_generations, taux_mutation):
    population = initialiser_population(taille_population, longueur_chromosome)
    for generation in range(nb_generations):
        # Évaluation de la fitness de chaque individu dans la population
        fitness_population = [evaluer_fitness(chromosome) for chromosome in population]
        
        # Sélection des parents pour la reproduction
        parents = selection(population, taille_population // 2)
        
        # Croisement des parents pour créer une nouvelle génération
        nouvelle_generation = []
        while len(nouvelle_generation) < taille_population:
            parent1, parent2 = random.choices(parents, k=2)
            enfant1, enfant2 = croisement(parent1, parent2)
            enfant1 = mutation(enfant1, taux_mutation)
            enfant2 = mutation(enfant2, taux_mutation)
            nouvelle_generation.extend([enfant1, enfant2])
        
        # Remplacer l'ancienne population par la nouvelle génération
        population = nouvelle_generation
    
    # Retourner le meilleur individu après les générations
    meilleur_chromosome = max(population, key=evaluer_fitness)
    return meilleur_chromosome

if __name__ == "__main__":
    # Exemple d'utilisation
    taille_population = 100
    longueur_chromosome = 70
    nb_generations = 50
    taux_mutation = 0.05

    meilleur_chromosome = algorithme_genetique(taille_population, longueur_chromosome, nb_generations, taux_mutation)
    print("Meilleur chromosome trouvé :", meilleur_chromosome)
