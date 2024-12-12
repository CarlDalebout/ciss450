import sys
import copy
from Matrix       import *
from functools    import reduce
import pygame
pygame.init()

from config import *

surface = pygame.display.set_mode(SIZE)
pygame.display.set_caption("N^2-1 Problem")

tries = 0

def row(matrix):
    return reduce(lambda x,y:x+y, matrix, [])

def move(char, dir, matrix):
    """ This is used to create test cases. """
    i = row(matrix).index(char)
    maxrows = len(matrix)
    maxcols = len(matrix[0])
    r = i // maxcols
    c = i % maxrows
    if dir == 'N':
        if r - 1 < 0: raise ValueError
        matrix[r-1][c], matrix[r][c] = matrix[r][c], matrix[r-1][c]
    elif dir == 'S':
        if r + 1 >= len(matrix): raise ValueError
        matrix[r+1][c], matrix[r][c] = matrix[r][c], matrix[r+1][c]
    elif dir == 'E':
        if c + 1 >= len(matrix): raise ValueError
        matrix[r][c+1], matrix[r][c] = matrix[r][c], matrix[r][c+1]
    elif dir == 'W':
        if c - 1 < 0: raise ValueError
        matrix[r][c-1], matrix[r][c] = matrix[r][c], matrix[r][c-1]    
    return matrix

class Digit:

    def __init__(self,i,fontsize,rect):
        w,h = rect[2],rect[3]
        font = pygame.font.Font(None, fontsize)
        text = str(i)
        textsize = font.size(text)
        self.__image = font.render(text, 0, WHITE, BLACK)
        self.__rect = rect[:]
        self.__xoffset = (w - textsize[0]) // 2
        self.__yoffset = (h - textsize[1]) // 2

    def draw(self):
        image = self.__image
        x = self.__rect[0] + self.__xoffset
        y = self.__rect[1] + self.__yoffset
        surface.blit(image, (x,y))
        pygame.display.flip()

    def erase(self):
        surface.fill(BLACK,self.__rect)

    def update(self,vector):
        x0,y0,x1,y1 = vector
        dx = x1 - x0
        dy = y1 - y0
        d = max(abs(dx),abs(dy))
        for i in range(d, SPEED):
            self.erase()
            self.__rect[0] += dx // d
            self.__rect[1] += dy // d
            self.draw()
            if DELAY:
                pygame.time.delay(DELAY)
        # one last time
        self.erase()
        self.__rect[0] = x1
        self.__rect[1] = y1
        self.draw()

class Board:

    def __init__(self,matrix):
        import copy
        self.__matrix = copy.deepcopy(matrix)
        self.__tries = 0
        self.max_row = len(matrix)
        self.max_col = len(matrix[0])
        for r in range(self.max_row):
            for c in range(self.max_col):
                digit = matrix[r][c]
                if digit!=None:
                    rect = [ c*TILE_WIDTH, r*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT ]
                    Digit(digit,FONT_SIZE, rect).draw()
        
    def __repr__(self):
        
        def None_to_space(x):
            if x==None:
                return " "
            else:
                return x

        s = "%10d.\n" % self.__tries
        for row in self.__matrix:
            row = [ "%4s" % None_to_space(x) for x in row]
            s += "                %s\n" % ("".join(row))
        return s
        
    def getmatrix(self):
        return self.__matrix

    def getactions(self, state):
        '''
            return ['N', 'S', ... ]
        '''
        m = matrix(self.max_col, state)
        ret = []
        for r, row in enumerate(m):
            for c, v in enumerate(row):
                if v == ' ':
                    if r > 0:
                        ret.append('N')
                    if r < self.max_row - 1:
                        ret.append('S') 
                    if c < self.max_col - 1:
                        ret.append('E')
                    if c > 0:
                        ret.append('W')
                    break
        return ret
    
    def getstate(self, matrix):
        state = ''
        dir = ''
        for r in range(self.max_row):
            for c in range(self.max_col):
                state += (dir + matrix[r][c])
                dir = ','
        return state
    
    def getNewState(self, state, action):
        mat = matrix(self.max_col, state)
        r0, c0 = rowcol(mat, ' ')
        r1, c1 = r0, c0
        if action == 'N':
            r1 -= 1
        elif action == 'S':
            r1 += 1
        elif action == 'E':
            c1 += 1
        elif action == 'W':
            c1 -= 1
        mat[r0][c0] = mat[r1][c1]
        mat[r1][c1] = ' '
        return self.getstate(mat)
        
    def update(self,vector,matrix):
        row,col,newrow,newcol = vector
        x0,y0 = col*TILE_WIDTH, row
        x0,y0 = col*TILE_WIDTH, row*TILE_HEIGHT
        x1,y1 = newcol*TILE_WIDTH, newrow*TILE_HEIGHT
        i = self.__matrix[newrow][newcol]
        rect = [ newcol*TILE_WIDTH, newrow*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT ]
        digit = Digit(i,FONT_SIZE, rect)
        digit.update([x1,y1,x0,y0])
        self.__matrix[row][col] = self.__matrix[newrow][newcol]
        self.__matrix[newrow][newcol] = None

        self.__tries += 1
        text = str(self.__tries)
        image = TRIES_FONT.render(text, 0, TRIES_COLOR, BLACK)
        rect = TRIES_FONT.size(text)
        x = WIDTH - rect[0]
        y = HEIGHT - rect[1]
        surface.fill(BLACK, [0,HEIGHT-rect[1],WIDTH,HEIGHT])
        surface.blit(image, (x,y))
        pygame.display.flip()

    

def rowcol(mat, target):
    for rownum, row in enumerate(mat):
        for colnum, col in enumerate(row):
            if col == target: return rownum, colnum
    raise ValueError("can't find %s" % target)


def draw(mat=[['0','1','2'],['3','4','5'],['6','7',' ']],
         solution=['N','N','E','E'],
         prompt=True):
    
    # Replace ' ' with None in mat
    for r in mat:
        for i,c in enumerate(r):
            if c == ' ':
                r[i] = None
    board = Board(mat) 
    
    while 1:
        if prompt:
            input("press enter to continue ... ")
        for event in pygame.event.get():
            if event.type == pygame.QUIT: break
            
        oldmatrix = copy.deepcopy(mat)
        d, solution = solution[0], solution[1:]
        newmatrix = move(None, d, mat)
        oldr, oldc = rowcol(oldmatrix, None)
        newr, newc = rowcol(newmatrix, None)
        vector = (oldr, oldc, newr, newc)        
        
        # draw
        board.update(vector,mat)
        print(board)
        
        mat = newmatrix
        if len(solution) == 0:
            break

        pygame.display.flip()
        pygame.time.delay(100)
        
    input("animation ended ... press enter to halt ... ")

    
if __name__ == "__main__":

    print("Test animation of 3x3")
    draw(mat=[['0','1','2'],['3','4','5'],['6','7',' ']],
         solution=['N','N','W','W','S','E'])

    print("Test animation of 4x4")
    draw(mat=[['0','1','2','3'],
              ['4','5','6','7'],
              ['8','9','10','11'],
              ['12','13','14',' ']],
         solution=['N','N','W','W','S','E', 'E','S','W','W','N','N','E', 'W', 'S', 'S', 'W','N','N','N','E','E','S'], prompt=False)
