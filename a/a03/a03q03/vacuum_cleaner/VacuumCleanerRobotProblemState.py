import sys;
sys.path.append('../ai/')
sys.path.append('../')
from GLOBALS import *
from agent.State import State
from vacuum_cleaner.VacuumCleanerRobotState import VacuumCleanerRobotState
from vacuum_cleaner.RoomState import RoomState

class VacuumCleanerRobotProblemState(State):
    def __init__(self, value):
        # value = (a,b) where a is an VacuumCleanerRobotState,
        # b is a RoomState
        State.__init__(self, value)
        VacuumCleanerRobotProblemState.check(value)
        self.value = value
        
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
        room = str(agent_state)
        print(agent_state , f"!!!!{type(room)}!!!!!!")
        if action == 'Suck':
            new_room_state = RoomState('Clean')
            return VacuumCleanerRobotProblemState((agent_state, \
                                                   new_room_state))
        elif action == 'Left':
            print(f"\n\n\n{self.value}\n\n\n")
            new_agent_state = VacuumCleanerRobotState(chr(ord(room) - 1))
            return VacuumCleanerRobotProblemState((new_agent_state, \
                                                   room_state))
        elif action == 'Right': 
            print(f"\n\n\n{self.value}\n\n\n")
            new_agent_state = VacuumCleanerRobotState(chr(ord(room) + 1))
            return VacuumCleanerRobotProblemState((new_agent_state, room_state))
