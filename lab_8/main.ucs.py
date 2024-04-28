from eight_puzzle_problem import EightPuzzleProblem
from uniform_cost_search import UniformCostSearchStrategy
from modify_search import Search

# Example initial state
initial_state = [[1, 3, 4], [8, 6, 2], [7, 0, 5]]
# Example goal state
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Create an instance of the 8-puzzle problem
eight_puzzle_problem = EightPuzzleProblem(initial_state, goal_state)

# Create an instance of the Uniform Cost Search strategy
ucs_strategy = UniformCostSearchStrategy()

# Create a search object using UCS strategy
ucs_search = Search(eight_puzzle_problem, ucs_strategy)
# Solve the problem using UCS
ucs_result = ucs_search.solveProblem()
if ucs_result is not None:
    print("\nUniform Cost Search Result:")
    ucs_search.printResult(ucs_result)
else:
    print("Uniform Cost Search: No solution found.")

expanded_nodes = ucs_search.getExpandedNodes()
print("The number of expanded nodes:", expanded_nodes)