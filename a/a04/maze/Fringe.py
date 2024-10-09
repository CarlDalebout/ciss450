"""
Fringe is the base class if fringe subclasses.
    - put, get
    - membership (i.e., __contains__)
    - find and update (later for search such as UCS and heuristic)
    - size
    - __len__ (similar to size)
    - __iter__ (for iteration in a for-loop. This is already done for you.)

A complete Stack and Queue class is provided. However membership check (i.e.
__contains__) is very slow. Therefore we have the following classes:

FSStack and FSQueue

A FSStack object contains a stack and a set. They contain the same values.
The set is used for find membership fast (with O(1) runtime). This is also
the same for FSQueue.
"""

import collections


class Fringe(object):
    def __init__(self):
        object.__init__(self)
    def put(self, x):
        raise NotImplementedError
    def get(self, x):
        raise NotImplementedError
    def __contains__(self):
        raise NotImplementedError
    def size(self):
        raise NotImplementedError
    def __len__(self):
        return 0 # Must be overwritten
    def __contains__(self, x):
        raise NotImplementedError
    def __iter__(self):
        raise NotImplementedError
 
    
class Stack(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        self.deque = collections.deque()
    def put(self, node):
        if node.state not in [n.state for n in self.deque]:
            self.deque.append(node)
    def get(self):
        return self.deque.pop()
    def __len__(self):
        return len(self.deque)
    def size(self):
        return len(self.deque)
    def __contains__(self, node):
        for n in self.deque:
            if node.state == n.state:
                return True
        return False
    def __str__(self):
        s = str(self.deque)[7:-2]
        return '<Stack [%s]>' % s
    def __iter__(self):
        return iter(self.deque)

class FSStack(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        self.stack = collections.deque()
        self.set = set()
    def put(self, node):
        if node.state not in self.set:
            # print ('\"' + str(node.state) + '\"')
            self.set.add(str(node.state))
            self.stack.append(node)
    def get(self):
        ret = self.stack.pop()
        # print(f"!!!{ret.state}!!! {type(ret.state)}")
        self.set.remove(str(ret.state))
        return ret
    def __len__(self):
        return len(self.stack)
    def size(self):
        return len(self.stack)
    def __contains__(self, node):
        return str(node.state) in self.set
    def __str__(self):
        s = str(self.stack)[7:-2]
        return '<Stack [%s]>' % s
    def __iter__(self):
        return iter(self.stack)
    
class Queue(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        self.deque = collections.deque()
    def put(self, x):
        self.deque.append(x)
    def get(self):
        return self.deque.popleft()
    def __len__(self):
        return len(self.deque)
    def size(self):
        return len(self.deque)
    def __contains__(self, node):
        for n in self.deque:
            if node.state == n.state:
                return True
        return False
    def __str__(self):
        s = str(self.deque)[7:-2]
        return '<Queue [%s]>' % s
    def __iter__(self):
        return iter(self.deque)
    
class FSQueue(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        self.queue = collections.deque()
        self.set = set()
    def put(self, node):
        if node.state not in self.set:
            # print ('\"' + str(node.state) + '\"')
            self.set.add(str(node.state))
            self.queue.append(node)
    def get(self):
        ret = self.queue.popleft()
        # print(f"!!!{ret.state}!!! {type(ret.state)}")
        self.set.remove(str(ret.state))
        return ret
    def __len__(self):
        return len(self.queue)
    def size(self):
        return len(self.queue)
    def __contains__(self, node):
        return str(node.state) in self.set
    def __str__(self):
        s = str(self.queue)[7:-2]
        return '<queue [%s]>' % s
    def __iter__(self):
        return iter(self.queue)

if __name__ == '__main__':
    from SearchNode import SearchNode
    print("Testing fringe with search nodes from (0,0) -> (1,0) -> (1,1) by actions ['E', 'S']")
    fringe = FSQueue()
    state00 = (0, 0)
    node00 = SearchNode(state00)
    state01 = (0, 1)
    node01 = SearchNode(state01, node00, 'E', 1)
    state11 = (1, 1)
    node11 = SearchNode(state11, node01, 'S', 1)
    print(node00)
    print(node01)
    print(node11)
    print()

    print(fringe)
    fringe.put(node00)
    print(node00 in fringe)
    print(node01 in fringe)
    print(node11 in fringe)
    print()
    
    print(fringe)
    fringe.put(node01)
    print(node00 in fringe)
    print(node01 in fringe)
    print(node11 in fringe)
    print()

    print(fringe)
    fringe.put(node11)
    print(node00 in fringe)
    print(node01 in fringe)
    print(node11 in fringe)
    print()

    print(fringe)
    n = fringe.get()
    print(n)
    print(node00 in fringe)
    print(node01 in fringe)
    print(node11 in fringe)
    print()

    print(fringe)
    n = fringe.get()
    print(n)
    print(node00 in fringe)
    print(node01 in fringe)
    print(node11 in fringe)
    print()
    
    print(fringe)
    n = fringe.get()
    print(n)
    print(node00 in fringe)
    print(node01 in fringe)
    print(node11 in fringe)
    print()

    print(fringe)
    try:    
        n = fringe.get()
        print(n)
    except IndexError:
        print("stack fringe is empty ... cannot get()")
    print(node00 in fringe)
    print(node01 in fringe)
    print(node11 in fringe)
    print()
    
