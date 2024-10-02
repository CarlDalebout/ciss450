import math as math

def printBoard(n, s):
    width = int(math.log10(n*n) + 1)
    def line(n, width):
        ret = n * ('+' + width * '-') + '+'
        return ret
    for row in s:
        print(line(n, width))
        print('|' + ('|'.join([str(_).rjust(width) for _ in row]) + '|'))

    print(line(n, width))

def bt_kt(n, s, r = None, c = None, taken = 0):
    # printBoard(n,s)
    if r == None:
        # special case ... can pick any square
        for r in range(n):
            for c in range(n):
                s[r][c] = 1
                flag = bt_kt(n, s, r, c, 1)
                if flag:
                    return True
                else:
                    # printBoard(n,s)
                    # print("!!!have to backtrack!!!")
                    s[r][c] = ' '
        return False
    
    else:
        if taken == n**2:
            return True
        
        else:
            for (dr, dc) in [(-1, +2), (-2, +1), (-2, -1), (-1, -2),
                (+1, -2), (+2, -1), (+2, +1), (+1, +2)]:
                r0, c0 = r + dr, c +dc
                if 0 <= r0 < n and 0 <= c0 < n and s[r0][c0] == ' ':
                    s[r0][c0] = taken + 1
                    flag = bt_kt(n, s, r0, c0, taken+1)
                    if flag:
                        return True
                    else:
                        # print("!!!have to backtrack!!!")
                        # printBoard(n,s)
                        s[r0][c0] = ' '
            # print("!!!have to backtrack!!!")
            # printBoard(n,s)
            return False

if __name__ == '__main__':
    n = int(input("n: "))
    print(n)
    s = [[' ' for r in range(n)] for c in range(n)]
    printBoard(n, s)

    flag = bt_kt(n, s)
    if flag:
        print("Done!!!")
        print(s)
    else:
        print("Fail!!!")
