'''
AI that plays Flappy Bird.

@since: 14/08/2015
@author: oblivion
'''
from random import randint
import random

from ann import ANN
from genetic import FloatGenome


class AI(object):
    '''
    Game AI.
    '''
    mutation_rate = 0.10

    def __init__(self, population):
        '''
        Create game AI.

        :param population: Number of AI to evolve.
        '''
        print("Creating game AI.")
        self.genomes = list()
        self.anns = list()
        self.generation = 1
        self.last_avg_fit = 0.0

        index = 0
        while population > 0:
            print("AI's left: " + str(population))
            ann = ANN()
            self.anns.append(ann)
            # Names will get strange if lots of brains are created
            self.genomes.append(FloatGenome(ann.get_internal_data(), 0.0,
                                            chr(ord('a') + index)))
            population -= 1
            index += 1

    def get_avg_fitness(self):
        '''
        Get average fitness.
        '''
        ret = 0.0
        for genome in self.genomes:
            ret += genome.fitness
        ret /= len(self.genomes)
        return ret

    def evolve(self):
        '''
        Evolve AI using genetic algorithms.
        '''
        print("Evolving AI.")
        genomes = len(self.genomes)
        new_genomes = list()
        print("Sorting for best fit.")
        self.genomes.sort(key=lambda genome: genome.fitness, reverse=True)
        avg_fit = self.get_avg_fitness()
        print("Parents fitness: worst {worst}, best {best}, average {avg}, and last average {lavg}.".format(
              worst=str(self.genomes[-1].fitness),
              best=str(self.genomes[0].fitness),
              avg=str(avg_fit),
              lavg=str(self.last_avg_fit)))

        if self.last_avg_fit == avg_fit:
            self.mutation_rate = 0.30
            print("Spiking mutation.")
        else:
            self.mutation_rate = 0.10
        self.last_avg_fit = avg_fit

        index = 0
        # Add some tried and tested genomes from the best half
        added = list()
        while len(new_genomes) < genomes / 3:
            index = randint(0, randint(0, int(genomes / 2)))
            if index not in added:
                print("Adding " + self.genomes[index].name + ".")
                new_genomes.append(FloatGenome(self.genomes[index].genome,
                                               0.0, self.genomes[index].name))
                added.append(index)

        # Crossover
        while len(new_genomes) < genomes:
            first_parent = randint(0, randint(0, genomes - 1))
            second_parent = randint(0, randint(0, genomes - 1))
            print("Splicing parent " + self.genomes[first_parent].name +
                  " and " + self.genomes[second_parent].name + ".")
            if first_parent != second_parent:
                split = randint(0, len(self.genomes[first_parent].genome))
                first_child = self.genomes[first_parent].genome[:split] + self.genomes[second_parent].genome[split:]
                second_child = self.genomes[second_parent].genome[:split] + self.genomes[first_parent].genome[split:]
                new_genomes.append(FloatGenome(first_child, 0.0,
                                               self.genomes[first_parent].name +
                                               self.genomes[second_parent].name))
                if len(new_genomes) < genomes:
                    new_genomes.append(FloatGenome(second_child, 0.0,
                                                   self.genomes[second_parent].name +
                                                   self.genomes[first_parent].name))

        index = 0
        # mutate some individuals
        for genome in new_genomes:
            if random.random() < self.mutation_rate:
                pos = randint(0, len(genome.genome) - 1)
                genome.genome[pos] += random.uniform(min(genome.genome),
                                                     max(genome.genome))
                print(genome.name + " mutated.")
                genome.name += '*'
            # Update the ANN's
            self.anns[index].set_internal_data(genome.genome)
            index += 1

        print(str(len(new_genomes)) + " new genomes.")
        self.genomes = new_genomes
        self.generation += 1
        print("======= Generation " + str(self.generation) + " =======", flush=True)
