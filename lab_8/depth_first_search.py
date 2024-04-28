from search_strategy import SearchStrategy  # Import the base class

class DepthFirstSearchStrategy(SearchStrategy):
    def __init__(self):
        # Initialize the stack
        self.stack = []

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def addNode(self, node):
        # Add a node to the stack
        self.stack.append(node)

    def removeNode(self):
        # Remove and return a node from the stack
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None
