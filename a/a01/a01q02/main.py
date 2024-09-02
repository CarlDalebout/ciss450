def find_(list = None):
    for i, char in enumerate(list):
        if char == ' ':
            return i
        
    return -1 

def move(direction = None, list = None):
    while direction != 'left' and direction != 'right': # while look to check direction value
        direction = input("!!!invalid direction!!! please pick 'left' and 'right':")
    
    space = find_(list)
    if space == -1:
        raise ValueError("ERROR in move: invalid list no space found")
    
    if direction == 'left':
        if space == 0:
            return list
        else:
            list[space] = list[space-1]
            list[space-1] = ' '
            return list
    
    elif direction == 'right':
        if space == len(list)-1:
            return list
        else:
            list[space] = list[space+1]
            list[space+1] = ' '
            return list

if __name__ == '__main__':
    direction = input() # 'left' and 'right' are accepted (without quotes)
    s = input()         # string from user like "123 8" (without quotes)
    m = list(s)
    # print(m)
    print(move(direction=direction, list=m))