'''
Created on 9 de jun de 2019

@author: zeller
'''

import math

from activate.ActivateFunction import ActivateFunction


class SigmoidFunction(ActivateFunction):
    '''
    Represents sigmoid activate function
    '''

    def calculate(self, input_value):
        return 1.0 / (1.0 + math.exp(-input_value))
        