# File: main.py
# Directory: ciss450/a/a01/a01q06
# Author: Carl Dalebout

def crossover(xs=None, ys=None, index0=0, index1=0):
    
    us = []
    vs = []

    if isinstance(xs, str) and isinstance(ys, str):
        for i  in range(index0):
            us.append(xs[i])
            vs.append(ys[i])

        if index1 <= len(xs) and index1 <= len(ys): # case for where index1 is less then the len of both xs and ys
            for i in range(index0, index1):
                us.append(ys[i])
                vs.append(xs[i])
        
        elif index1 <=len(xs):                      # case for where index1 is less then the len xs but greater then the len ys
            for i in range(index0, index1):
                vs.append(xs[i])
            for i in range(index0, len(ys)):
                us.append(ys[i])

        elif index1 <= len(ys):                     # case for where index1 is greater then the len of xs but less then the len of ys
            for i in range(index0, len(xs)):
                vs.append(xs[i])
            for i in range(index0, len(index1)):
                us.append(ys[i])
            
        else:                                      # case for where index1 is greater then the len of both xs and ys
            for i in range(index0, len(xs)):
                vs.append(xs[i])
            for i in range(index0, len(ys)):
                us.append(ys[i])
            

        for i in range(index1, len(xs)):
            us.append(xs[i])
        
        for i in range(index1, len(ys)):
            vs.append(ys[i])
        
        return us, vs
    
    elif isinstance(xs, list) and isinstance(ys, list):
        for i  in range(index0):
            us.append(xs[i])
            vs.append(ys[i])
        for i in range(index0, index1):
            us.append(ys[i])
            vs.append(xs[i])
        for i in range(index1, len(xs)):
            us.append(xs[i])
        for i in range(index1, len(ys)):
            vs.append(ys[i])
        return us, vs 
    
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
