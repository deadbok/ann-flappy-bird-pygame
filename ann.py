'''
Artificial Neural Network.

@since: 14/08/2015
@author: oblivion
'''
import random


def print_neuron(neuron):
    '''
    Print the internal values of a neuron.

    :param neuron: The neuron to print from
    '''
    for weight in neuron.weights:
        print(str(weight) + ", ", end="")
    print()


class Neuron(object):
    '''An artificial neuron.'''

    def __init__(self, inputs):
        self.inputs = list()
        self.weights = list()
        self.output = 0

        while inputs > 0:
            self.inputs.append(0)
            self.weights.append(random.uniform(-1, 1))
            inputs -= 1
        # Threshold
        self.weights.append(random.uniform(-1, 1))


    def activation(self):
        '''Calculate the activation value.'''
        ret = 0.0

        for index in range(0, len(self.inputs)):
            ret += self.inputs[index] * self.weights[index]
        return ret

    def state(self):
        '''Get the output state.'''
        # The last weight is actually the threshold, but adding it to the list
        # makes it easier to modify by the GA.
        self.output = self.activation() - self.weights[-1]
        return self.output


class ANNLayer(object):
    '''A layer of neurons.'''
    def __init__(self, inputs, neurons):
        '''
        Create a layer.

        :param inputs: Number of inputs of each neuron.
        :param neurons: Number of neurons in the layer.
        '''
        self.neurons = list()
        while neurons > 0:
            self.neurons.append(Neuron(inputs))
            neurons -= 1

    def set_inputs(self, inputs):
        '''
        Set inputs from an array.

        :param inputs: Array of input values.
        '''
        for neuron in self.neurons:
            neuron.inputs = inputs

    def get_ouputs(self):
        '''
        Get all outputs as an array.
        '''
        ret = list()
        for neuron in self.neurons:
            ret.append(neuron.state())
        return ret


class ANNInputLayer(ANNLayer):
    '''An input layer of neurons. Has only one input per neuron.'''
    def __init__(self, neurons):
        '''
        Create input layer.

        :param neurons: Number of neurons in the layer.
        '''
        ANNLayer.__init__(self, 1, neurons)

    def set_inputs(self, inputs):
        '''
        Set inputs from an array.

        :param inputs: Array of input values.
        '''
        n = 0
        for neuron in self.neurons:
            neuron.inputs[0] = inputs[n]
            n += 1


class ANNOutputLayer(ANNLayer):
    '''An output layer of neurons. Has only one neuron.'''
    def __init__(self, inputs):
        '''
        Create output layer.

        :param inputs: Number of inputs of each neuron.
        '''
        ANNLayer.__init__(self, inputs, 1)

    def set_inputs(self, inputs):
        '''
        Set inputs from an array.

        :param inputs: Array of input values.
        '''
        self.neurons[0].inputs = inputs


class ANN(object):
    '''Artificial Neural Network that plays Flappy Bird.'''
    def __init__(self):
        '''
        Build the ANN.
        '''
        self.layers = list()
        self.layers.append(ANNInputLayer(3))
        self.layers.append(ANNLayer(3, 7))
        self.layers.append(ANNLayer(7, 4))
        self.layers.append(ANNOutputLayer(4))

    def action(self, flappy_data):
        '''
        Decide from game data if Fappy should go up.
        '''
        # Run the game data through the network.
        self.layers[0].set_inputs(flappy_data)
        self.layers[1].set_inputs(self.layers[0].get_ouputs())
        self.layers[2].set_inputs(self.layers[1].get_ouputs())
        self.layers[3].set_inputs(self.layers[2].get_ouputs())

        ret = self.layers[2].get_ouputs()[0] > 1
        return ret

    def get_internal_data(self):
        '''
        Get all weights and thresholds as a list.
        '''
        ret = list()
        for layer in self.layers:
            for neuron in layer.neurons:
                ret.extend(neuron.weights)
        return ret

    def set_internal_data(self, data):
        '''
        Set all weights and thresholds from an list.
        '''
        index = 0
        for layer in self.layers:
            for neuron in layer.neurons:
                next_index = index + len(neuron.weights)
                neuron.weights = data[index: next_index]
                index = next_index
