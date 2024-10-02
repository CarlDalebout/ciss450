import math

"""
    +-+   +-+   +-+
    |R| - |G| - |R|
    +-+   +-+   +-+
       \   |   / |
        \  |  /  |
         \ | /   |
          +-+   +-+
          |B| - |G|
          +-+   +-+

   0 1 2 3 4
  +-+-+-+-+-+
0 | |1| |1| |
  +-+-+-+-+-+
1 |1| |1|1| |
  +-+-+-+-+-+
2 | |1| |1|1|
  +-+-+-+-+-+
3 |1|1|1| |1|
  +-+-+-+-+-+
4 | | |1|1| |
  +-+-+-+-+-+

"""

def printBoard(n, s):
    def line(n):
        ret = n * ('+' + '-') + '+'
        return ret
    for row in s:
        print(line(n))
        print('|' + ('|'.join([str(_) for _ in row]) + '|'))

    print(line(n))

def graphColoring(n, nodes, colored = 0):
    if colored == 0:
        for i in range(n):
            nodes[i][n] = 0
            flag = graphColoring(n, nodes, 1)
            if flag:
                return True
            else:
                s[i][n] = '-1'
        return False
    else:
        if colored == n:
            return True
        
        else:
            for col in nodes[colored]:
                pass
            return False


if __name__ == "__main__":
    n = 5
    print(n)
    s = [[0 for r in range(n)] for c in range(n)]

    # settings all the connctions
    s[0][1] = 1
    s[0][3] = 1
    s[0].append(' ')
    s[1][0] = 1
    s[1][2] = 1
    s[1][3] = 1
    s[1].append(' ')
    s[2][1] = 1
    s[2][3] = 1
    s[2][4] = 1
    s[2].append(' ')
    s[3][0] = 1
    s[3][1] = 1
    s[3][2] = 1
    s[3][4] = 1
    s[3].append(' ')
    s[4][2] = 1
    s[4][3] = 1
    s[4].append(' ')
    printBoard(n, s)
