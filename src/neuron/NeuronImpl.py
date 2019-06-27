'''
Created on 9 de jun de 2019

@author: zeller
'''
from neuron.Neuron import Neuron

class NeuronImpl(Neuron):
    '''
    Represents a default neuron of a neural network
    '''

    def __init__(self, identifier, activationFunction):
        self.id = identifier
        self.activationFunction = activationFunction
        self.inputs = set()
        self.outputs = set()
        
        
    def addInputSynapse (self, synapse):
        """Implementation of abstract Neuron class"""
        self.inputs.add (synapse)
        
    def addOutputSynapse (self, synapse):
        self.outputs.add(synapse)
    
    def setActivateFunction(self, activateFunction):
        self.activationFunction = activateFunction
        
    def weightedInputs(self):
        weightedInputs = 0.0
        for synapse in self.inputs:
            weightedInputs += synapse.getAnterior.activate()
            
        return weightedInputs
        
    def activate(self):
        return self.activationFunction.calculate(self.weightedInputs())
    
    def activateWithWeightedInputs(self, weightedInputs):
        return self.activationFunction.calculate(weightedInputs)
    
    def countOutputSynapse(self):
        return len(self.outputs)
    
    def getId(self):
        return self.id
    
    def setId(self, neuronIdentifier):
        self.id = neuronIdentifier
    
    def getInputSynapses(self):
        return self.inputs
    
    def getOutputSynapses(self):
        return self.outputs