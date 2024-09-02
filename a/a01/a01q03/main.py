def find_(list = None):
    for i, char in enumerate(list):
        if char == ' ':
            return i
        
    return -1 

def move2(direction = None, list = None):
    while direction != 'n' and direction != 's' and direction != 'e' and direction != 'w': # while look to check direction value
        direction = input("!!!invalid direction!!! please pick 'n', 's', 'e', or 'w': ")
    
    space = find_(list)
    

if __name__ == '__main__':
    direction = input() # 'left' and 'right' are accepted (without quotes)
    s = input()         # string from user like "123 8" (without quotes)
    m = list(s)
    # print(m)
    print(move2(direction=direction, list=m))