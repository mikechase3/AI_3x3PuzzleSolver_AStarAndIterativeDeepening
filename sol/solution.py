#This is the only file you need to work on. You do NOT need to modify other files
from typing import List

from sol.functionLib import PathNode

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
'''


# Below are the functions you need to implement. For the first project, you only need to finish implementing iddfs()
# ie iterative deepening depth first search


# here you need to implement the Iterative Deepening Search Method



def iterativeDeepening(puzzle: List[int]):  # input is a list of 9 numbers. 8 is "empty"
    print("Input Puzzle: {}".format(puzzle))
    goal_state: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    PathNode

    return list


# This will be for next project
def astar(puzzle: List[int]):
    print(puzzle)
    path = []
    return list