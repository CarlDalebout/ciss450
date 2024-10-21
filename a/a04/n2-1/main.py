import sys

import copy
import random
from Fringe       import *
from ClosedList   import *
from Matrix       import *
from animation    import *
from functools    import reduce
from graph_search import graph_search
from SearchNode   import SearchNode

import pygame
pygame.init()

from config       import *

surface = pygame.display.set_mode(SIZE)
pygame.display.set_caption("n^2-1 Problem")

n = int(input("size: "))
mat = input("initial: ")
board = Board(matrix(n, mat))

fringe_type = input("bfs or dfs: ")
if fringe_type == "bfs":
    fringe = FSQueue()
if fringe_type == "dfs":
    fringe = FSStack()

closed_list = SetClosedList()

solution = graph_search(board       = board,
                        fringe      = fringe,
                        closed_list = closed_list)

print(rowcol(board.matrix, '5'))

if solution == None:
    print("solution = None")
    draw(board.matrix, solution)

else:
    print(f"solution: {solution}")
    print(f"len(Solution): {len(solution)}")
    print(f"len(closed_list): {len(closed_list)}")
    print(f"len(fringe): {len(fringe)}")
    draw(board, solution)


