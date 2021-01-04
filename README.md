# Tabu Search


This is an optimisation method designed to help a search negotiate difficult regions by imposing restrictions. 

The power of TS derives from its use of flexible memory cycles. 

These memory cycles control the local search pattern and intensity and diversify the search in the quest for a suitable solution. 

### Local Search 

1. Choose a starting point randomly. Evaluate the objective function f(x). Choose a suitably sized increment for each control variable x1, x2, ... xn. 

2. Record the current point as a base point. 

3. For each vairable in turn, 
  * Increase it by its increment, while keeping the other variabels at their base point values, and evaluate f(x)
  * Decrease it by its increment, while keeping th ohter variables at their base point values. 

4. Make the best allowed(non-tabu) move 

5. If the objective function evaluation was reduced by the move, perform a pattern move by repeating the vector from the last base point. If this reduces agian, accpet it. Otherwise, discard it. 

6. Record the current point as the new base point. Return to step 3. 

### Short term memory 
* Whether a move is allowed or not is determind by the short term memory. 
* This records the last N locations successfully visited. 
* The list is updated every time a new location is successfully visited (first in, first out)
* Locations within the STP are tabu, so they are not allowed to be visited again. 
* The requirement that the best allowed move be made means that often the move results in an objective function increase. 

* The effect of the STM is that the algorithm behaves like a normal hill-descending algorithm until it reaches a minimum. It is then forced to climb out of the hollow and explore further. 

### Search intensification 
* This is the process associated witht eh Medium Term Memory. 
* The MTM records the best M solutions located thus far, i.e the M solutions with the lowest objective function values. 
* If there has been no improvement in the best solution found for a specified number of local search iterations, then the search is intensified. This entails moving the current search location xk+1 to an average best position. This entails moving the current search location to an average best position. 
* SI is performed in order to focus the search in the neighbourhood of the best solutiosn found without visiting any of them again. 

### Search diversification 
* If SI does not succeed in finding an improved best solution, then the search is diversified. 
* Search Diversification is associated with the Long Term Memory (LTM)
* The LTM records the areas fothe search space which ahve been searched resonably throughly. 
* The LTM can be implemented by, for instance, dividing the search space into sectors and tallying the number of locations successfully visited in each sector. 
* When search diversification takes place the current search location is moved to a randomly selected part of the search space which has not been thoroughly explored. 
* SD is performed in order to investigate previously unexplored parts of the search space, if no further progress is being made in areas already well explored.

### Step size reduction 
* After prolonged lack of success despite SI and SD, then step size reduction takes place 
* In SST The step sizes associated with each control variable are reduced, the search is returned to the location of the best solution found thus far, and the counter controlling SI, SD and SSR is reset. 
* SSR is carreid out in order to ensure that the neighbourhood of the best solution is searched carefully. 

### Convergence 
* The convergence can be defined as a threshold, ie after certain numbers of search diversification iterations. 
* Another criterion is that despite of SI, SD and SSR, the same best location is repeatedly being found. 

### Search control 
* Counter = 0 
* test convergence 
* If converged, stop and if not, we could like to perform a local search iteration. 
* If a new best solution has been found, go to step 1, if not, increment counter 
* If counter == Intensify, intensify search 
* If counter == Diversify, diversify search 
* If counter == Reduce, reduce step size and go to step 1 
* go to step 2 

### Recommended parameters 
  * N = 7 
  * M = 4 
  * Intensify = 10 
  * Diversify = 15 
  * Reduce = 25 


### Local search variants. 
These can come in very many different flavours. 

#### Random subset search 
At each iteration a random subset of the possibel non-tabu moves are evaluated and the best allowed amongst these is made. 

#### Successive Random Subset Search 
  * At each iteration a random subset of the possible non-tabu moves are evaluated. 
  * If any of these moves improves on th current solution, the best allowed move is made. 
  * If not, another subset of the possible non-tabu moves are evaluated. 
  * This continues until an improving move is found or all moves have been evaluated. 
  * If no imporoving, non-tabu move is found, the best allowed move is made. 

#### Variable prioritisation search 
  * Here an attempt is made to identify which control variables have the breatest influence on the objective function and then these are prioritised in the local search. 
  * The steps are as follows: 
    - Conduct an exhaustive search around the current point. 
    - Calculate the sensitivity of f to each control variable. 
    - Rank the control variables accroding to sensitivity. 
    - Select the n.2 highest ranked variables to be free variables and fix the values of the others. 
    - Continue the search usign the reduced set of variables for a defined number of iterations then do this again. 

    
=======================================

## Code use example 

```python3
from tabu_search import TabuSolver
solver = TabuSolver()
all_points, best_points = solver.run()
```

















