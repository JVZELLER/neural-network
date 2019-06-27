'''
Created on 9 de jun de 2019

@author: zeller
'''
from neuron.NeuronImpl import NeuronImpl

class InputNeuron(NeuronImpl):
    '''
    Represents a value getting into the network
    '''


    def __init__(self, neuronIdentifier):
        super(neuronIdentifier, None)
        self.x = None
        
    def getX (self):
        return self.x
    
    def setX (self, x):
        self.x = x
        
    def activate(self):
        return self.x
    
    def activateWithWeightedInputs(self, weightedInputs):
        return self.x
    
    def weightedInputs(self):
        return self.x
    
    def addInputSynapse(self, synapse):
        raise ValueError('This is an input neuron, it can\'t receive input synapses')
        