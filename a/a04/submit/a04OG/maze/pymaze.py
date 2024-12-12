"""
File: pymaze.py

Here are the classes and their constructors:
    
    maze0 = Maze(filename='maze.json') # Restore saved maze # base class
    maze1 = DFSMaze(rows=10, cols=10) # create 10-by-10 DFS maze
    maze2 = DFSMazeWithCycles(rows=10, cols=10,
                              maxpunches=10, maxtries=1000

DFSMaze creates a maze with the given number of rows and columns using a
(depth first traversal by knocking down walls).

DFSMazeWithCycles does the same as DFSMaze, and then
1. In a loop, randomly find (row, col) and direction to
   punch a hole if the choice is valid.
2. Will stop 1. if number of punches reach maxpunches
   or when number of times executing the loop reaches
   maxtries
This will create loops in the maze.

See also RandomMaze.

After a maze is created, the following two methods are useful. Suppose maze0
is a maze.

- maze0.get_directions((r, c))
  Returns a list of valid directions (i.e., 'N', 'S', 'E', 'W') at position
  (r, c) of the maze. For instance suppose at (r, c), one can go north
  and east and west, then ['N','E','W'] is returned.

- maze0.get_adj_tuple((r, c), dir)
  Returns resulting (row, column) of (r,c) in the given direction dir. For
  instance maze0.get_adj_tuple((2, 5), 'N') returns (1, 5).
       
"""


import math
import random; random.seed()
import json


def adj_tuple(rc, direction):
    ''' return (row, col) adjacent to (r0, c0) in the given direction '''
    (r0,c0) = rc
    if direction == 'N':
        return (r0 - 1, c0)
    if direction == 'S':
        return (r0 + 1, c0)
    if direction == 'E':
        return (r0, c0 + 1)
    if direction == 'W':
        return (r0, c0 - 1)
    raise ValueError('invalid direction %s' % str(direction))


class Maze:    
    """
    Note that doors of the maze is bidirectiona1, i.e., if you can go
    from (row0, col0) to (row1, col1), then you can go from (row1, col1) to
    (row0, col0).
    """

    # dictionary default value is 1 ... i.e., if value is 1, it's not stored.
    DEFAULT = 1
    
    def __init__(self, rows=0, cols=0, filename=None):
        if filename:
            self.restore(filename)
        else:
            self.rows = rows
            self.cols = cols
            self.walls = walls = {}

    def valid_tuple(self, t):
        (r, c) = t
        return (0 <= r < self.rows) and (0 <= c < self.cols)
    
    def get_adj_tuple(self, rc, direction):
        """
        self.get_adj_tuple((r0, c0, direction)) return (row, col)
        """
        tup = adj_tuple(rc, direction)
        #if not self.valid_tuple(tup):
        #    raise ValueError("get_adj_tuple: out of bound")
        return tup

    def get_directions(self, rc):
        """
        returns available directions, i.e., directions available for walking
        """
        dirs = []
        for _ in ['N','S','E','W']:
            if self[rc,_] == 0:
                t = adj_tuple(rc, _)
                if self.valid_tuple(t):
                    dirs.append(_)
        return dirs
        
    def __setitem__(self, x, val):
        (tup, b) = x
        try:
            tup2 = self.get_adj_tuple(tup, b)
        except:
            return

        if not self.valid_tuple(tup2):
            raise ValueError("INVALID")
        z = frozenset([tup, tup2])
        if val == Maze.DEFAULT:
            del self.walls[z]
        else:
            self.walls[z] = val
        
    def __getitem__(self, x):
        '''
        b can be direction or tuple
        '''
        (tup, b) = x
        try:
            tup2 = self.get_adj_tuple(tup, b)
        except Exception as e:
            raise
            #print "[] ...", tup, b
            # out of bound ... so assume there's a wall
            return 1
        
        z = frozenset([tup, tup2])
        return self.walls.get(z, Maze.DEFAULT)
            
    def save(self, filename=None):
        """
        Serialize the object as a json string and save it in the file with
        given filename.
        """
        walls = [tuple(k) for k,v in self.walls.items() if v != Maze.DEFAULT]
        s = json.dumps({'rows':self.rows,
                        'cols':self.cols,
                        'walls':walls,
                        })
        f = open(filename, 'w'); f.write(s)
        
    def restore(self, filename=None):
        """
        Restore maze data from the saved json data from the file with the
        given filename.
        """
        j = json.loads(open(filename, 'r').read())
        self.rows = j['rows']
        self.cols = j['cols']
        self.walls = {}
        for x in j['walls']:
            z = tuple(tuple(_) for _ in x)
            self.walls[frozenset(z)] = 0


class RandomMaze(Maze):

    def __init__(self, rows, cols, maxpunches, maxtries=1000):
        Maze.__init__(self, rows, cols)
        punches = 0
        for i in range(maxtries):
            r = random.randrange(rows)
            c = random.randrange(cols)
            d = random.choice(['N','S','E','W'])
            rc = adj_tuple((r,c), d)
            if self.valid_tuple(rc):
                punches += 1
                self[(r,c), d] = 0
                if punches >- maxtries:
                    break

        
class DFSMaze(Maze):
            
    def __init__(self, rows, cols):
        Maze.__init__(self, rows, cols)
        start = random.randrange(rows), random.randrange(cols)
        stack = [start]
        visited = set([])
        while stack != []:
            r,c = stack[-1]
            visited.add((r,c))
            
            # options
            dirs = [direction for direction in ['N','S','E','W'] \
                    if \
                    ((direction == 'N' and r > 0        and (r-1,c) not in visited) or \
                     (direction == 'S' and r < rows - 1 and (r+1,c) not in visited) or \
                     (direction == 'E' and c < cols - 1 and (r,c+1) not in visited) or \
                     (direction == 'W' and c > 0)       and (r,c-1) not in visited) and \
                    self[(r,c), direction] == 1]
        
            if dirs == []:
                stack.pop()
                continue
            else:
                # pick an option and move forward
                direction = random.choice(dirs)
                self[(r,c), direction] = 0
                if direction == 'N':
                    r -= 1
                elif direction == 'S':
                    r += 1
                elif direction == 'E':
                    c += 1
                else:
                    c -= 1
                stack.append((r,c))


class DFSMazeWithCycles(DFSMaze):
    def __init__(self, rows, cols, maxpunches=0, maxtries=1000):
        """ DFS maze is built then punches are made to existing walls """
        DFSMaze.__init__(self, rows, cols)
        punches = 0
        for _ in range(maxtries):
            r = random.randrange(rows)
            c = random.randrange(cols)

            # Directions where there's a wall -- can't walk in that direction
            # Use this for punching. We still have to check that we're not
            # punching at a wall that results in leaving the maze [??]
            directions = [_ for _ in ['N','S','E','W'] \
                          if _ not in self.get_directions((r,c))] # directions where there's a wall
            #print "directions:", directions
            
            t = []
            for _ in directions:
                rc = adj_tuple((r,c), _)
                #print "rc:", rc
                if self.valid_tuple(rc):
                    #print "is valid"
                    t.append(_)
            directions = t
            #print "direction:", directions
                
            if directions:
                direction = random.choice(directions)
                self[(r,c), direction] = 0
                punches += 1
                if punches >= maxpunches:
                    break

class NoWallMaze(Maze):
    def __init__(self, rows, cols):
        Maze.__init__(self, rows=rows, cols=cols)
        for r in range(rows):
            for c in range(cols):
                for _ in ['N','S','E','W']:
                    t = adj_tuple((r, c), _)
                    if self.valid_tuple(t):
                        self[(r, c),_] = 0
