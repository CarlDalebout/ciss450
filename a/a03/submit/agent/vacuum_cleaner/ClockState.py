import sys;
sys.path.append('../ai')
import agent.State

class ClockState(agent.State.State):
    def __init__(self, value):
        agent.State.State.__init__(self, value)
        ClockState.check(value)
        
    @staticmethod
    def check(value):
        if not isinstance(value, int):
            raise Exception("Invalid value %s" % value)
