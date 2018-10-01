from utils.queens import *
from utils.general import guess
from utils.priority_queue import priority_queue
__MAX_GENERATIONS = 5000

def random_population(popul_size, board_size):
    population = []
    for i in range(popul_size):
        population.append(n_sized_board(board_size))

    return population

def main():
    population_size = 150
    board_size = 4
    population = random_population(population_size, board_size)

    for epoch in range(__MAX_GENERATIONS):
        print('Epoch: {}, random sample: {}'.format(epoch, population[0]))

        fittest_population = priority_queue('fitness')

        for individual in population:
            fitness_value = h(individual)

            fittest_population.enqueue(
                {
                    'fitness': fitness_value,
                    'board': individual
                 }
            )

        for i in range(2):
            rand = guess()

            rand_index = population_size * rand**5 # rand^5

# poop, gave up

main()
