# -*- coding: utf-8 -*-
"""
@author: Simon Biswas 
"""

import random
        
def gen_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) 
        y = random_pick(population, probabilities) 
        child = crossover(x, y) 
        if random.random() < mutation_probability:
            child = mutation(child)
        print_chr_fit(child)
        new_population.append(child)
        if fitness(child) == maxFit: break
    return new_population

def crossover(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutation(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def print_chr_fit(chrom):
    print("Chromosome = {},  Fitness = {}"
        .format(str(chrom), fit(chrom)))
    
def random_chromosome(size): 
    return [ random.randint(1, nq) for _ in range(nq) ]

def fit(chromosome):
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for x in range(2*n-1):
        counter = 0
        if left_diagonal[x] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[x] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
        res = int(maxFit - (horizontal_collisions + diagonal_collisions)) 
    return res
    

def probability(chromosome, fitness):
    p = fitness(chromosome) / maxFit
    return p

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Exception occured"



if __name__ == "__main__":
    nq = int(input("Number of Queens?"))
    maxFit = (nq*(nq-1))/2 
    pop = [random_chromosome(nq) for _ in range(4)]
    
 
    
    generation = 1

    while not maxFit in [fit(chrom) for chrom in pop]: 
        print("Generation {}".format(generation))
        pop = gen_queen(pop, fit)
        print("")
        print("Maximum Fit = {}".format(max([fit(n) for n in pop])))
        generation += 1
    chrom_out = []
    print("Solved in Gen {}!".format(generation-1))
    for chrom in pop:
        if fit(chrom) == maxFit:
            print("");
            print("A solution: ")
            chrom_out = chrom
            print_chr_fit(chrom)
            
    mat = []

    for i in range(nq):
        mat.append(["i"] * nq)
        
    for j in range(nq):
        mat[nq-chrom_out[j]][j]="Q"
            

    def print_board(board):
        for row in board:
            print (" ".join(row))
            
    print_board(mat)



