# File: main.py
# Directory: ciss450/a/a01/a01q06
# Author: Carl Dalebout

def crossover(xs=None, ys=None, index0=0, index1=0):

    if isinstance(xs, str) and isinstance(ys, str):
        pass
    elif isinstance(xs, list) and isinstance(ys, list):
        pass    
    else:
        raise ValueError("ERROR in crossover: xs=%s, ys=%s" % (xs, ys))

if __name__ == '__main__':

    i = int(input()) # enter 0 for string xs and 1 for int list xs

    if i == 0:
        xs = input() # for instance enter "abcdefghi" (w/o quotes)
        ys = input() # for instance enter "ABCDEFGHI" (w/o quotes)
    else:
        xs = input() # for instance enter "5,3,1,2,6,5"
        xs = xs.split(",") # xs becomes ['5','3','1','2','6','5']
        xs = [int(x) for x in xs] # xs becomes [5,3,1,2,6,5]
        ys = input() # for instance enter "5,2,1,4,3,3"
        ys = ys.split(",") # ys becomes ['5','2','1','4','3','3']
        ys = [int(y) for y in ys] # ys becomes [5,2,1,4,3,3]

    index0 = int(input())
    index1 = int(input())
    us, vs = crossover(xs, ys, index0, index1)

    print(us)
    print(vs)
