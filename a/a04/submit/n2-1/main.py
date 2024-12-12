import sys

from Fringe       import *
from ClosedList   import *
from Matrix       import *
from pyboard      import *
from functools    import reduce
from graph_search import graph_search
from SearchNode   import SearchNode

import pygame
pygame.init()


def get_solution(n):
    ret = ''
    for i in range(1, n*n):
        ret += f'{i},'
        dir = ','
    ret += ' '
    return ret

if __name__ == "__main__":
        
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n")

    from config       import *

    surface = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("n^2-1 Problem")

    n = int(input("size: "))
    solution = get_solution(n)
    print(solution)
    mat = matrix(n, input("initial: "))
    board = Board(mat)
    print(board.getmatrix())
    fringe_type = input("bfs or dfs: ")
    if fringe_type == "bfs":
        fringe = FSQueue()
    if fringe_type == "dfs":
        fringe = FSStack()

    closed_list = SetClosedList()

    solution = graph_search(board       = board,
                            solution    = solution,
                            fringe      = fringe,
                            closed_list = closed_list)

    print(rowcol(board.getmatrix(), ' '))

    print(f"solution: {solution}")
    print(f"len(Solution): {len(solution)}")
    print(f"len(closed_list): {len(closed_list)}")
    print(f"len(fringe): {len(fringe)}")
    draw(board.getmatrix(), solution)
