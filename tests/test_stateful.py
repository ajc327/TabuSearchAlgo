# Created by Andy at 05-Jan-21

# Enter description here

# ___________________________________
import time
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant
import pytest
from tabu_search import *


class TestStatefulBehaviour(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.solver = TabuSolver()


    @rule()
    def test_step(self):
        len_original_outputs = len(self.solver._all_historical_points)
        self.solver.step()
        assert len(self.solver._all_historical_points) == len_original_outputs +1 or \
               len(self.solver._all_historical_points) == len_original_outputs +2

    @invariant()
    def test_short_term_memory_invariant(self):
        assert len(self.solver._tabu) <= self.solver.STM
        assert len(self.solver._best_solutions_found) <= self.solver.MTM


testcase = TestStatefulBehaviour.TestCase




@pytest.fixture(autouse= True)
def timer():
    start = time.time()
    yield
    finish = time.time()
    dx = finish - start
    print(f"\n The function took {dx:.3f} seconds to run")
