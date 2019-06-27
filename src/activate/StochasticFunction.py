'''
Created on 9 de jun de 2019

@author: zeller
'''

from activate import ActivateFunction

class Stochastic(ActivateFunction):
    '''
    Represents stochastic activate function
    '''
    
    def calculate(self, input_value):
        return 1 if input_value >= 0 else 0
    
    
        