'''
Created on 9 de jun de 2019

@author: zeller
'''

from abc import ABC, abstractmethod

class ActivateFunction (ABC):
    """
    Represents a default activate function
    """
    
    @abstractmethod
    def calculate (self, input_value):
        """
        Calculate function
        """
        