import numpy as np

def linear_regression_activation(z):
    '''
    Linear Regression activation function
    
    Parameters:
    -----------
    z : float --> input to activation function
    
    Returns:
    --------
    float: same as input
    '''
    
    return z

def sigmoid_activation(z):
    '''
    Sigmoid activation function
    '''
    return 1.0/(1.0 + np.exp(-z))