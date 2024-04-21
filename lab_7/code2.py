import random
import operator
import math
from deap import base, creator, tools, gp

# Define the primitive set
pset = gp.PrimitiveSet("MAIN", arity=1)
pset.addPrimitive(operator.add, arity=2)
pset.addPrimitive(operator.sub, arity=2)
pset.addPrimitive(operator.mul, arity=2)
pset.addPrimitive(operator.neg, arity=1)
pset.addPrimitive(math.sin, arity=1)
pset.addPrimitive(math.cos, arity=1)
pset.addPrimitive(math.exp, arity=1)

def eval_function(individual):
    # Compile the individual into a Python function
    func = toolbox.compile(expr=individual)
    # Evaluate the compiled function
    try:
        x = 1  # Input value for the equation
        y = func(x)
        # Calculate RMSE (Root Mean Square Error) fitness
        fitness = math.sqrt((y - (5*x**3 - 6*x**2 + 8*x - 1))**2)
    except (OverflowError, ValueError, ZeroDivisionError):
        fitness = float('inf')  # Assign infinite fitness for invalid expressions
    return (fitness,)


# Create the toolbox
def create_toolbox():
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=3)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)
    toolbox.register("evaluate", eval_function)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
    
    return toolbox

if __name__ == "__main__":
    toolbox = create_toolbox()
    random.seed(7)
    population = toolbox.population(n=500)
    probab_crossing = 0.5
    probab_mutating = 0.2
    num_generations = 10
    print('\nEvolution process starts')

   # Evaluate the initial population
fitnesses = list(map(toolbox.evaluate, population))
for ind, fit in zip(population, fitnesses):
    ind.fitness.values = fit
print('\nEvaluated', len(population), 'individuals')

# Evolution process
for g in range(num_generations):
    print("\nGeneration", g)

    # Select the next generation individuals
    offspring = toolbox.select(population, len(population))
    offspring = list(map(toolbox.clone, offspring))

    # Apply crossover and mutation
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < probab_crossing:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < probab_mutating:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluate individuals with invalid fitness values
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    for ind in invalid_ind:
        ind.fitness.values = toolbox.evaluate(ind)
    print('Evaluated', len(invalid_ind), 'individuals')

    # Replace old population with offspring
    population[:] = offspring

    # Calculate statistics
    fits = [ind.fitness.values[0] for ind in population]
    length = len(population)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean**2)**0.5

    print('Min:', min(fits), 'Max:', max(fits))
    print('Average:', round(mean, 2), 'Standard deviation:', round(std, 2))

print("\nEvolution ends")
