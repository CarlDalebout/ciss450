import sys;
sys.path.append('../')
import GLOBALS
sys.path.append('../ai/')

import agent
import agent.Agent

class VacuumCleanerRobot(agent.Agent.Agent):

    def __init__(self,
                 name='?',
                 state=None,
                 brain=None):
        agent.Agent.Agent.__init__(self,
                                   name=name,
                                   state=state,
                                   brain=brain)
        VacuumCleanerRobot.check(state)
        print("VacummCleanerRobot constructor")
        
    @staticmethod
    def check(state):
        pass # WARNING: NO CHECK
        #if isinstance(state, VacuumCleanerRobotState)
        #    raise ValueError("Invalid value %s" (state))

if __name__ == '__main__':
    name = 'a'
    for x in GLOBALS.ROOMS:
        VacuumCleanerRobot(name=name, state=x)
        name = chr(ord(name) + 1)
        print("pass")
    for x in [1,2,3]:
        try:
            VacuumCleanerRobot(name=name, state=x)
            name = chr(ord(name) + 1)
            print("FAIL")
        except:
            print("pass")
