# File: main.py
# Dir: a/a02/a02q01 
# Author: Carl Dalebout

import DLList

if __name__ == '__main__':
    xs = DLList.DLList(); print(xs.head, xs, xs.tail, len(xs), xs.is_empty())
    xs.insert_head(5); print(xs.head, xs, xs.tail, len(xs), xs.is_empty())
    xs.insert_head(2); print(xs.head, xs, xs.tail, len(xs), xs.is_empty())
    xs.insert_tail(6); print(xs.head, xs, len(xs), xs.is_empty())
    xs.head = 1234; print(xs.head, xs, xs.tail, len(xs), xs.is_empty())
    xs.tail = 5678; print(xs.head, xs, xs.tail, len(xs), xs.is_empty())
    x = xs.delete_head()
    print(x)
    print(xs.head, xs, xs.tail, len(xs), xs.is_empty())
    x = xs.delete_tail()
    print(x)
    print(xs.head, xs, xs.tail, len(xs), xs.is_empty())