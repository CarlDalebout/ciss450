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
    def put(self, x):
        pass
    def __contains__(self, x):
        return False
    def size(self):
        return 0
    def __len__(self):
        return 0
    def __str__(self):
        return "<DummyClosedList {}>"
    def values(self):
        return []
    def __iter__(self):
        return iter([])
    def clear(self):
        return


class SetClosedList(ClosedList):
    """ Implementation of ClosedList using python sets """
    def __init__(self):
        ClosedList.__init__(self)
        self.xs = set()
    def put(self, x):
        self.xs.add(x)
    def __contains__(self, x):
        return x in self.xs
    def size(self):
        return len(self.xs)
    def __len__(self):
        return len(self.xs)
    def __str__(self):
        s = str(self.xs)[5:-2]
        return "<SetClosedList {%s}>" % s
    def values(self):
        return self.xs
    def __iter__(self):
        return iter(self.xs)
    def clear(self):
        self.xs.clear()

        
class SetClosedListWithCompression(ClosedList):
    """ Implementation of ClosedList using python sets and with state compression"""
    def __init__(self, compress=lambda x:x, decompress=lambda x:x):
        """
        compress -- a function to compress state
        decompress -- inverse function of compress
        """
        ClosedList.__init__(self)
        self.xs = set()
        self.compress = compress
        self.decompress = decompress
    def put(self, x):
        x = self.compress(x)
        self.xs.add(x)
    def __contains__(self, x):
        x = self.compress(x)
        return x in self.xs
    def size(self):
        return len(self.xs)
    def __len__(self):
        return len(self.xs)
    def __str__(self):
        s = str(self.xs)[5:-2]
        return "<SetClosedListWithCompression {%s}>" % s
    def values(self):
        f = self.decompress
        return [f(x) for x in self.xs]    
    def __iter__(self):
        for x in self.xs:
            yield f(x)
        raise StopIteration
    def clear(self):
        self.xs.clear()

        
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
    
    def compress(x):
        # x is a 3-tuple of 32-but unsigned int
        a,b,c = x
        return ((a << 64) + (b << 32) + c)
    def decompress(x):
        a, b, c = (x>>64 & 0xffffffff, (x >> 32) & 0xffffffff, x & 0xffffffff)
        return (int(a), int(b), int(c))

    x = (1, 2, 3)
    print("x:", x)
    print("compress(x):", compress(x))
    print("decompress(compress(x)):", decompress(compress(x)))
