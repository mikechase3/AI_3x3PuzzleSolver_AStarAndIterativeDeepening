from typing import List


class PathNode():
    # INSTANCE VARIABLES
    treeDepth: int
    state: List[int]

    def __init__(self, treeDepth: int, state: List[int],):
        self.treeDepth = treeDepth
        self.state = state

    def __str__(self):
        return "TreeDepth: {} | State{}".format(self.treeDepth, str(self.state))

def swapPositions(PathNode, firstIndexPos, secondIndexPos):
    raise NotImplementedError("swapPositions not implemented yet.")