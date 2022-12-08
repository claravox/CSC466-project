import numpy as np

def distance(x,c):
    # this is correct
    d = np.sqrt(np.sum((x-c)**2))
    return d