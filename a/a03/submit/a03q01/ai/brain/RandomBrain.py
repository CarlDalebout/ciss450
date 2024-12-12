import random
from Brain import Brain

class RandomBrain(Brain):
    def __init__(self, actions=None):
        Brain.__init__(self)
        if actions == None: actions = []
        self.actions = actions
    def run(self, percept):
        ret = random.choice(self.actions)
        return ret
    def __str__(self):
        return "<RandomBrain %s %s>" % (id(self), self.actions)

if __name__ == '__main__':
    print("Testing RandomBrain")
    b = RandomBrain([1,2,3])
    print(b)
