# File: main.py
# Directory: ciss450/a/a01/a01q04
# Author: Carl Dalebout

def find_Q(m):
    ret = list()
    
    for i in range(len(m)):
        
        for j, char in enumerate(m[i]):
            
            if char == "Q":
                # print(f"found queen at ({i},{j})")
                ret.append((i, j))
    
    # print(ret)
    return ret

def matrix(n, s, separator=","):
    ret, list = [], []
    tok = ""
    
    for i in s:
        
        if i != separator:
            tok += i
        
        elif i == separator:
            list.append(tok)
            tok = ""
            
            if len(list) == n:
                ret.append(list)
                list = []
    
    if tok != "":
        list.append(tok)
        tok = ""
        
        if list != []:
            ret.append(list)
            list = []

    if list != []:
        ret.append(list)
        list = []

    return ret

def attacking_pairs(m):
    queens = find_Q(m)
    ret = 0
    for q0 in range(0, len(queens)):
        
        for q1 in range(q0+1, len(queens)):
            
            if(queens[q0][0] == queens[q1][0]):   #checking row
                # print(f"pair at ({queens[q0][0]},{queens[q0][1]}), ({queens[q1][0]},{queens[q1][1]})")
                ret +=1
                continue
            
            elif(queens[q0][1] == queens[q1][1]): #checking colm
                # print(f"pair at ({queens[q0][0]},{queens[q0][1]}), ({queens[q1][0]},{queens[q1][1]})")
                ret +=1
                continue
            
            elif(abs(queens[q0][0]-queens[q1][0]) == abs(queens[q0][1] - queens[q1][1])): # checking diag
                # print(f"pair at ({queens[q0][0]},{queens[q0][1]}), ({queens[q1][0]},{queens[q1][1]})")
                ret +=1
                continue

    return ret

if __name__ == '__main__':
    
    # For this:
    # +-+-+-+
    # |Q|Q| |
    # +-+-+-+
    # | | |Q|
    # +-+-+-+
    # | | | |
    # +-+-+-+
    
    s = input()         # enter "Q,Q, , , ,Q, , , " (without double-quotes)
    n = int(input())    # enter 3
    m = matrix(n, s)    # m is a 3-by-3 2D array
    
    for i in m:
        print(i)
    # queens = find_Q(m)
    
    print(attacking_pairs(m))