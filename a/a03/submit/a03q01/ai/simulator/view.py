"""
TODO: In View, object name was used to identify object.
Change to object id.

The simulation is discrete. The View object v will be
initialized with the initial env. v will draw and return.
For each subsequent env, v will store the new env and keep
the previous as well. v will then draw a simulation of
the previous env being changed to the next env.
Suppose the envs are e0, e1, e2, ..., e9.
1. When v is intialized with e0. It draw e0 and return.
2. When e1 is added to v, v draw the transition from e0 to e1
   in 2 seconds. At the end of the 2 seconds, it draw e1
   (in case the drawing does not reach e1).
3. e2 is added to v. v repeats 1 with e1, e2.
4. e3 is added to v. v repeats 1 with e2, e3.
etc.
5. e9 is added to v. v repeats 1 with e8, e9.
6. Af the end, we need to signal to

"""

import math
import random; random.seed()
import copy

import pygame, sys

# Move to view constructor
#pygame.init()
#pygame.display.set_caption("CISS450")

sys.path.append('..')
from agent.Agent import Agent
from vacuum_cleaner.Room import Room
from vacuum_cleaner.Clock import Clock

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

CELLWIDTH = 100
CELLHEIGHT = 100
RADIUS = 20

SPEED = 2 # if this is too large tolerance test would fail 


# Draw clock
def draw_clock(surface,
               x, y,
               clock,
               fontsize=24, color=WHITE):
    font = pygame.font.Font(None, 24)
    text = font.render(str(clock), 1, WHITE)
    rect = text.get_rect()
    rect.x = x # self.SIZE[0] - 24
    rect.y = y # self.SIZE[1] - 30
    surface.blit(text, rect)

def draw_bot(surface, x, y, color, radius=20):
    center = (int(x), int(y))
    pygame.draw.circle(surface, color, center, radius)


class View:
    """
    This graphical view draw intermediate transitions between
    states.
    Therefore it must keep the *previous* state.

    Note that the env changes during simulation. The two env's stored
    in the GUI view should be FIXED. Therefore a deep copy
    should be made. Note therefore that the code should identify
    the objects (agents or otherwise) by their class type and name
    and not my object id.
    """
    def __init__(self, env):

        self.env0 = copy.deepcopy(env) # We need to make a copy since env
                                       # will change
        self.env1 = copy.deepcopy(env) 

        pygame.init()
        pygame.display.set_caption("CISS450")

        self.rooms = {}
        self.bots = {}
        self.clock = None
        self.num_rooms = 0
        self.num_agents = 0
        for obj in env.objs:
            if isinstance(obj, Agent):
                self.bots[obj.name] = obj.state.value
                self.num_agents += 1
            elif isinstance(obj, Room):
                self.rooms[obj.name] = obj.state.value
                self.num_rooms += 1
            elif isinstance(obj, Clock):
                self.clock = obj

        #======================================================================
        # TODO: Make this 2D.
        # Since rooms are names A, B, C, D, maybe name AA, AB, AC, AD, ...,
        # CA, CB, CC, CD for 3 rows. Here AA is the same as A, i.e., if the
        # room name has 1 character c, the by default the name ia Ac.
        # Or better have a name-(row,col) association. 
        #======================================================================
        
        WIDTH = CELLWIDTH * self.num_rooms
        #HEIGHT = CELLHEIGHT + 40 * len(self.bots.values()) # extra for legend
        HEIGHT = CELLHEIGHT + 40 * self.num_agents
        self.SIZE = SIZE = WIDTH, HEIGHT
        self.surface = surface = pygame.display.set_mode(SIZE)

        # Offset position in cell for each bot
        # The lower left is for the dirt
        self.bot_offset = {}
        for name in self.bots.keys():
            self.bot_offset[name] = [random.randrange(RADIUS + 10,
                                                      CELLWIDTH-RADIUS-10),
                                     random.randrange(RADIUS + 10,
                                                      CELLWIDTH-RADIUS-10),
                                     ]
        
        # Color of each bot
        self.bot_color = {}
        for i,name in enumerate(self.bots.keys()):
            if i == 0:
                self.bot_color[name] = (255, 0, 0)
            elif i == 1:
                self.bot_color[name] = (0, 255, 0)
            elif i == 2:
                self.bot_color[name] = (0, 0, 255)
            else:
                self.bot_color[name] = (random.randrange(128, 256),
                                        random.randrange(128, 256),
                                        random.randrange(128, 256))

        # Dirt rect (without cell)
        self.dirt_offset = [10, CELLHEIGHT - 10, 50, 10]
        self.dirt_color = WHITE


    def __del__(self):
        pygame.display.quit()
        pygame.quit()
        
    #def run(self, envs, actions=None):
    def run(self, env, actions=None):

        clock = self.clock.state.value
        dt = 2000 # time for each simulator step

        i = 0
        t = pygame.time.get_ticks() # Start time curr time step simulation

        #curr_env = envs[0]
        #next_env = envs[1]

        self.env0 = self.env1
        self.env1 = copy.deepcopy(env)
        curr_env = self.env0 # actually should call this prev_env
        next_env = self.env1 # and this one should be curr_env

        stop = False
        while 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            if stop: break
            
            if pygame.time.get_ticks() - t > dt:
                # CASE: Time step for current simulation step
                # has ended.
                # Should draw objects at their final destinations before
                # stopping this simulation loop.
                self.env0 = copy.deepcopy(env)
                self.env1 = self.env0 # simulation step ended: env0=env1
                curr_env = self.env0
                next_env = self.env0
                stop = True
            
            curr_rooms = {}
            curr_bots = {}
            for obj in curr_env.objs:
                state = obj.state.value
                if isinstance(obj, Agent): curr_bots[obj.name] = state
                elif isinstance(obj, Room): curr_rooms[obj.name] = state
            next_rooms = {}
            next_bots = {}
            for obj in next_env.objs:
                state = obj.state.value
                if isinstance(obj, Agent): next_bots[obj.name] = state
                elif isinstance(obj, Room): next_rooms[obj.name] = state
        
            self.surface.fill(BLACK)

            # Draw cell boundaries
            for _ in range(self.num_rooms):
                rect = pygame.Rect(_*CELLWIDTH, 0, CELLWIDTH, CELLHEIGHT)
                pygame.draw.rect(self.surface, WHITE, rect, 4)

            # Draw legend
            for j,(name,v) in enumerate(sorted(self.bot_color.items())[::-1]):
                # Draw name of bot
                font = pygame.font.Font(None, 24)
                text = font.render(name, 1, WHITE)
                rect = text.get_rect()
                rect.x += 40
                rect.y = self.SIZE[1] - (j + 1)*(30)
                self.surface.blit(text, rect)
                # Get action of this object
                action = env.find_first_by_name(name).action
                text = font.render(action, 1, WHITE)
                rect = text.get_rect()
                rect.x += 80
                rect.y = self.SIZE[1] - (j + 1)*(30)
                self.surface.blit(text, rect)
                # Draw circle
                (x, y) = (15, rect.y + 10)
                pygame.draw.circle(self.surface,
                                   self.bot_color[name], (x,y), 8)

            draw_clock(surface=self.surface,
                       x=self.SIZE[0] - 24,
                       y=self.SIZE[1] - 30,
                       clock=clock)
            
            # Draw dirt
            for k,v in curr_rooms.items():
                if v == 'Dirty':
                    if next_rooms[k] == 'Dirty':
                        color = self.dirt_color
                        height = 10
                    else:
                        # dirt is disappearing
                        color = list(self.dirt_color)
                        factor = (dt - (pygame.time.get_ticks() - t))/float(dt)
                        color[0] = int(color[0] * factor)
                        color[1] = int(color[1] * factor)
                        color[2] = int(color[2] * factor)
                        height = int(10 * factor)
                        if height < 0: height = 0
                    if height > 0:
                        col = ord(k) - ord('A')
                        rect = pygame.Rect(col * CELLWIDTH + 10,
                                           80,
                                           20, height)
                        color = self.dirt_color
                        pygame.draw.rect(self.surface, color, rect)

            #==================================================================
            # TODO: For 2D, need to translate letter naming of rooms to
            # (row, col) in the grid.
            #============================o=====================================

            # Draw bot
            for k,v in curr_bots.items():
                col = ord(v) - ord('A')
                next_col = ord(next_bots[k]) - ord('A')
                factor = (pygame.time.get_ticks() - t) / float(dt)
                delta = (next_col - col) * factor
                x = (col+delta) * CELLWIDTH + self.bot_offset[k][1]
                y = self.bot_offset[k][0]
                draw_bot(self.surface, x, y, self.bot_color[k])
                
            pygame.display.flip()
            pygame.time.delay(10)

        # Slight delay of 1 second after this time step simulation
        t = pygame.time.get_ticks()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            if pygame.time.get_ticks() - t >= 1000:
                break
            pygame.time.delay(10)
