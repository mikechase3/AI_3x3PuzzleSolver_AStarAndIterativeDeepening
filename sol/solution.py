# This is the only file you need to work on. You do NOT need to modify other files
import heapq
from typing import List

from sol.PathNode import PathNode


# Below are the functions you need to implement. For the first project, you only need to finish implementing iddfs()
# ie iterative deepening depth first search


def recursiveIterativeDeepening(node: PathNode, goalState: List[int], depth: int, maxDepth: int = 10,
                                visitedNodes: List[int] = None) -> List[PathNode]:
    """
    Not sure yet - but we'll call itself until we find a solution!
    :param node: represents information about a node in a map
    :param goalState: obvious.
    :param maxDepth: maximum allowed tree depth
    :return: The path from the initial state to the goal state as a list of PathNode objects,
             or an empty list if no solution is found within the given depth. This will be a
             sequence of PathNode objects, each representing a state in the solution path.
    """
    if visitedNodes is None:
        visitedNodes = []
    # BASE CASES
    if node.state == goalState:
        return [node]
    if depth >= maxDepth:
        return []

    # RECURSIVE CASE
    currentNodeStateAsStr = node.getStateStr()

    if currentNodeStateAsStr not in visitedNodes:
        visitedNodes.append(node.getStateStr())
        visitedNodes.append(currentNodeStateAsStr)  # Mark node as visited.
        children = node.generate_children()
        for child in children:
            result = recursiveIterativeDeepening(child, goalState, depth + 1, maxDepth, visitedNodes)
            if result:
                return [node] + result

    return []  # No solutions found from this node.


def iterativeDeepening(puzzle: List[int], maxDepth=10) -> List[int]:
    print("DEBUG Trace solution.iterativeDeepening: Input Puzzle: {}".format(puzzle))
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    root = PathNode(state=puzzle, treeDepth=0, parent=None)

    for depth in range(maxDepth + 1):
        solution_nodes = recursiveIterativeDeepening(root, goal_state, depth, maxDepth)
        solution_path: List[int] = []  # stores solution as integers for assignment output.

        if solution_nodes:
            for n in solution_nodes:
                solution_path.append(n.lastPosSwap)
            # Extract the states from the nodes in the solution path if required, or
            # change the PathNode class to store the necessary information that needs
            # to be returned, then format them in the way expected by the problem statement
            return solution_path[1:]

    raise Exception("No solutions exist up to depth {}.".format(maxDepth))









# Modify the reconstruct_path function to return the sequence of moves
def reconstruct_path(end_node: PathNode) -> List[int]:
    moves = []
    current = end_node
    while current.parent:  # Continue until the root node (which has no parent)
        moves.append(current.lastPosSwap)
        current = current.parent
    return moves[::-1]  # Reverse the list to get moves in the correct order


def astar(puzzle: List[int]) -> List[int]:
    initial_state_pn = PathNode(puzzle)
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    max_depth = 10

    pq = [(0, initial_state_pn)]  # Priority queue
    heapq.heapify(pq)

    while pq:
        burden, pn = heapq.heappop(pq)
        # Update the return statement when goal is found in 'astar' function
        if pn.state == goal_state:
            return reconstruct_path(pn)

        if pn.treeDepth < max_depth:
            children = pn.generate_children()
            for child in children:
                cost = child.f_cost()
                heapq.heappush(pq, (child.f_cost(), child))
    return []  # No solution found

if __name__ == "__main__":
    initial_state = [0, 1, 2, 3, 4, 5, 6, 8, 7]  # create your initial PathNode instance
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # define your goal state
    sol = astar(initial_state)
    for i in sol:
        print(i)