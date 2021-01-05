# Created by Andy at 05-Jan-21

# Enter description here

# ___________________________________
import time
import pytest
from hypothesis import strategies as st, given
import mock
from tabu_search import *


def test_full_local_search_tabus_out(default):
    '''The local search should return valueerror at boundary if all feasible points are in tabu
    This is when it cannot move anywhere.'''
    # THE local search should fail with VALUE ERROR

    # GIVEN some function which returns a valid input 
    def mockfun(x):
        return 2
    
    with pytest.raises(ValueError):
        # WHEN the only tabu move is to move out of the boundary 
        maybe_new_point = full_local_search(np.array([0,0]), mockfun, 2, [(0,2),(2,0),(0,0)],-1,100)
    
    with pytest.raises(ValueError):
        maybe_new_point = full_local_search(np.array([0,0]), mockfun, 2, [(0,2),(2,0),(0,0),(-2,0),(0,-2)],-10,100)

def test_full_local_search_works():
    maybe_new_point = full_local_search(np.array([0, 0]), rana, 10, [(0,0)], -500,
                                        500)


@given(lst= st.lists(st.integers(-480,480),1,10))
def test_full_local_search_gives_best_solution(lst):
    '''If no tabu present, it should return the best solution'''
    lst = np.array(lst)
    dx, reduced = full_local_search(lst, rana, 10, [tuple(lst)],-500,500)
    new_point = lst + dx
    for i in range(len(lst)):
        for j in [1,-1]:
            option = np.array(lst)
            option[i] += j*10
            assert rana(option) >= rana(new_point)









@pytest.fixture(name = "default")
def default_solver():
    solver = TabuSolver()
    yield solver
    del solver

@pytest.fixture(autouse= True)
def timer():
    start = time.time()
    yield
    finish = time.time()
    dx = finish - start
    print(f"\n The function took {dx:.3f} seconds to run.")
