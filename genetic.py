'''
@since: 14/08/2015
@author: oblivion
'''

import pickle

class FloatGenome(object):
    '''
    Genome created of floats.
    '''
    def __init__(self, genome, fitness, name="Joshua"):
        '''
        Create a genome from an array.

        :param size: Size
        '''
        self.genome = genome
        self.fitness = fitness
        self.name = name
        if len(self.name) > 200:
            self.name = self.name[-50:-1]

    def save(self, filename):
        '''
        Save the genome to a file.
        '''
        with open(filename, 'wb') as genome_file:
            pickle.dump(self, genome_file, -1)

    def load(self, filename):
        '''
        Load a genome from a file.
        '''
        temp = None
        with open(filename, "rb") as genome_file:
            temp = pickle.load(genome_file)

        if temp is not None:
            self.genome = temp.genome
            self.fitness = temp.fitness
            self.name = "lo"
