# Import necessary classes
from eight_puzzle_problem import EightPuzzleProblem
from breadth_first_search import BreadthFirstSearchStrategy
from modify_search import Search

# Create an instance of the 8-puzzle problem
initial_state = [[1, 3, 4],[8, 6, 2],[7, 0, 5]]
  # Example initial state
goal_state = [[1, 2, 3],[8, 0, 4], [7, 6, 5]]
  # Example goal state

eight_puzzle_problem = EightPuzzleProblem(initial_state, goal_state)

# Create an instance of the breadth-first search strategy
breadth_first_search_strategy = BreadthFirstSearchStrategy()

# Create a search object
search = Search(eight_puzzle_problem, breadth_first_search_strategy)

# Solve the problem
result = search.solveProblem()

# Print the result
search.printResult(result)

# Get the number of expanded nodes
expanded_nodes = search.getExpandedNodes()
print("Number of expanded nodes:", expanded_nodes)
