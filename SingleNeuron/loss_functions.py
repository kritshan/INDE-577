import numpy as np

def cross_entropy_loss(y_hat, y):
    return - y*np.log(y_hat) - (1 - y)*np.log(1 - y_hat)

def mean_sqaured_error(y_hat, y):
    return .5*(y_hat - y)**2

def sign(z):
    return np.sign(z)