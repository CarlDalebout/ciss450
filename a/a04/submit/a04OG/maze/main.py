"""
There should only be console printing in main.py. Remember to comment out ALL
debug/test printing in your other python files.
"""

import sys
import random;

import config
from pymaze import *
from Problem import *
from Fringe import *
from ClosedList import *
from Bot import RandomBot
from view import View
from view import EdgeView
from graph_search import graph_search

seed = int(input("enter random seed: "))
random.seed(seed)

#==============================================================================
# DO NOT CHANGE ANYTHING IN THIS SECTION.
# Create maze
#==============================================================================
ROWS = config.ROWS
COLS = config.COLS
PUNCHES = config.PUNCHES
option = int(input("0-random maze or 1-stored maze: "))
maze = DFSMazeWithCycles(ROWS, COLS, PUNCHES)
if option == 1:
    maze.restore('maze.json')

#==============================================================================
# DO NOT CHANGE ANYTHING IN THIS SECTION.
#==============================================================================
NUMBOTS = 1
r0 = int(input("initial row: "))
c0 = int(input("initial column: "))
initial_state = (r0, c0)
r1 = int(input("goal row: "))
c1 = int(input("goal column: "))
goal_state = (r1, c1)
search = input("bfs or dfs: ")

#==============================================================================
# NEW 2018
# gui == True iff use graphical animation. For now set this to True.
#==============================================================================
gui = input('graphical animation? (y/n): ')
if gui in 'yY':
    gui = True
else:
    gui = False

#==============================================================================
# DO NOT CHANGE ANYTHING IN THIS SECTION.
# Create view of maze and bot
#==============================================================================
if gui:
    CELLWIDTH = config.CELLWIDTH
    BOT_COLOR = config.BOT_COLOR
    view0 = View(width=(COLS) * CELLWIDTH,
                 height=(ROWS) * CELLWIDTH,
                 delay=config.DELAY)
    mazeview = view0.add_maze(maze, name='maze')
    edgeview = view0.add_edges(mazeview, name='edgeview')
    
    bots = []
    for i in range(NUMBOTS):
        bot = RandomBot(maze, start=(r0, c0))
        bots.append(bot)
        name = 'bot%s' % i
        view0.add_bot(bot,
                      mazeview,
                      color=BOT_COLOR,
                      name=name)
else:
    view0 = None

#===========================================================
# TODO: Compute solution using graph search.
# Select the correct fringe object.
#===========================================================
problem = MazeProblem(maze=maze,
                      initial_state=(r0,c0),
                      goal_states=[(r1,c1)])

if search == 'bfs':
    fringe = Fringe()
elif search == 'dfs':
    fringe = Fringe()
else:
    raise Exception('invalid search')

print("close animation window to halt", flush=True)
closed_list = SetClosedList()
solution = graph_search(problem=problem,
                        fringe=fringe,
                        closed_list=closed_list,
                        view0=view0)

#==============================================================================
# DO NOT CHANGE ANYTHING IN THIS SECTION.
#==============================================================================
if solution == None:
    print("solution = None")
    while 1:
        view0.run()
else:
    print("solution: %s" % solution)
    print("len(solution): %s" % len(solution))
    print("len(closed_list): %s" % len(closed_list))
    print("len(fringe): %s" % len(fringe))

    # Compute path from solution for drawing.
    maze = problem.maze
    (r, c) = initial_state
    path = [initial_state]
    for action in solution:
        (r, c) = maze.get_adj_tuple((r, c), action)
        path.append((r, c))
        print("path: %s" % path)

    if gui:
        input("press enter to draw path ... ")
        print("close animation window to halt", flush=True)
        for bot in bots: 
            bot.set_path(path)
        while 1:
            view0.run()
