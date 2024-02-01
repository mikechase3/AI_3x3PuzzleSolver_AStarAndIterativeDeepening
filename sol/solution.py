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


def calculateHeuristicHammingMethod(pn: PathNode) -> int:
    wrongSpots: int = 0
    for number in pn.state:
        if number != pn.state.index(number):
            wrongSpots += 1
    return wrongSpots

def calculate_manhattan_heuristic(node: PathNode) -> int:
    manhattan_distance = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Assuming '0' represents the empty tile

    for index, value in enumerate(node.state):
        if value == 8:  # Skip the empty tile
            continue
        current_row, current_col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_state.index(value), 3)
        manhattan_distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return manhattan_distance



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
        burden: int = calculateHeuristicHammingMethod(child)  # Est. cost to reach goal from this node
        hq.append((burden, child))


        # if child.getStateStr() not in visitedNodes:
        #     visitedNodes.append(child.getStateStr())
        #     result = aStarRecursive(child, visitedNodes, )
        #     if result:
        #         return [pn] + result
    return []


def astar(puzzle: List[int]) -> List[int]:
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    rootNode = PathNode(puzzle)

    print(puzzle)
    path = []
    return path


if __name__ == "__main__":
    initial_state = [0, 1, 2, 3, 8, 5, 6, 4, 7]  # create your initial PathNode instance
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # define your goal state
    initial_PathNode_state = PathNode(initial_state, 0)
    pn = PathNode(initial_state, 0)
    print(calculateHeuristicHammingMethod(pn))
