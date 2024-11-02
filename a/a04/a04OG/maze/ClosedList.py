"""
COMPLETE DummyClosedList and SetClosedList.

- CloseList: Base class for closed lists.
  Let c be a closed list.
  - c.put(x): puts x into the closed list c
  - x in c:   return True iff x is in c. Note: x in c is the same as c.__contains__(x)
  - c.size(): number of values in c
  - len(c):   same as c.size(). Note: len(c) is the same as c.__len__())
  - values(): Returns the values in the closed list.
  - clear():  Clear the values in the closed list.
  Subclasses of ClosedList must implement the above methods.

The following are two subclasses of CloseList:
- DummyClosedList: The closed list modeled is always empty.
- SetClosedList: The closed list is modeled using a python set.

Note that the values() method is actually not used in the graph search
algorithm. It is included here only because it is used in the graphical
animation. If this returns a list, then it is very memory inefficient.

"""

class ClosedList(object):
    def __init__(self):
        object.__init__(self)
    def put(self, x):
        """ Put x into closed list """
        raise NotImplementedError
    def __contains__(self, x):
        """ Implements "in" operator to check is x is in the closed list """
        raise NotImplementedError
    def size(self):
        """ Returns the number of values in the closed list """
        raise NotImplementedError
    def __len__(self):
        """ Returns the number of values in the closed list """
        return 0 # Must be overwritten
    def values(self):
        raise NotImplementedError
    def __iter__(self):
        raise NotImplementedError
    def clear(self):
        raise NotImplementedError


class DummyClosedList(ClosedList):
    def __init__(self):
        ClosedList.__init__(self)
    def __len__(self):
        return 0
    def __str__(self):
        return "<DummyClosedList {}>"
    def values(self):
        return []


class SetClosedList(ClosedList):
    """ Implementation of ClosedList using python sets """
    def __init__(self):
        ClosedList.__init__(self)
        self.xs = set()
    def __str__(self):
        return "<SetClosedList {}>"
    def values(self):
        return self.xs

if __name__ == '__main__':
    closed = SetClosedList()
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))

    closed.put(4)
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))

    closed.put(3)
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))

    closed.put(3)
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))
    
    closed = DummyClosedList()
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))

    closed.put(4)
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))

    closed.put(3)
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))

    closed.put(3)
    print(closed)
    print(3 in closed)
    print(4 in closed)
    print(len(closed))
    
