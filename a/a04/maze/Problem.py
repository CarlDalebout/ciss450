"""
MazeProblem is a subclass of Problem.The following methods of MazeProblem must tbe implemented:
- goal_test(self, state)
- actions(self, state)
- result(self, state, action)
- successors(self, state)
    
"""
class Problem(object):

    def __init__(self,
                 initial_state):
        self.initial_state = initial_state
    
    def get_initial_state(self):
        return self.initial_state

    def goal_test(self, state):
        raise NotImplementedError
                 
    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def successors(self, state):
        raise NotImplementedError
    
    def cost(self, state, action):
        return 1


class MazeProblem(Problem):

    def __init__(self,
                 maze=None,
                 initial_state=None,
                 goal_states=None):
        Problem.__init__(self, initial_state)
        self.maze = maze
        self.goal_states = goal_states

    def goal_test(self, state):
        return state in self.goal_states
                 
    def actions(self, state):
        return self.maze.get_directions(state)

    def result(self, state, action):
        return self.maze.get_adj_tuple(state, action)

    def successors(self, state):
        dirs = self.actions(state)
        return [(d, self.result(state, d)) for d in dirs]

