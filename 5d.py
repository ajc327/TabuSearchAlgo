# Created by Andy at 17-Jan-21

# Enter description here

# ___________________________________
from tabu_search import *

default_list = []
proposed_list = []

for i in range(20):
    default_solver = TabuSolver(n_dims=5, reduce=25, MTM=4,reduction_factor=0.7)
    proposed_solver = TabuSolver(n_dims=5, reduce=60, MTM=4,reduction_factor=0.9 )
    _, d_best = default_solver.run()
    _, p_best = proposed_solver.run()
    default_list.append(sorted(d_best, key = lambda x: x[0])[0])
    proposed_list.append(sorted(p_best, key = lambda x: x[0])[0])



default_list = sorted(default_list, key = lambda x: x[0])
proposed_list = sorted(proposed_list, key = lambda x: x[0])


print(f"The average for default params is {np.mean([-sol[0] for sol in default_list])}")
print(f"The best found for default params is {-default_list[-1][0]}")
print(f"this is at {default_list[-1][1]} \n \n")


print(f"The average for proposed params is {np.mean([-sol[0] for sol in proposed_list])}")
print(f"The best found for proposed params is {-proposed_list[-1][0]} ")
print(f"this is at {proposed_list[-1][1]}")
