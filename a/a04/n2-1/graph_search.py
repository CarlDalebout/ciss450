import random
from SearchNode import SearchNode

#==============================================================================
# GRAPH_SEARCH
#
# The fringe and closed list must be drawn while the thinking takes place.
# - Draw the closed list blue (255, 0, 0).
# - Draw the fringe in green (0, 255, 0).
#
# There must be NO console printing in this python file. Make sure you remove
# them or comment them out when you are done.
#==============================================================================
def graph_search(board       = None,
                 solution    = [[1,2,3],[4,5,6],[7,8, ]], 
                 fringe      = None,
                 closed_list = None
                 ):
  initial_state = board.matrix
  print("initial_state: ", initial_state)
  print('create function to get goal_state', solution)
  #==========================================================================
  # TODO: The code here creates a *random* solution starting at state (0,0).
  # Replace with the correct late version of graph search algorithm.
  #==========================================================================
  
  return ['N','N','W','S','S','W','N','N']
