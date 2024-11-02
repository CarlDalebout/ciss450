class State:
    def __init__(self):
        pass

class MazeState(State):
    def __init__(self, (r, c)=(0, 0)):
        State.__init__(self)
        self.value = (r, c)

    def __hash__(self):
        return self.value[0] * 1000 + self.value[1]

