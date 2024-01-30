# Puzzle8 AI Techniques
This project uses some AI techniques to solve an 8 piece puzzle within a 3x3 grid.

## REQUIREMENTS
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

## References
1. [Branch/Bound](https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/)
2. 8-puzzle problem [medium writeup](https://medium.com/@dpthegrey/8-puzzle-problem-2ec7d832b6db)

## What it should do
Something like this:
![sol](treeDemoToFindSolution.png)

## Changelog (newest->oldest)

### Jan 30 \@ 8AM 
1. Solution isn't memoized.
2. It's going deep. Need to implement a queue? Not iterative deepening yet.
![that](TheseStinkToDebug.png)

### Earlier
Got DFS working! Not iterative deepening or A* yet.