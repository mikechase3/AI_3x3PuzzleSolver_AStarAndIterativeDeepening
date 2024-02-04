from typing import List, Optional


class PathNode():
    """
    Reprsents a node in the tree/graph of possible solutions.
    """
    treeDepth: int
    state: List[int]
    lastPosSwap: int

    def __init__(self, state: List[int], treeDepth: int = 0, parent=None, lastPosSwap: Optional[int] = None):
        """Initialize a node for the search tree"""
        self.treeDepth = treeDepth
        self.state: List[int] = state
        self.lastPosSwap: int = lastPosSwap if lastPosSwap is not None else -1  # Do I need this?
        self.parent = parent

    def __repr__(self):
        return f"PathNode(state={self.state}, treeDepth={self.treeDepth}, lastPosSwap={self.lastPosSwap})"

    def getStateStr(self):
        return str(self.state)

    def calculate_hamming_distance(self) -> int:
        """
        Calculate the Hamming distance between the current state and the goal state.
        The Hamming distance is the number of tiles in the wrong position.
        :return: The Hamming distance
        """
        goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        return sum(s != g and s != 8 for s, g in zip(self.state, goal_state))

    def f_cost(self):  # f(n) = g(n) + h(n)
        """
        Calculate the f(n) cost of the node.
        :return:
        """
        return self.treeDepth + self.calculate_hamming_distance()

    def swapPositions(self, lst, pos1, pos2):
        """
        Swap positions of two elements in a list.

        :param lst: The list to swap elements in.
        :param pos1: Index of the first element.
        :param pos2: Index of the second element.
        :return: A new list with the elements at pos1 and pos2 swapped.
        """
        lst_copy = lst[:]
        lst_copy[pos1], lst_copy[pos2] = lst_copy[pos2], lst_copy[pos1]
        return lst_copy

    def generate_children(self):
        """
        Generate all valid child nodes from the current state.
        AI Generated; not my own work.
        :return: A list of PathNode objects representing the children.
        """
        children = []
        empty_index = self.state.index(8)  # Finds the '8' position where 8 is the 'empty' space.
        move_offsets = [-3, 3, -1, 1]  # Corresponding to up, down, left, and right in a 3x3 grid

        # Loop through all possible moves
        for move in move_offsets:
            new_index = empty_index + move

            # Skip out-of-bound moves
            if new_index < 0 or new_index >= len(self.state):
                continue

            # Skip invalid left/right moves that cross the grid boundaries
            if (empty_index % 3 == 0 and move == -1) or (empty_index % 3 == 2 and move == 1):
                continue

            # Create a new state by swapping the empty space with the adjacent tile
            new_state = self.swapPositions(self.state, empty_index, new_index)

            # Create a new child node with the new state and incremented depth
            child_node = PathNode(state=new_state, treeDepth=self.treeDepth + 1, parent=self, lastPosSwap=new_index)
            children.append(child_node)

        return children

    def __lt__(self, other):
        # Primary comparison by f-cost
        if self.f_cost() != other.f_cost():
            return self.f_cost() < other.f_cost()
        # Secondary comparison can be based on any other consistent and distinct attribute
        return self.treeDepth < other.treeDepth

