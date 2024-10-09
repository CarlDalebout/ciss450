def pause():
    input("\nenter to continue ... "); print()

print()
print("""0 ...
When printing a dictionary, for a (key,value), the repr for both are used. This is the same for sets since python sets are implemented using dictionaries.
(Remember: python sets are implemented using dictionaries. For C++ hashtables are std::unordered_map and sets are std::unodered_set which are balanced trees.)
""")

class X:
    def __init__(self):
        pass
    def __str__(self):
        return "__str__"
    def __repr__(self):
        return "__repr__"
d = {}
d[0] = "a"
d[1] = X()
d[X()] = 'b'
print("d:", d)
s = set()
s.add(X())
print("s:", s)
pause()

print("""1 ...
When using your objects as keys in a dictionary, the id of the object is used as the hashing. This is the same for a set. Also, see below ...
""")

x = X()
d = {}
d[x] = 'b'
d[id(x)] = 'd' # proves that d[x] is the same as d[id(x)]
print("d:", d)
print(id(x))
s = set()
s.add(x)
print("s:", s)
s.add(x) # no change in s
print("s:", s)
s.add(X()) # s is now changed. why? think pointers.
print("s:", s)

pause()

print("""2 ...
When using your objects as keys in a dictionary (or set), you can write your own hash. As usual python dictionary uses separate chaining (see 350). So a (k,v) is hashed to a linked list. To check if (k,v) is in this linked list, the k is compared against other keys in this linked list using is __eq__ of k. Note that by default __eq__ for a class compares using id.""")

class X:
    def __init__(self, a):
        self.a = a
    def __hash__(self):
        return hash(self.a)
    def __str__(self):
        return "<X id:%s a:%s, hash:%s>" % (id(self), self.a, hash(self))
    def __repr__(self):
        return str(self)

d = {}
d[X(1)] = 'a'
d[X(1)] = 'b' # this X(1) is *different* from previous X(1) (different id).
print("d:", d)
print(X(1)==X(1)) # compares using id

s = set()
x = X(1)
s.add(x)
print("s:", s)
s.add(x) # x *not* added
print("s:", s)
s.add(X(1)) # this X(1) *is* added
print("s:", s)

pause()

print("""3 ...
When using your objects as keys in a dictionary (or set),
(1) you can write your own hash (avoid id) to hash into a linked list, and
(2) you can write your own __eq__ (avoid id) for comparison inside the linked list.
""")

class X:
    def __init__(self, a):
        self.a = a
    def __hash__(self):
        return hash(self.a)
    def __eq__(self, x): # <<<< NEW
        return isinstance(x, X) and hash(self) == hash(x)
    def __str__(self):
        return "<X id:%s a:%s, hash:%s>" % (id(self), self.a, hash(self))
    def __repr__(self):
        return str(self)

d = {}
d[X(1)] = 'a'
d[X(1)] = 'b' # this X(1) is *same* as previous X(1)
print("d:", d)
print(X(1)==X(1)) # compares using hash

s = set()
x = X(1)
s.add(x)
print("s:", s)
s.add(x) # x *not* added
print("s:", s)
s.add(X(1)) # this X(1) *not* added
print("s:", s)

pause()

print("""4 ...
In general if you want things/objects to be uniquely determined by their *appearances* (based on the values of their instance variables), you use these values as your hash and __eq__.

At other times you want to define uniqueness based on something called "object identity". For instance it's possible to have two John Does to look exactly the same but are two different people. In that case you want to differentiate between them based on the space they are standing on.

In the case of states of an AI search algorithm, you might want the state to be determined by their appearances. So there's only one "(2, 3)". Of course in your system there might be a thousand objects that look like "(2, 3)", which is a waste of space. One way to prevent that is to create states through a function F. The function maintains a pool of states. If you call F(2, 3), it either returns the pointer to an existing "(2, 3)" that it maintains, or it creates one and then return its address. So in this case "(2, 3)" is in fact uniquely determined by it's id. This F is usually implemented as an object, something like

class State:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        # other stuff

class StateCreator:
    def __init__(self):
        self.pool = {}
    def get(self, r, c):
        if (r, c) not in self.pool:
            self.pool[(r, c)] = State(r, c)
        return self.pool[(r, c)]

statefactory = StateCreator()

a = statefactory.get(2, 3)
b = statefactory.get(2, 3)
print(id(a), id(b))
d = {}
d[a] = 'ham'
print(d)
d[b] = 'eggs'
print(d)
        
""")
