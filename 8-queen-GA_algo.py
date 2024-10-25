import random
def fitness_score(seq):
    score = 0
    
    for row in range(8):
        col = seq[row]
        
        for other_row in range(8):
            
            #queens cannot pair with itself
            if other_row == row:
                continue
            if seq[other_row] == col:
                continue
            if other_row + seq[other_row] == row + col:
                continue
            if other_row - seq[other_row] == row - col:
                continue
            #score++ if every pair of queens are non-attacking.
            score += 1
    return score

import itertools
def crossover(parents):
    
    #random indexes to to cross states with
    cross_points = random.sample(range(8), 3 - 1)
    offsprings = []
    
    #all permutations of parents
    permutations = list(itertools.permutations(parents, 3))
    
    for perm in permutations:
        offspring = []
        
        #track starting index of sublist
        start_pt = 0
        
        for parent_idx, cross_point in enumerate(cross_points):    #doesn't account for last parent
            
            #sublist of parent to be crossed
            parent_part = perm[parent_idx][start_pt:cross_point]
            offspring.append(parent_part)
            
            #update index pointer
            start_pt = cross_point
            
        #last parent
        last_parent = perm[-1]
        parent_part = last_parent[cross_point:]
        offspring.append(parent_part)
        
        #flatten the list since append works kinda differently
        offsprings.append(list(itertools.chain(*offspring)))
    
    return offsprings

def mutate(seq):
    for row in range(len(seq)):
        if random.random() < 0.1:
            seq[row] = random.randrange(8)
    
    return seq

def select(population):
    # Consider implementing tournament selection here for possible improvement

    max_score = sum(fitness_score(ind) for ind in population)
    pick = random.uniform(0, max_score)
    current = 0
    for individual in population:
        current += fitness_score(individual)
        if current > pick:
            return individual
        
def genetic_algorithm():
    population = [random.sample(range(8), 8) for _ in range(100)]  # Ensure initial population creation
    best_fitness_seen = 0
    stagnation_count = 0
    for generation in range(3000):
        if not population:  # Check for empty population before processing
            print(f"Error: Empty population encountered in generation {generation}.")
            return None

        new_population = []
        for _ in range(100 // 2):
            parent1 = select(population)  # Ensure selection returns a valid individual
            parent2 = select(population)
            children = crossover([parent1, parent2])
            for child in children:
                mutate(child)
                new_population.append(child)

        # ... rest of the loop logic for fitness evaluation, stagnation check, etc.

        population = new_population

    return max(population, key=fitness_score)

# Run the genetic algorithm
solution = genetic_algorithm()
print(solution)

# End of one.py