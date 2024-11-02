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
                 Node=None,
                 fringe=None,
                 closed_list=None,
                 view0=None,
                 ):

    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    solution = []
    
    while 1:
                
        (r, c) = (0, 0)
        maze = problem.maze
        for action in solution:
            (r, c) = maze.get_adj_tuple((r, c), action)
        dirs = maze.get_directions((r, c))
        if dirs != []:
            action = random.choice(dirs)
            solution.append(action)
            print("actions:", dirs, ",", end='')
            print("choose:", action, ",", end='')
            print("resulting pos:", maze.get_adj_tuple((r, c), action))
            print("solution:", solution)
            print()
            
        if random.randrange(0, 200) == 0:
            return solution
        
        #======================================================================
        # TODO: The following randomly colors the maze cells with red and blue.
        # Replace with the following:
        # - Iterate through the fringe and color the states of the search
        #   nodes with blue
        # - Iterate through the closed list and color the states with red
	# - Color the initial state green
        #======================================================================
        if view0:
            if random.randrange(2) == 0:
                r = random.randrange(maze.rows)
                c = random.randrange(maze.cols)
                if random.choice([0,1]) == 0:
                    view0['maze'].background[(r,c)] = (255,0,0) # color it red
                else:
                    view0['maze'].background[(r,c)] = (0,0,255) # color it blue
            view0.run() # Draw everything
        
    return None # None is used to indicate no solution
