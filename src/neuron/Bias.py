'''
Created on 9 de jun de 2019

@author: zeller
'''

from neuron.InputNeuron import InputNeuron

class Bias(InputNeuron):
    '''
    Representes neuron's Bias
    '''

    def __init__(self, neuronIdentifier):
        super(neuronIdentifier)
        super().setX(1)
    
        