"""
DO NOT CHANGE ANYTHING IN THIS FILE.
"""

"""
For this problem, note that the Bot receives
- maze
- starting row and column
- ending row and column
These forms the problem:
- the maze gives us "actions" and "successors"
- starting row and column gives us the initial state
- ending row and column gives us the goal state
"""

LENGTH = 1000
import random;random.seed()

class Bot:
    
    def __init__(self, path):
        self.path = path

    def run(self):
        pass


class RandomBot(Bot):
    
    def __init__(self,
                 maze,
                 start=(None, None)):
        self.maze = maze
        if start == (None, None):
            r = random.randrange(maze.rows)
            c = random.randrange(maze.cols)
            start = (r, c)
        self.start = start
            
        path = [start]
        Bot.__init__(self, path)

    def set_path(self, path):
        self.path = path


