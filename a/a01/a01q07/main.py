# File: main.py
# Directory: ciss450/a/a01/a01q07
# Author: Carl Dalebout

def floatrange(start = None, end = None, itorator = None):
    
    ret = []
    
    if end == None and itorator == None:
        i = 0.0
        while i < start:
            ret.append(float(i))
            i += 1.0
    
    elif itorator == None:
        while start < end:
            ret.append(float(start))
            start += 1.0

    else:
        while start < end:
            ret.append(float(start))
            start += itorator
            
    return ret

if __name__ == '__main__':
    
    a = float(input())
    b = input() # enter "" (w/o quotes) for default b and c
    c = input() # enter "" (w/o quotes) for default c
    if b == '':
        print(floatrange(start=a))
    else:
        b = float(b)
        if c == '':
            print(floatrange(start=a, end=b))
        else:
            c = float(c)
            print(floatrange(start=a, end=b, itorator=c))