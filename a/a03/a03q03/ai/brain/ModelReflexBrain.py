from Brain import Brain

class ModelReflexBrain(Brain):
    def __init__(self, actions=None):
        Brain.__init__(self)
        if actions == None: actions = []
        self.actions = actions
        self.i = 0
    
    def run(self, percept):
        print(percept)
        if percept['room_status'] == 'Dirty':
            return 'Suck'
        elif percept['location'] == 'A':
            self.i = 1
            return 'Right'
        elif percept['location'] == 'B':
            if self.i == 1: return 'Right'
            else: return 'Left'
        elif percept['location'] == 'C':
            if self.i == 1: return 'Left'
            else: return 'Right'
        else:
            self.i = 1
            return 'Left'
        
    def __str__(self):
        return "<ModelReflexBrain %s %s>" % (id(self), self.actions)

if __name__ == '__main__':
    print("Testing ModelReflexBrain")
    b = ModelReflexBrain([1,2,3])
    print(b)
