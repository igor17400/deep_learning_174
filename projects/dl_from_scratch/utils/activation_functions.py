from typing import ndarray
import numpy as np

def square(x: ndarray) -> ndarray:
    '''
    Square each element in the input ndarray
    '''
    return np.power(x, 2)

def leaky_rely(x: ndarray) -> ndarray:
    '''
    Apply "Leaky ReLU" function to each element in ndarray.
    '''
    return np.maximum(0.2*x, x)

def sigmoid(x: ndarray) -> ndarray:
    '''
    Apply the sigmoid function to each element in the input ndarray
    '''
    return 1 / (1 + np.exp(-x))
