# This is the only file you need to work on. You do NOT need to modify other files
from typing import List

from sol.PathNode import PathNode

'''
REQUIREMENTS
(1) Your code is free of compilation error or runtime errors (10%)
(2) For the iterative deepening search, your code can iteratively increase depth limit and
perform DFS correctly (10%)
(3) Successfully return an optimal path by iterative deepening search (10%)
(4) Correctly define Heuristic function h() for A-star search (10%)
(5) Correctly compute the total cost f(S) = g(S) + h(S) for each move (10%)
(6) A-star search correctly expand states in the right order (15%)
(7) A-star search correctly get an optimal path (25%)
(8) Provide a short document describing what you have achieved and limits, with some
snapshots (10%)

REFERENCES USED
(1) https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/

'''


# Below are the functions you need to implement. For the first project, you only need to finish implementing iddfs()
# ie iterative deepening depth first search


def recursivelyFindSolution(node: PathNode, goalState: List[int], maxDepth: int = 10) -> List[PathNode]:
    """
    Not sure yet - but we'll call itself until we find a solution!
    :param node: represents information about a node in a map
    :param goalState: obvious.
    :param maxDepth: maximum allowed tree depth
    :return: The path from the initial state to the goal state as a list of PathNode objects,
             or an empty list if no solution is found within the given depth. This will be a
             sequence of PathNode objects, each representing a state in the solution path.
    """
    # BASE CASE
    if node.state == goalState:
        return [node]

    if node.treeDepth >= maxDepth:
        # raise RuntimeWarning("No solution was found. Try increasing depth?")
        return []

    # RECURSIVE CASE
    # Generate child nodes representing all valid moves from the current state.
    # You'll need to define how you determine valid moves and create child PathNodes.
    children = node.generate_children()
    for child in children:
        # Recursively call the function on child nodes with the same depth limit.
        result = recursivelyFindSolution(child, goalState, maxDepth)
        if result:
            return [node] + result
    return []  # No solutions found from this node.


def iterativeDeepening(puzzle: List[int], maxDepth=10) -> List[int]:
    print("DEBUG Trace solution.iterativeDeepening: Input Puzzle: {}".format(puzzle))
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    root = PathNode(state=puzzle, treeDepth=0, parent=None)

    for depth in range(maxDepth + 1):
        solution_nodes = recursivelyFindSolution(root, goal_state, depth)
        solution_path: List[int] = []  # stores solution as integers for assignment output.

        if solution_nodes:
            for n in solution_nodes:
                solution_path.append(n.lastPosSwap)
            # Extract the states from the nodes in the solution path if required, or
            # change the PathNode class to store the necessary information that needs
            # to be returned, then format them in the way expected by the problem statement
            return solution_path

    raise Exception("No solutions exist up to depth {}.".format(maxDepth))


# This will be for next project
def astar(puzzle: List[int]):
    print(puzzle)
    path = []
    return list


if __name__ == "__main__":
    initial_state = [0, 1, 2, 3, 4, 5, 6, 8, 7]  # create your initial PathNode instance
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]     # define your goal state
    initial_PathNode_state = PathNode(initial_state, 0)
    solution_path = recursivelyFindSolution(initial_PathNode_state, goal_state)
    print(solution_path)

    print("Solution: {}".format(iterativeDeepening(initial_state)))