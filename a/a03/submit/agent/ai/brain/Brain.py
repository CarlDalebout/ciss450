class Brain:
    def __init__(self):
        pass
    def run(self, percept):
        pass
    def __str__(self):
        return "<Brain %s>" % id(self)

if __name__ == '__main__':
    print("Testing Brain")
    b = Brain()
    print(b)
