from typing import List, Optional


class PathNode():

    def __init__(self, state: List[int], treeDepth: int = 0, parent=None, lastPosSwap: Optional[int] = None):
        """Initialize a node for the search tree"""
        self.treeDepth = treeDepth
        self.state: List[int] = state
        self.lastPosSwap: int = lastPosSwap if lastPosSwap is not None else -69  # Do I need this?

    def __repr__(self):
        return f"PathNode(state={self.state}, treeDepth={self.treeDepth}, lastPosSwap={self.lastPosSwap})"

    def swapPositions(self, firstIndexPos, secondIndexPos) -> "PathNode":  # Is this type hint valid?
        """
        Swap positions in state & return a new pathnode with those indexes swapped.
        :param firstIndexPos: for swapping...
        :param secondIndexPos:
        :return a new noew node
        """
        new_state = self.state.copy()
        new_state[firstIndexPos], new_state[secondIndexPos] = self.state[secondIndexPos], self.state[firstIndexPos]

        # Create a new PathNode with the modified state
        new_node = PathNode(new_state, self.treeDepth + 1, parent=self, lastPosSwap=secondIndexPos)
        return new_node

