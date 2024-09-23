import sys
sys.path.append('../../')
from GLOBALS import ACTIONS
from ai.brain.RandomBrain import RandomBrain

class VacuumCleanerRobotRandomBrain(RandomBrain):
    def __init__(self):
        RandomBrain.__init__(self, actions=ACTIONS)

if __name__ == '__main__':
    brain = VacuumCleanerRobotRandomBrain()
    print(brain.run(None))
    print(brain.run(None))
    print(brain.run(None))
    print(brain.run(None))
