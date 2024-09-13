# File: main.py
# Dir: a/a02/a02q01 
# Author: Carl Dalebout

import DLList
import DLNode


if __name__ == '__main__':
    xs = [1,2,3]
    ys = [3,2,1]
    a = DLList.DLList(xs)
    b = DLList.DLList(ys)

    print(len(a))
    print(a.head)
    print(a.get_list())