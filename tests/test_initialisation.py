# Created by Andy at 04-Jan-21

# Enter description here

# _____________________________
import pytest
from tabu_search import *
from hypothesis import given, strategies as st
from hypothesis import settings

# settings(max_examples=10)

@given(stm = st.integers(1,1000), mtm = st.integers(1,1000), intensify = st.integers(1,1000),
       diversify = st.integers(1,1000), reduce = st.integers(1,1000), stopping_stepsize = st.floats(0.01,30),
       stepsize = st.floats(0.01,1000), ndims = st.integers(1,6))
def test_initialises_with_valid_input(stm, reduce, stopping_stepsize, stepsize, ndims, diversify, mtm, intensify):
    solver = TabuSolver(obj_fun=rana, STM=stm, MTM= mtm, reduce=reduce, stopping_stepsize= stopping_stepsize,
                        diversify= diversify, intensify = intensify, stepsize= stepsize, n_dims= ndims)
    assert len(solver._current_location) == ndims
    assert len(solver._best_solutions_found) == 1
    assert len(solver._tabu) == 1
    assert len(solver._segment_counts) == 3**ndims




@pytest.mark.parametrize("stm, mtm, stepsize, ndims",[(-1,1,10,50),(1,-1,10,10),(2,2,100000,20),(2,2,10,50)])
def test_initialise_fails_with_invalid_input(stm,mtm, stepsize, ndims):
    '''The system will not be able to initialise if given invalid inputs'''
    with pytest.raises(ValueError):
        solver = TabuSolver(obj_fun=rana, STM=stm, MTM= mtm, stepsize= stepsize, n_dims= ndims)


@pytest.mark.parametrize("stm, mtm, stepsize, ndims",
                         [(11, 1, 10, "50"), (1, "1", 10, 10), ("2", 2, 10, 20), ([2], 2, 10, 10)])
def test_initialise_fails_with_wrong_type_input(stm, mtm, stepsize, ndims):
    '''The system will not be able to initialise if given invalid inputs'''
    with pytest.raises(TypeError):
        solver = TabuSolver(obj_fun=rana, STM=stm, MTM=mtm, stepsize=stepsize, n_dims=ndims)


