class State(object):
    def __init__(self, value):
        object.__init__(self)
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return '<%s %s %s>' % (self.classname(), id(self.value), self.value)
    @staticmethod
    def classname():
        return 'State'
    @staticmethod
    def compress(state):
        return state.value
    @staticmethod
    def decompress(compressed):
        return compressed
    
    
class MazeState(State):
    """
    (x,y) is compressed into a 64-bit integer [... 32 bits of x ...][... 32 bits of y ...]
    Therefore this assumes a maximum row and column size (32 bit unsigned int) for the maze.
    """    
    def __init__(self, value):
        # Precondition: value is 2-tuple of integers
        assert isinstance(value, tuple)
        assert len(value) == 2
        assert all(isinstance(v, int) for v in value)
        State.__init__(self, value)

    @staticmethod
    def classname():
        return 'MazeState'
    @staticmethod
    def compress(state):
        return (state.value[0] << 32 | state.value[1])
    @staticmethod
    def decompress(compressed):
        return (compressed >> 32, compressed & 0xffff) 
 

class N2M1State(State):
        
    def __init__(self, value):
        # Precondition: value is a rectangular tuple of tuples of strings
        assert isinstance(value, tuple)
        assert all(isinstance(_, tuple) for _ in value)
        assert all(len(_) == len(value[0]) for _ in value[1:])
        assert all(all(isinstance(_, str) for _ in row) for row in value)        
        State.__init__(self, value)
        
    @staticmethod
    def classname():
        return 'N2M1State'
    @staticmethod
    def compress(state):
        xs = []
        for row in state.value:
            xs += row
        return ','.join(xs)
    @staticmethod
    def decompress(compressed):
        xs = compressed.split(',')
        import math
        n = int(math.sqrt(len(xs)))
        ret = []
        while len(xs) != 0:
            ret.append(tuple(xs[:n]))
            xs = xs[n:]
        return tuple(ret)
    

if __name__ == '__main__':

    x = MazeState((1,2))
    y = MazeState((1,2))
    z = MazeState((2,3))
    print(x, repr(x))
    print(y, repr(x))
    print(z, repr(z))
    print(x, x.compress(x), x.decompress(x.compress(x)))
    import sys
    print(sys.getsizeof((1,2)), sys.getsizeof(MazeState.compress(x)))

    x = N2M1State((('1','2','3'),('4','5','6'),('7','8',' ')))
    y = N2M1State((('1','2','3'),('4','5','6'),('7','8',' ')))
    z = N2M1State((('1','2','3'),('4','5','6'),('7',' ','8')))
    print(x, repr(x))
    print(y, repr(y))
    print(z, repr(z))
    print(x, x.compress(x), x.decompress(x.compress(x)))
