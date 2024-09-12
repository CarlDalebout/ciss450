# File: main.py
# Directory: ciss450/a/a01/a01q03
# Author: Carl Dalebout

def find_(list = None, target = " "):
    for i in range(len(list)):
        for j, char in enumerate(list[i]):
            if char == target:
                return (i,j)
    return -1 

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

def move2(direction = None, list = None, target = ' '):
    while direction != 'n' and direction != 's' and direction != 'e' and direction != 'w': # while look to check direction value
        direction = input("!!!invalid direction!!! please pick 'n', 's', 'e', or 'w': ")
    
    space = find_(list=list, target=target)
    
    if space == -1:
        print("!!!Error!!! could not find space!!!")
        return -1

    if direction == 'n':
        if space[0] == 0:
            return list
        else: 
            list[space[0]][space[1]] = list[space[0]-1][space[1]]
            list[space[0] - 1][space[1]] = ' '
            return list
    
    elif direction == 's':
        if space[0] == len(list)-1:
            return list
        else: 
            list[space[0]][space[1]] = list[space[0]+1][space[1]]
            list[space[0] + 1][space[1]] = ' '
            return list
    
    elif direction == 'e':
        if space[1] == len(list[0])-1:
            return list
        else: 
            list[space[0]][space[1]] = list[space[0]][space[1]+1]
            list[space[0]][space[1]+1] = ' '
            return list
    
    elif direction == 'w':
        if space[1] == 0:
            return list
        else: 
            list[space[0]][space[1]] = list[space[0]-1][space[1]-1]
            list[space[0]][space[1]-1] = ' '
            return list
    else:
        print("no cases checked")
        return list

if __name__ == '__main__':
    
    direction = input("direction: ") # for instance enter "N" (w/o quotes)
    s = input("list: ")         # for instance enter "1,2,3,4,5,6,7, ,8" (w/o
                        # quotes)
    n = int(input("size: "))         # for instance enter 3
    m = matrix(n=n, s=s, separator=",")
    target = input("target: ")    # for instance enter " " (w/o quotes)
                        # Enter "" (w/o quotes) for default case.
    if target == '':
            print(move2(direction=direction, list=m))
    else:
        while(direction != 'd'):
            print(move2(direction=direction, list=m, target=target))
            