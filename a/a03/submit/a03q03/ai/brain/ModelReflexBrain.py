from GLOBALS import *
from Brain import Brain

class ModelReflexBrain(Brain):
    def __init__(self, actions=None):
        Brain.__init__(self)
        if actions == None: actions = []
        self.actions = actions
        self.i = 0
    
    def run(self, percept):
        print(f'!!!{self.i}!!!')
        if percept['room_status'] == 'Dirty':
            return 'Suck'
        elif percept['location'] == ROOMS[0]:
            self.i = 1
            return 'Right'
        elif percept['location'] == ROOMS[-1]:
            self.i = 0
            return 'Left'
        else:
            if self.i == 1: return 'Right'
            else: return 'Left'
        
    def __str__(self):
        return "<ModelReflexBrain %s %s>" % (id(self), self.actions)

if __name__ == '__main__':
    print("Testing ModelReflexBrain")
    b = ModelReflexBrain([1,2,3])
    print(b)
