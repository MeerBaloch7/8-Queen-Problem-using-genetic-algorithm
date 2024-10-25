# Genetic-Algorithm
### Genetic algorithms (GAs) are a type of computational optimization technique inspired by the principles of natural selection and genetics. They are used to solve complex problems by mimicking the process of evolution to improve a population of potential solutions iteratively

---

The genetic algorithm begins with an initial population of individuals, typically generated randomly. It then goes through a series of iterations, known as generations or epochs, in which the individuals undergo operations such as selection, crossover, and mutation. These operations mimic the processes of natural selection, and genetic variation observed in biological evolution

### Selection Process:
individuals from the current population are evaluated based on a fitness function, quantifying how well each solution solves the problem. The individuals with higher fitness values are more likely to be selected for further processing, simulating the survival of the fittest.

### Crossover, or recombination
Crossover, or recombination, is a genetic operator where two selected individuals exchange genetic information to create offspring.
### Mutation
Mutation introduces small random changes in the genetic information of selected individuals. 
### Ftiness Function:
The fitness function simply defined is a function which takes a candidate solution to the problem as input and produces as output how “fit” our how “good” the solution is with respect to the problem in consideration.
Calculation of fitness value is done repeatedly in a GA and therefore it should be sufficiently fast. A slow computation of the fitness value can adversely affect a GA and make it exceptionally slow.

The basic structure of a GA is shown in Figure in images
---
# 8-Queen Problem using Genetic Algorithm
#### The 8-Queens problem is a classic combinatorial problem where the objective is to place 8 queens on an 8x8 chessboard such that no two queens threaten each other. This means that no two queens can be in the same row, the same column, or on the same diagonal.

#### Population: 
Each individual in the population is a list representing the column positions of the queens. The index represents the column, and the row represents the value.

Sample population:
Population 1: [0, 4, 7, 5, 1, 3, 6, 2]

**Meaning:**
- Queen in column 0, row 0
- Queen in column 1, row 4
- Queen in column 2, row 7
- Queen in column 3, row 5
- Queen in column 4, row 1
- Queen in column 5, row 3
- Queen in column 6, row 6
- Queen in column 7, row 2

The initial chromosomes are given for your reference. You can create the initial population by yourself too.

**Fitness:** 
Calculates how many pairs of queens do not attack each other. The maximum fitness is 28 (for 8 queens).

**Crossover:**
Crossover exchange moves between adjacent chromosomes after determining maximum fitness value.

**Mutation:** 
Randomly changes the position of one queen to introduce genetic diversity. Can also be done by swapping the position of two queens.










