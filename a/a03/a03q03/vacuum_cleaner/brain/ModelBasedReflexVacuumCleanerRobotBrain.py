import sys
sys.path.append('../../')
from GLOBALS import ACTIONS
from ai.brain.ModelReflexBrain import ModelReflexBrain

class ModelBasedReflexVacuumCleanerRobotBrain(ModelReflexBrain):
    def __init__(self):
        ModelReflexBrain.__init__(self, actions = ACTIONS)

if __name__ == '__main__':
    brain = ModelBasedReflexVacuumCleanerRobotBrain()
    print(brain.run("A", "Clean"))
    print(brain.run("A", "Dirty"))
    print(brain.run("B", "Clean"))
    print(brain.run("B", "Dirty"))