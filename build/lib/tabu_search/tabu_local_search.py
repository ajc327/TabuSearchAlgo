# Created by Andy at 04-Jan-21

# Enter description here

# ___________________________________
import numpy as np

def full_local_search(x, fun, stepsize, tabu, lower, higher):
    '''This conducts a full local search from the current x location.
    Returns the best non-tabu step to take.'''
    f_eval = fun(x)
    n_dims = len(x)
    evals = []
    for i, xi in enumerate(x):
        dx = np.zeros(n_dims)
        for j in (1,-1):
            dx[i] = stepsize*j
            x_new = dx + x
            if all(lower< k < higher for k in x_new):
                evals.append((list(dx), fun(x_new)))
    sorted_evals = sorted(evals, key = lambda x: x[1])
    for val in sorted_evals:
        if tuple(x+val[0]) not in tabu:
            return val[0], val[1] > f_eval

    raise ValueError("All feasible points in tabu! ")



if __name__ == "__main__":
    def dum(x):
        return 3
    full_local_search([0,0,0], dum, 1, [], -100,100)