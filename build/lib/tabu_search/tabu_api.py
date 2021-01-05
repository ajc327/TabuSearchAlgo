# Created by Andy at 04-Jan-21

# Enter description here

# ___________________________________
from itertools import product 
from .tabu_validators import *
from .tabu_local_search import *
from .demo_functions import rana
from .tabu_tools import *
import numpy as np
from collections import deque, defaultdict
import heapq

from collections import namedtuple




class TabuSolver:

    STM  = Number(1,1200, True)
    MTM =  Number(1, 1000, True)
    intensify = Number(1, 1000, True)
    diversify = Number(1, 1000, True)
    reduce = Number(1,1000, True)
    stopping_stepsize = Number(0,30)
    stepsize = Number(0, 1000)
    n_dims = Number(1,30,True)
    def __init__(self, obj_fun = rana, STM = 7, MTM = 4, intensify = 10, diversify = 15, reduce = 25, stopping_stepsize = 4.0,
                 stepsize = 40, n_dims = 2):

        self.STM = STM
        self.MTM = MTM
        self.intensify = intensify
        self.diversify = diversify
        self.reduce = reduce
        self._counter = 0
        self.stopping_stepsize = stopping_stepsize
        self._reduction_factor = 0.7
        self.stepsize = stepsize
        self._best_solutions_found = []  # This is a heapq
        self._obj_fn = rana 
        self._tabu = deque(maxlen=self.STM)
        self._all_historical_points = []
        self.n_dims = n_dims
        self.LOWER = -500
        self.HIGHER = 500
        self._current_location = np.random.uniform(self.LOWER, self.HIGHER, self.n_dims)
        self._tabu.append(tuple(self._current_location))
        self._best_solutions_found.append((-self._obj_fn(self._current_location), tuple(self._current_location)))
        self._best = self._obj_fn(self._current_location)
        self._all_historical_points.append(tuple(self._current_location))
        self.flags =[2]
        self.c = 0
        self._segmentation = 3
        all_segments = product(range(1,self._segmentation+1), repeat= self.n_dims)
        self._segment_counts = {"".join(map(str,i)):0 for i in all_segments}
        self._segment_counts[convert_to_segment(self._current_location, self._segmentation, self.LOWER, self.HIGHER)] = 1




    def intensify_search_average(self):
        print("intensifying")
        self._current_location = 1./self.MTM*sum(np.array(i[1]) for i in self._best_solutions_found)
        self.record_point(self._current_location, flag = 3)

    def diversify_search(self):
        print(" Diversifying!!!!")
        least_visited_segment = min(self._segment_counts, key = self._segment_counts.get)
        self._current_location = gen_random_x_from_segment(least_visited_segment, self._segmentation, self.LOWER,
                                                           self.HIGHER)

        self.record_point(self._current_location, flag = 4)

    def reduce_step_size(self):
        print("reducing step size !!!!")
        self.stepsize *= self._reduction_factor
        self._counter = 0




    def step(self):
        '''Takes a step and do all the side effects'''
        try:
            dx, improving = full_local_search(self._current_location, self._obj_fn, self.stepsize, self._tabu,
                                              self.LOWER, self.HIGHER)
        except ValueError:
            self.diversify_search()
            return
        self._current_location += dx
        new_feval = self._obj_fn(self._current_location)
        self.record_point(self._current_location)

        if improving:
            pattern_location = self._current_location + dx
            improved_again = True if self._obj_fn(pattern_location) < new_feval\
                                     and all(self.LOWER< j < self.HIGHER for j in pattern_location) else False

            if improved_again:
                self._current_location += dx
                self.record_point(self._current_location)
                self.flags[-2]= 0


    def record_point(self, point, flag = 1 ):
        ''' This is to visit a point. This involves adding it to the list of all visited,
        adding it to the tabu list, and adding it to the medium term mem if it is good,
        also reset the counter if good. Also update the long_term_memory.'''
        self._all_historical_points.append(tuple(point))
        encoded_point = convert_to_segment(point, self._segmentation, self.LOWER, self.HIGHER)
        self._segment_counts[encoded_point] += 1
        self.flags.append(flag)
        self.c += 1
        self._tabu.append(tuple(point))
        neg_feval = -self._obj_fn(point)
        if neg_feval > self._best_solutions_found[0][0]:
            heapq.heappushpop(self._best_solutions_found,(neg_feval, tuple(point)))
        elif len(self._best_solutions_found) <self.MTM:
            heapq.heappush(self._best_solutions_found,(neg_feval, tuple(point)))

        if -neg_feval < self._best:
            self._best = -neg_feval
            self._counter = 0
        else:
            self._counter+=1




    def __repr__(self):
        return(f"I am currently at {self._current_location}, the short term memory is {self._tabu}, "
              f"The medium term memory is {self._best_solutions_found}")

    def run(self):
        # Initialise the starting position
        while self.stepsize > self.stopping_stepsize:
        #for i in range(200):
            # do a step search
            self.step()
            if self._counter >= self.reduce:
                self.reduce_step_size()
                continue

            elif self._counter == self.diversify:
                self.diversify_search()
                continue

            elif self._counter == self.intensify:
                self.intensify_search_average()



        print(self.stepsize)
        print(self._segment_counts.values())
        # Results are stored in M
        return self._all_historical_points, self._best_solutions_found



if __name__ == "__main__":

    solver = TabuSolver(n_dims=5, reduce=45)

    points, best = solver.run()
    flags = solver.flags
    print(best)

    #visualise_population_location(points, 500,-500,flags)
