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
                 solution    = '1,2,3,4,5,6,7,8, ', 
                 fringe      = None,
                 closed_list = None
                 ):
  initial_state = board.getmatrix()
  print("initial_matrix: ", initial_state)
  
  state = board.getstate(initial_state)
  print("initial_state:  ", state)

  print('goal_state:     ', solution)
  #==========================================================================
  # TODO: The code here creates a *random* solution starting at state (0,0).
  # Replace with the correct late version of graph search algorithm.
  #==========================================================================
  
  fringe.put(SearchNode(state))
  closed_list.put(state)
  while 1:
    node = fringe.get()
    # input()
    # print(f"current state: [{node.state}]\nsolution:      [{solution}]")
    if node.state == solution:
      print(f"found the end")
      return node.solution()
    
    dir = board.getactions(node.state)
    for xd in dir:
      temp = SearchNode(board.getNewState(node.state, xd), node, xd, 1)
      if temp.state not in closed_list:
        closed_list.put(temp.state)
        fringe.put(temp)

  return None