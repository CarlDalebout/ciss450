import sys; sys.path.append('..')
from ai import Object

class Agent(Object):

    def __init__(self,
                 name='?',
                 state='A',
                 brain=None):
        Object.__init__(self,
                        name=name,
                        state=state)
        self.is_agent = True
        self.brain = brain
        
        # NEW -- redundant. The following are not used.
        self.sensors = {}
        self.actuators = {}
        
        self.percept = None # percept received from Environment (in sensor)
        self.action = None # action returned (in actuator)

    def run(self, percept):
        self.percept = percept
        self.action = self.brain.run(self.percept)
        return self.action

    def clear(self):
        """ Sets self.action and self.percept to None """
        self.percept = None
        self.action = None

if __name__ == '__main__':
    pass