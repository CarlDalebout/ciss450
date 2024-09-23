import sys; sys.path.append('..')
from vacuum_cleaner.RoomState import RoomState
from vacuum_cleaner.VacuumCleanerRobotState import VacuumCleanerRobotState
from vacuum_cleaner.VacuumCleanerRobotProblemState \
     import VacuumCleanerRobotProblemState

class VacuumCleanerRobotProblem:
    def __init__(self):
        pass
    def result(self, state, action):
        return state.result(action)
        """
        agent_state, room_state = state.value 
        if action == 'Suck':
            new_room_state = RoomState('Clean')
            return VacuumCleanerRobotProblemState((agent_state, \
                                                   new_room_state))
        elif action == 'Left':
            new_agent_state = VacuumCleanerRobotState('A')
            return VacuumCleanerRobotProblemState((new_agent_state, \
                                                   room_state))
        elif action == 'Right': 
            new_agent_state = VacuumCleanerRobotState('B')
            return VacuumCleanerRobotProblemState((new_agent_state, room_state))
        """
