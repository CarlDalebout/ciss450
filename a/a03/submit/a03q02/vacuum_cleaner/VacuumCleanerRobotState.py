import sys
sys.path.append('../')
sys.path.append('../ai/')
import agent.State 
import GLOBALS

class VacuumCleanerRobotState(agent.State.State):
    def __init__(self, value):
        agent.State.State.__init__(self, value)
        VacuumCleanerRobotState.check(value)
        
    @staticmethod
    def check(value):
        #print('WARNING: NO CHECK IN VACUUMCLEANERSTATE')
        if value not in GLOBALS.ROOMS:
            raise ValueError("Invalid value %s" % value)


if __name__ == '__main__':
    pass
