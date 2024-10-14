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
    initial_state = problem.initial_state
    maze = problem.maze
    print(initial_state)
    print(problem.goal_states[0])
    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    solution = []
    # stop = input(f"this is the problem goal_state {problem.goal_states}")
    if view0:
        view0['maze'].background[initial_state] = (0, 255, 0) # color the initial state green
        view0['maze'].background[problem.goal_states[0]] = (0, 0, 255)
    fringe.put(SearchNode(initial_state))
    closed_list.put(initial_state)
    while 1:
        node = fringe.get()
        # closed_list.put(node.state)
        # print(fringe, closed_list, sep= '\n')
        # stop = input(f"pause\n\n")
        # print(node.state)
        if view0:
            view0['maze'].background[node.state] = (255, 0, 0)
        if node.state == problem.goal_states[0]: # if node is what we are looking for
            if view0:
                view0['maze'].background[problem.goal_states[0]] = (0, 0, 255)
            print(f"found the end {node}")
            solution.append(node.action)
            parent = node
            while parent != None:
                solution.append(parent.parent_action)
                parent = parent.parent
            solution.pop()
            solution.pop()
            print(solution)
            return solution
        dir = maze.get_directions(node.state) # get all adjacent Edges
        for xd in dir:
            temp = SearchNode(maze.get_adj_tuple(node.state, xd), xd, node, node.action, (node.path_cost + 1))
            # print(temp.state, xd)
            if temp.state not in closed_list:
                closed_list.put(temp.state)
                fringe.put(temp)
                if view0:
                    view0['maze'].background[temp.state] = (0, 255, 0)
            # stop = input(f"pause\n\n")
            
        # for action in solution:
        #     (r, c) = maze.get_adj_tuple((r, c), action)
        #     print((r, c))
        # dirs = maze.get_directions((r, c))
        # if dirs != []:
        #     action = random.choice(dirs)
        #     solution.append(action)
        #     print("actions:", dirs, ",", end='')
        #     print("choose:", action, ",", end='')
        #     print("resulting pos:", maze.get_adj_tuple((r, c), action))
        #     print("solution:", solution)
        #     print()
            
        # if random.randrange(0, 200) == 0:
        #     return solution
        
        #======================================================================
        # TODO: The following randomly colors the maze cells with red and blue.
        # Replace with the following:
        # - Iterate through the fringe and color the states of the search
        #   nodes with blue
        # - Iterate through the closed list and color the states with red
	    # - Color the initial state green
        #======================================================================
        # if view0:
        #     if random.randrange(2) == 0:
        #         r = random.randrange(maze.rows)
        #         c = random.randrange(maze.cols)
        #         if random.choice([0,1]) == 0:
        #             view0['maze'].background[(r,c)] = (255,0,0) # color it red
        #         else:
        #             view0['maze'].background[(r,c)] = (0,0,255) # color it blue
        view0.run() # Draw everything
        
    return None # None is used to indicate no solution
