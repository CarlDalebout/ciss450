import sys
import random;

import config
from Fringe import *
from ClosedList import *
from graph_search import graph_search
from SearchNode import SearchNode

n = int(input("size: "))
board = input("initial: ")
fringe = input("bfs or dfs: ")
