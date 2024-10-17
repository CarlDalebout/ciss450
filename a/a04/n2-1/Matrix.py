# File: Matrix.py
# Directory: ccis450/a/a04/n2-1
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
