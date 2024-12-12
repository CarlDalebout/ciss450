# File:  VertexSet.py
# Dir: a/a02/a02q02
# Author: Carl Dalebout

class VertexSet:
    def __init__(self, V):
        '''
        V - list/tuple/set/frozenset of nodes
        self.V - set of nodes with values from V
        '''
        self.V = set(V)
    
    def __contains__(self, i):
        return i in self.V
    
    def __iter__(self):
        for _ in self.V:
            yield _

    def __str__(self):
        xs = list(self.V)
        xs.sort()
        s = ', '.join([str(x) for x in xs])
        return '{%s}' % s

if __name__ == '__main__':
    
    V = VertexSet([1,2,3])
    
    print(V)
    print(1 in V) # 1 in V same as V.__contains__(1)
    print(4 in V)
    print("v0" in V)
    
    for _ in V:
        print(_, type(_))
