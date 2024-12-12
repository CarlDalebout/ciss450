from Brain import Brain

class SimpleBrain(Brain):
    def __init__(self, actions=None):
        Brain.__init__(self)
        if actions == None: actions = []
        self.actions = actions
    
    def run(self, percept):
        print(percept)
        if percept['room_status'] == 'Dirty':
            return 'Suck'
        elif percept['location'] == 'A':
            return 'Right'
        else:
            return 'Left'
        
    def __str__(self):
        return "<SimpleBrain %s %s>" % (id(self), self.actions)

if __name__ == '__main__':
    print("Testing SimpleBrain")
    b = SimpleBrain([1,2,3])
    print(b)
