import sys
sys.path.append('../../')
from GLOBALS import ACTIONS
from ai.brain.SimplyBrain import SimpleBrain

class SimpleReflexVacuumCleanerRobotBrain(SimpleBrain):
    def __init__(self):
        SimpleBrain.__init__(self, actions = ACTIONS)

if __name__ == '__main__':
    brain = SimpleReflexVacuumCleanerRobotBrain()
    print(brain.run("A", "Clean"))
    print(brain.run("A", "Dirty"))
    print(brain.run("B", "Clean"))
    print(brain.run("B", "Dirty"))