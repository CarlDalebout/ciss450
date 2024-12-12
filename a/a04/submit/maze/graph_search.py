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
def graph_search(problem=None,
                 fringe=None,
                 closed_list=None,
                 view0=None,
                 ):
    initial_state = problem.initial_state
    maze = problem.maze
    print(initial_state)
    print(problem.goal_states[0])
    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    if view0:
        view0['maze'].background[initial_state] = (0, 255, 0) # color the initial state green
        view0['maze'].background[problem.goal_states[0]] = (0, 0, 255)
    fringe.put(SearchNode(initial_state))
    closed_list.put(initial_state)
    while 1:
        node = fringe.get()
        if view0:
            view0['maze'].background[node.state] = (255, 0, 0)
        
        if node.state == problem.goal_states[0]: # if node is what we are looking for
            print(f"found the end {node}")
            return node.solution()
        
        dir = maze.get_directions(node.state) # get all adjacent Edges
        for xd in dir:
            temp = SearchNode(maze.get_adj_tuple(node.state, xd), node, xd, 1)
            if temp.state not in closed_list:
                closed_list.put(temp.state)
                fringe.put(temp)
                if view0:
                    view0['maze'].background[temp.state] = (0, 255, 0)
        
        view0.run() # Draw everything
        
    return None # None is used to indicate no solution
