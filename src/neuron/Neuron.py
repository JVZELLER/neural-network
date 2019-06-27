'''
Created on 9 de jun de 2019

@author: zeller
'''

from abc import ABC, abstractmethod

class Neuron(ABC):
    '''
    Represents neuron behavior
    '''
    
    @abstractmethod
    def activate (self):
        """Activate the neuron running it's activate activate
        Returns:
           Value generate by the activation activate 
        """
    
    @abstractmethod
    def activateWithWeightedInputs (self, weightedInputs):
        """Activate the neuron running it's activate activate
        Args:
            weightedInputs: the sum of inputs multiplyed by weigh.
        Returns:
            Value generate by activation activate
        """
    
    @abstractmethod
    def getId (self):
        """ Returns neuron's id"""
        pass
    
    @abstractmethod
    def addInputSynapse (self, synapse):
        """ Add input synapse to the neuron
        Args:
            synapse: neuron's input synapse to be added
        """
    
    @abstractmethod
    def addOutputSynapse (self, synapse):
        """ Add output synapse to the neuron
        Args:
            synapse: neuron's output synapse to be added
        """
        
    @abstractmethod
    def countOutputSynapse (self):
        """ Count the neuron's output synapses
        Returns:
            The number of output synapses
        """
        
    @abstractmethod
    def weightedInputs (self):
        """Returns the weightedInputs from neuron's synapses"""
    
    @abstractmethod
    def setActivateFunction(self, activateFunction):
        """Set the neuron's activate activate"""
        
    @abstractmethod
    def setId (self, neuronIdentifier):
        """Set the neuron's id'"""
    
    @abstractmethod
    def getInputSynapses (self):
        """Returns the neuron's input synapses"""
        
    @abstractmethod
    def getOutputSynapses (self):
        """Returns the neuron's output synapses"""