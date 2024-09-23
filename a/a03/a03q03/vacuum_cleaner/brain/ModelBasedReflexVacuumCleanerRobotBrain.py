import sys
sys.path.append('../../')
from GLOBALS import ACTIONS
from ai.brain.ModelBasedBrain import ModelBasedBrain

class ModelBasedReflexVacuumCleanerRobotBrain(ModelBasedBrain):
    def __init__(self):
        ModelBasedBrain.__init__(self, actions = ACTIONS)

if __name__ == '__main__':
    brain = ModelBasedReflexVacuumCleanerRobotBrain()
    print(brain.run({'location': 'A', 'room_status': "Clean"}))
    print(brain.run({'location': 'A', 'room_status': "Dirty"}))
    print(brain.run({'location': 'B', 'room_status': "Clean"}))
    print(brain.run({'location': 'B', 'room_status': "Dirty"}))
    print(brain.run({'location': 'C', 'room_status': "Clean"}))
    print(brain.run({'location': 'C', 'room_status': "Dirty"}))
    print(brain.run({'location': 'D', 'room_status': "Clean"}))
    print(brain.run({'location': 'D', 'room_status': "Dirty"}))
