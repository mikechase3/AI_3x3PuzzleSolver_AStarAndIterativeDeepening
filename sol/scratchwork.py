# Original work; replaced/refined by AI solutions.

# For use in PathNode class.
def OLDswapPositions(self, firstIndexPos, secondIndexPos) -> "PathNode":  # How is this type hint valid?
    """
    Swap positions in state & return a new pathnode with those indexes swapped.
    :param firstIndexPos: for swapping...
    :param secondIndexPos:
    :return a new node
    """
    new_state = self.state.copy()
    new_state[firstIndexPos], new_state[secondIndexPos] = self.state[secondIndexPos], self.state[firstIndexPos]

    # Create a new PathNode with the modified state
    new_node = PathNode(new_state, self.treeDepth + 1, parent=self, lastPosSwap=secondIndexPos)
    return new_node

def h_cost_v1(self):
    '''
    My attempt to manually calculate the cost of a state.
    :return:
    '''
    wrongSpots: int = 0
    for number in self.state:
        if number != self.state.index(number):
            wrongSpots += 1
    return wrongSpots

def aStarRecursive(pn: PathNode, depth: int, maxDepth: int, visitedNodes: List[str] = None,
                   hq: heapq = None) -> List[PathNode]:
    # BASE CASES
    if visitedNodes == None:
        visitedNodes = []
    if hq == None:
        hq = []
    if pn.state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return [pn]
    if depth >= maxDepth:
        return []

    # RECURSIVE CASE
    visitedNodes.append(pn.getStateStr())
    children = pn.generate_children()
    for child in children:
        burden: int = child.f_cost()
        # burden: int = calculateHeuristicHammingMethod(child)  # Est. cost to reach goal from this node
        hq.append((burden, child))
        # heapq.heapify(hq)
        aStarRecursive(child, depth + 1, maxDepth, visitedNodes, hq)

        # if child.getStateStr() not in visitedNodes:
        #     visitedNodes.append(child.getStateStr())
        #     result = aStarRecursive(child, visitedNodes, )
        #     if result:
        #         return [pn] + result
    return []