from typing import List, Optional


class PathNode():

    def __init__(self, state: List[int], treeDepth: int = 0, parent=None, lastPosSwap: Optional[int] = None):
        """Initialize a node for the search tree"""
        self.treeDepth = treeDepth
        self.state: List[int] = state
        self.lastPosSwap: int = lastPosSwap if lastPosSwap is not None else -69  # Do I need this?

    def __repr__(self):
        return f"PathNode(state={self.state}, treeDepth={self.treeDepth}, lastPosSwap={self.lastPosSwap})"

    # def swapPositions(self, firstIndexPos, secondIndexPos) -> "PathNode":  # Is this type hint valid?
    #     """
    #     Swap positions in state & return a new pathnode with those indexes swapped.
    #     :param firstIndexPos: for swapping...
    #     :param secondIndexPos:
    #     :return a new noew node
    #     """
    #     new_state = self.state.copy()
    #     new_state[firstIndexPos], new_state[secondIndexPos] = self.state[secondIndexPos], self.state[firstIndexPos]
    #
    #     # Create a new PathNode with the modified state
    #     new_node = PathNode(new_state, self.treeDepth + 1, parent=self, lastPosSwap=secondIndexPos)
    #     return new_node



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
        Uses 8-puzzle theory: https://medium.com/@dpthegrey/8-puzzle-problem-2ec7d832b6db
        :return: A list of PathNode objects representing the children.
        """
        children = []

        # Find the position of the empty space (assuming 8 represents the empty space)
        empty_index = self.state.index(8)

        # Define the moves for the empty space as up, down, left, and right
        # [0, 1, 2,
        #  3, 4, 5,
        #  6, 7, 8]
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
            child_node = PathNode(state=new_state, treeDepth=self.treeDepth + 1, parent=self)
            children.append(child_node)

        return children