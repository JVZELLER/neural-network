'''
Created on 9 de jun de 2019

@author: zeller
'''

class Synapse(object):
    '''
    Represents synpse between two neurons
    '''


    def __init__(self, previous_neuron, weight, next_neuron):
        self.previous_neuron = previous_neuron
        self.weight = weight
        self.next_neuron = next_neuron
        
    def get_previous_neuron (self):
        return self.previous_neuron
    
    def get_next_neuron (self):
        self.next_neuron
    
    def get_weight (self):
        return self.weight
    
    def set_weight (self, weight):
        self.weight = weight
        
        