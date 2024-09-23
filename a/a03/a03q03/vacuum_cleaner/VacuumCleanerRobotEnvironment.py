import sys; sys.path.append('..')
from GLOBALS import *
import vacuum_cleaner.Room
import agent.Environment
from vacuum_cleaner.VacuumCleanerRobotProblem import VacuumCleanerRobotProblem
from vacuum_cleaner.VacuumCleanerRobotProblemState \
     import VacuumCleanerRobotProblemState

class VacuumCleanerRobotEnvironment(agent.Environment.Environment):
    
    def __init__(self,
                 objs=None,
                 object_states=None,
                 ):
        agent.Environment.Environment.__init__(self, objs)

    def room_relation(self, agent):
        # Relation:
        # Returns room object such that agent is in that room
        #print("room_relation ...")
        for obj in self.objs:
            #print("obj:", obj)
            if isinstance(obj, vacuum_cleaner.Room.Room) and \
                   obj.name == agent.state.value:
                #print(agent, "in", obj)
                return obj
        raise Exception("ERROR: agent %s not in any room" % agent)
        
    def get_percept(self, agent):
        #----------------------------------------------------------------------
        # Tell robot the state of the room he is in.
        # 1. First find the room.
        #.2. Get the state of the room.
        #----------------------------------------------------------------------
        room = self.room_relation(agent)
            
        return {'location':agent.state.value,
                'room_status':room.state.value}

    def act(self, agent, action):
        room = self.room_relation(agent)

        # Compute new problem state
        problem = VacuumCleanerRobotProblem()
        print(f"\n\n\n{agent.state}\n\n\n")
        problem_state = VacuumCleanerRobotProblemState((agent.state, \
                                                        room.state))
        new_problem_state = problem.result(problem_state, action)

        # Modify agent and room state
        (new_agent_state, new_room_state) = new_problem_state.value
        agent.state.value = new_agent_state.value
        room.state.value = new_room_state.value
        
