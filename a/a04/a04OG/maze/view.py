import math
import random; random.seed()
import pygame, sys
pygame.init()
pygame.display.set_caption("CISS450: Maze")
import collections

import config
from config import PATH_COLOR, PATH_LINEWIDTH

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

X,Y = config.X, config.Y
CELLWIDTH = config.CELLWIDTH 
WALLWIDTH = config.WALLWIDTH

BOT_RADIUS = config.BOT_RADIUS
SPEED =  config.SPEED

class MazeView:

    def __init__(self, surface,
                 maze,
                 background=None,
                 cellwidth=50,
                 wallwidth=10,
                 x=0,
                 y=0):
        self.surface = surface
        self.maze = maze
        if background == None: self.background = {}
        else: self.background = background
        self.X = x
        self.Y = y
        self.CELLWIDTH = cellwidth # assumed square
        self.WALLWIDTH = wallwidth

    def CELLCENTER(self, rc):
        (r, c) = rc
        X, Y = self.X, self.Y
        CELLWIDTH = self.CELLWIDTH
        WALLWIDTH = self.WALLWIDTH
        i = X + int((CELLWIDTH+WALLWIDTH)/2.0)
        return int(X + (CELLWIDTH+WALLWIDTH)/2.0 + CELLWIDTH * c), \
           int(Y + (CELLWIDTH+WALLWIDTH)/2.0 + CELLWIDTH * r)

    def run(self):
        surface = self.surface
        maze = self.maze
        background = self.background
        self.draw()

    def draw(self):
        """
        background is a dictionary.
        background[2,3] = (255,0,0) means draw the cell 2,3 red
        """
        ROWS = self.maze.rows
        COLS = self.maze.cols
        CELLWIDTH = self.CELLWIDTH
        WALLWIDTH = self.WALLWIDTH
        background = self.background
        surface = self.surface
        maze = self.maze
        def CELLCENTER(t): return self.CELLCENTER(t)

        # Draw background
        if background != None:
            for r in range(ROWS):
                for c in range(COLS):
                    color = background.get((r,c), None)
                    if color:
                        x,y = CELLCENTER((r,c))
                        rect = pygame.Rect(x - CELLWIDTH/2,
                                           y - CELLWIDTH/2,
                                           CELLWIDTH,
                                           CELLWIDTH)
                        pygame.draw.rect(surface, color, rect)
    
        # Draw walls
        color = WHITE
        for r in range(ROWS):
            for c in range(COLS):

                x,y = CELLCENTER((r,c))
            
                # EAST
                if c == COLS - 1 or maze[(r,c),'E']:
                    rect = pygame.Rect(x + CELLWIDTH/2 - WALLWIDTH/2,
                                       y - CELLWIDTH/2 - WALLWIDTH/2,
                                       WALLWIDTH,
                                       CELLWIDTH + WALLWIDTH)
                    pygame.draw.rect(surface, color, rect)
                    
                # SOUTH
                if r == ROWS - 1 or maze[(r,c),'S']:
                    rect = pygame.Rect(x - CELLWIDTH/2 - WALLWIDTH/2,
                                       y + CELLWIDTH/2 - WALLWIDTH/2,
                                       CELLWIDTH + WALLWIDTH,
                                       WALLWIDTH)
                    pygame.draw.rect(surface, color, rect)

        # DRAW TOP
        for c in range(COLS):
            x,y = CELLCENTER((-1,c))
            rect = pygame.Rect(x - CELLWIDTH/2 - WALLWIDTH/2,
                               y + CELLWIDTH/2 - WALLWIDTH/2,
                               CELLWIDTH + WALLWIDTH,
                               WALLWIDTH)
            pygame.draw.rect(surface, color, rect)
    
        # DRAW LEFT SIDE
        for r in range(ROWS):
            x,y = CELLCENTER((r,-1)) 
            rect = pygame.Rect(x + CELLWIDTH/2 - WALLWIDTH/2,
                               y - CELLWIDTH/2 - WALLWIDTH/2,
                               WALLWIDTH,
                               CELLWIDTH)
            pygame.draw.rect(surface, color, rect)

        # drawing centers of cell
        color = (255,255,255)
        for r in range(ROWS):
            for c in range(COLS):
                center = CELLCENTER((r,c))
                pygame.draw.circle(surface, color, center, 3)


class EdgeView:
    def __init__(self,
                 surface,
                 mazeview,
                 color=(255,255,255)):
        self.surface = surface
        self.mazeview = mazeview
        self.color = color
        self.edges = []
    def add(self, x):
        (rc0, rc1) = x
        self.edges.append((rc0, rc1))
    def remove(rc0, rc1):
        self.edges.remove((rc0, rc1))
    def run(self):
        mazeview = self.mazeview
        for (rc0, rc1) in self.edges:
            p0 = mazeview.CELLCENTER(rc0) 
            p1 = mazeview.CELLCENTER(rc1) 
            pygame.draw.line(self.surface, self.color, p0, p1)


class BotView:
    
    def __init__(self, surface, bot, mazeview,
                 color=None,
                 dx=None, dy=None, # offset within cell
                 ):
        self.bot = bot
        self.surface = surface
        # The ps is a sequence of points in the surface
        # Therefore we need CELLCENTER which is in the maze view
        self.mazeview = mazeview
        self.ps = ps = [mazeview.CELLCENTER(t) for t in bot.path]
        if self.ps:
            self.i = 0
            self.p = ps[0]
        else:
            self.i = -1
            self.p = None
        if not color:
            color = (random.randrange(10,256), random.randrange(10,256), random.randrange(10,256))
        self.color = color
        if not dx: dx = random.randrange(-2, 3)
        self.dx = dx
        if not dy: dy = random.randrange(-2, 3)
        self.dy = dy

    def run(self):
        self.ps = ps = [self.mazeview.CELLCENTER(t) for t in self.bot.path] # because the path could have changed        
        p = self.p
        
        # Compute velocity using ps[i] and ps[i+1] (if ps[i+1] is valid)
        # Have to recompute this since ps can change.
        # (However note that we're not allowing self.i to change -- for now.
        if self.i < len(self.ps) - 1:
            i = self.i
            self.v = (self.ps[i+1][0] - self.ps[i][0], self.ps[i+1][1] - self.ps[i][1])
            length = math.sqrt(self.v[0]*self.v[0] + self.v[1]*self.v[1])
            self.v = (self.v[0]/length * SPEED, self.v[1]/length * SPEED)
        else:
            self.v = (0.0, 0.0)

        # Move self.p by small increment
        self.p = (self.p[0] + self.v[0], self.p[1] + self.v[1])
        
        # If there's a next point, and bot is closed enough to the next point,
        # move bot immediately to the next point.
        if self.i < len(self.ps) - 1 and \
               (self.ps[i+1][1] - self.p[1])**2 + (self.ps[i+1][0] - self.p[0])**2 < 1.5*SPEED:
            self.i += 1
            self.p = self.ps[self.i]

        # 2022/09/23: draw bot's path
        surface = self.surface
        i = self.i                                 
        p0 = self.ps[i]                            
        p1 = self.p                                
        for j in range(0, i):
            pygame.draw.line(surface, PATH_COLOR, self.ps[j], self.ps[j + 1], PATH_LINEWIDTH)
        pygame.draw.line(surface, (0,0,0), p0, p1, PATH_LINEWIDTH)
        pygame.draw.circle(surface, self.color, (int(self.p[0]) + self.dx, int(self.p[1]) + self.dy), int(BOT_RADIUS))


class View:

    def __init__(self, width=None, height=None, delay=100):
        self.width = width
        self.height = height
        if width and height:
            SIZE = width,height
            self.surface = surface = pygame.display.set_mode(SIZE)
        else:
            self.surface = None
        #self.xs = []
        self.views = collections.OrderedDict() # NEW
        self.delay = delay

    # low level access
    def surface(self):
        return self.surface
    
    def add_maze(self,
                 maze,
                 cellwidth=CELLWIDTH,
                 wallwidth=WALLWIDTH,
                 background=None,
                 name='maze', # NEW
                 ):
        rows = maze.rows
        cols = maze.cols
        if not self.surface:
            self.width = WIDTH = cols * CELLWIDTH + WALLWIDTH  
            self.height = HEIGHT = rows * CELLWIDTH + WALLWIDTH 
            SIZE = WIDTH, HEIGHT
            self.surface = surface = pygame.display.set_mode(SIZE)
        mazeview = MazeView(self.surface,
                            maze,
                            cellwidth=cellwidth,
                            wallwidth=wallwidth,
                            background=background)
        #self.xs.append(mazeview)
        self.views[name] = mazeview
        return mazeview
        
    def add_bot(self,
                x,
                mazeview,
                color=None,
                name='bot'):
        self.views[name] = BotView(self.surface,
                                   x,
                                   mazeview,
                                   color=color)

    def add_edges(self, mazeview, name='edgeview'):
        self.views[name] = EdgeView(surface=self.surface,
                                    mazeview=mazeview,
                                    )
        
    def run(self):
        # Exit if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.surface.fill(BLACK)
        for x in self.views.values():
            x.run()
            
        pygame.display.flip()
        if self.delay:
            pygame.time.delay(self.delay)

    # NEW
    def __getitem__(self, name):
        return self.views[name]

