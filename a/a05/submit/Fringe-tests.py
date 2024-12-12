class TestSearchNode:
    def __init__(self, state, pri):
        self.state = state
        self.pri = pri
    def priority(self):
        return self.pri
    def __str__(self):
        return '<%s %s>' % (self.state, self.pri)

n0 = TestSearchNode('a', 8)
n1 = TestSearchNode('b', 7)
n2 = TestSearchNode('c', 4)
n3 = TestSearchNode('d', 2)
n4 = TestSearchNode('e', 6)
n5 = TestSearchNode('f', 1)

ns = [n0, n1, n2, n3, n4, n5]
f = UCSFringe()
print(f)
for n in ns:
    f.put(n)
    print("insert", n, "...", f)

print("Checking fringe ...")
f.check()

print("Testing inserting duplicate state with larger priority")
f.put(TestSearchNode('e',10))
print(f)

print("Testing inserting duplicate state with smaller priority")
f.put(TestSearchNode('e', 0))
print(f)

while len(f) != 0:
    n = f.get()
    print("get", n, "...", f)

