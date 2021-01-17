# Created by Andy at 17-Jan-21

# Enter description here

# ___________________________________

from tabu_search import *

def visualise_population_location(parents, upper=500, lower=-500, flags = None, best = None):
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
    legend = ["Pattern move", "Visited location","Starting point", "Intensification", "Diversification" ]
    seen = ["red","blue","black","green","pink"]
    for indx, (parent, flag) in enumerate(zip(parents, flags)):
        colors =["red","blue","black","green","pink"]
        if colors[flag] in seen:
            ax.scatter(parent[0], parent[1], c= colors[flag], alpha= indx*(0.7/my_len)+0.3, label = legend[flag])
            seen.remove(colors[flag])
        else:
            ax.scatter(parent[0], parent[1], c= colors[flag], alpha= indx*(0.7/my_len)+0.3)
    ax.scatter(best[1][0], best[1][1], c = "cyan", s = 100, marker ="x", linewidth=5, label = "Best solution")
    ax.legend()
    ax.title.set_text(f"Minimum found: {-best[0]:.2f}")
    plt.savefig(r"..\ts4.png")
    plt.show()

np.random.seed(1)
solver = TabuSolver(n_dims=2, reduce=60, MTM=4,reduction_factor=0.9)

points, best = solver.run()
flags = solver.flags
best = sorted(best, key = lambda x: x[0])[-1]
print(best)

visualise_population_location(points, 500,-500,flags, best)