# File: main.py
# Directory: ciss450/a/a01/a01q07
# Author: Carl Dalebout

def floatrange(start = None, end = None, itorator = None):

    pass    

if __name__ == '__main__':
    
    print(floatrange(5))            #returns [0.0, 1.0, 2.0, 3.0, 4.0]
    print(floatrange(2, 5))         #returns [2.0, 3.0, 4.0]
    print(floatrange(1, 1))         #returns []
    print(floatrange(1, 2, 1))      #returns [1.0]
    print(floatrange(1, 2, 0.5))    #returns [1.0, 1.5]
    print(floatrange(1, 2, 1.5))    #returns [1.0]
    print(floatrange(-2, 2, 0.5))   #returns [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
