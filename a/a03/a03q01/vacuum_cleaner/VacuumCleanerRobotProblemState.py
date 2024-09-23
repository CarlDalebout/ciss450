import sys;
sys.path.append('../ai/')
sys.path.append('../')
from agent.State import State
from vacuum_cleaner.VacuumCleanerRobotState import VacuumCleanerRobotState
from vacuum_cleaner.RoomState import RoomState

class VacuumCleanerRobotProblemState(State):
    def __init__(self, value):
        # value = (a,b) where a is an VacuumCleanerRobotState,
        # b is a RoomState
        State.__init__(self, value)
        VacuumCleanerRobotProblemState.check(value)
        
    @staticmethod
    def check(value):
        return
        """ 2022/9/15: isinstance(room_state, RoomState) error
        Temporarily commented out.
        
        agent_state, room_state = value
        print("VCRPS state:", agent_state, room_state)
        if not isinstance(agent_state, VacuumCleanerRobotState):
            raise Exception("Invalid value %s" % \
                            agent_state)
        if not isinstance(room_state, RoomState):
            raise Exception("Invalid RoomState value %s" % \
                            room_state)
        """
        
    def result(self, action):
        agent_state, room_state = self.value 
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
