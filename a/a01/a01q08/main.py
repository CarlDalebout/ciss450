# File: main.py
# Directory: ciss450/a/a01/a01q07
# Author: Carl Dalebout

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

# f function here
def f(list):
    ret = []
    edge = []
    for i in range(len(list)-1):
        edge.append(list[i])
        edge.append(list[i+1])
        ret.append(edge)
        edge = []
    return ret

# g function here
def g(list):
    ret = []
    ret.append(list[0][0])
    for i in range(0, len(list)):
        ret.append(list[i][1])
    return ret

if __name__ == '__main__':
    option = int(input())
    if option == 1:         # test f
        s = input()         # enter "a,b,c,d,e" (without double-quotes)
        xs = s.split(",")   # xs is ["a", "b", "c", "d", "e"]
        print(f(xs))
    else:                   # test g
        s = input()         # enter "a,b,b,c,c,d,d,e" (without double-quotes)
        xs = matrix(2,s)    # xs is [["a","b"],["b","c"],["c", "d"],["d", "e"]]
        print(g(xs))
