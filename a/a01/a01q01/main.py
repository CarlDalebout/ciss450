# File: main.py
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

if __name__ == '__main__':
    n = int(input())    # for instance enter 3
    s = input()         # for instance enter "a,b,c,d,e,f,g,h,i"
                        # (without quotes)
    separator = input() # for instance enter "," (without quotes)
                        # or enter "" (without quotes) for default case
    if separator == '':
        print(matrix(n, s))
    else:
        print(matrix(n, s, separator))
