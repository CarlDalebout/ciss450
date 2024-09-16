# File: main.py
# Dir: a/a02/a02q02
# Author: Carl Dalebout

import VertexSet as VertexSet

if __name__ == '__main__':
    
    V = VertexSet.VertexSet([1,2,3])
    
    print(V)
    print(1 in V) # 1 in V same as V.__contains__(1)
    print(4 in V)
    print("v0" in V)
    
    for _ in V:
        print(_, type(_))
