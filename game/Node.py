import time
from collections import deque
import heapq
import math

class Node:
    def __init__(self, parent, puzzle, cost):
        self.parent = parent
        self.puzzle = puzzle
        self.children = []
        self.cost = cost

