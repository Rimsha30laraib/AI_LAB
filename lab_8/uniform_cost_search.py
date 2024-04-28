from queue import PriorityQueue
from search_strategy import SearchStrategy

class UniformCostSearchStrategy(SearchStrategy):
    def __init__(self):
        self.priority_queue = PriorityQueue()

    def isEmpty(self):
        return self.priority_queue.empty()

    def addNode(self, node):
        priority = node.cost  # Priority based on the cost of the node
        self.priority_queue.put((priority, id(node), node))  # Using id(node) for comparison

    def removeNode(self):
        _, _, node = self.priority_queue.get()
        return node