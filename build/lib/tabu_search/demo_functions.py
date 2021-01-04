# Created by Andy at 04-Jan-21

# Enter description here

# ___________________________________
import numpy as np

def rana(x):
    ''' computes the n dimensional rana function'''
    if isinstance(x[0], (list, tuple)):
        return [rana(i) for i in x]
    else:
        return sum(x[i]*np.cos(np.sqrt(abs(x[i+1] + x[i] +1)))*np.sin(np.sqrt(abs(x[i+1] - x[1] +1)))
                   +(1+x[i+1])*np.cos(np.sqrt(abs(x[i+1] - x[i] +1)))*np.sin(np.sqrt(abs(x[i+1] + x[i] + 1)))
                   for i in range(0,len(x)-1))
