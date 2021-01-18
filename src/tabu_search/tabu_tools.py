# Created by Andy at 04-Jan-21

# Contains some of the useful tools used in the main solver

# ___________________________________

import matplotlib.pyplot as plt
from .demo_functions import *
import numpy as np
import bisect

def visualise_population_location(parents, upper=500, lower=-500, flags = None):
    # This function shows the plot for
    assert len(parents[0]) ==2

    x = np.linspace(lower,upper,300)
    y = np.linspace(lower,upper,300)
    xy = np.meshgrid(x,y)
    X, Y = np.meshgrid(x,y)
    result = rana(xy)
    fig, ax = plt.subplots(1,1, figsize=(10,10))
    surf = ax.contourf(X,Y,result, levels = 50, cmap = "RdBu_r")
    fig.colorbar(surf, ax = ax)
    my_len = len(parents)
    for indx, (parent, flag) in enumerate(zip(parents, flags)):
        colors =["red","blue","black","green","pink"]
        ax.scatter(parent[0], parent[1], c= colors[flag], alpha= indx*(0.7/my_len)+0.3)

    plt.show()




def convert_to_segment(x, n_segments, lower, upper):
    '''Function for encoding the n dimensional input vector in to a string of length n. '''
    segment_list = np.linspace(lower, upper, n_segments+1)
    output_string = ''
    for xi in x:
        # Bisect finds the rank of the value in a list efficiently
        output_string += str(bisect.bisect(segment_list, xi))
    return output_string


def gen_random_x_from_segment(encoded_string, n_segments, lower, upper):
    ''' Used when diversifying search. Takes a segment encoding and generates a random input point within
    the search space represented by the segment encoding'''
    x_out = []
    segment_list = np.linspace(lower, upper, n_segments+1)
    for si in encoded_string:
        index = int(si)
        # Find the bounds on the dimension represented by the encoded character.
        low = segment_list[index-1]
        high = segment_list[index]
        x_out.append(np.random.uniform(low, high))
    return np.array(x_out)



if __name__ == "__main__":
    print(convert_to_segment([400,-300], 3, -500,500))
    print(gen_random_x_from_segment("32", 3, -500,500))