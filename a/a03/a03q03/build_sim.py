import sys
sys.path.append('ai')
sys.path.append('Views')
sys.path.append('brain')
sys.path.append('simulator')
sys.path.append('vacuum_cleaner')

import random
seed = input("random seed: ")
random.seed(seed)

from GLOBALS import *
from vacuum_cleaner.VacuumCleanerRobot import VacuumCleanerRobot
from vacuum_cleaner.VacuumCleanerRobotState import VacuumCleanerRobotState
from vacuum_cleaner.brain.VacuumCleanerRobotRandomBrain \
     import VacuumCleanerRobotRandomBrain
from vacuum_cleaner.brain.SimpleReflexVacuumCleanerRobotBrain \
     import SimpleReflexVacuumCleanerRobotBrain
from vacuum_cleaner.brain.ModelBasedReflexVacuumCleanerRobotBrain \
     import ModelBasedReflexVacuumCleanerRobotBrain
from vacuum_cleaner.Room import Room
from vacuum_cleaner.Clock import Clock
from VacuumCleanerRobotEnvironment import VacuumCleanerRobotEnvironment
from simulator.DiscreteSimulator import DiscreteSimulator
import Agent

def build_sim(steps,
              room_states,
              agent_data,
              graphical):
    
    env = VacuumCleanerRobotEnvironment()
    
    clock = Clock(maxtime=steps)
    env.add(clock)

    for room_name, room_state in zip(ROOMS, room_states):
        room = Room(room_name, room_state)
        env.add(room)

    for (name, brain_type, location) in agent_data:
        if brain_type == 0:
            brain = VacuumCleanerRobotRandomBrain()
        elif brain_type == 1:
            brain = SimpleReflexVacuumCleanerRobotBrain()
        elif brain_type == 2:
            brain = ModelBasedReflexVacuumCleanerRobotBrain()
        agent = VacuumCleanerRobot(name=name,
                                   state=VacuumCleanerRobotState(location),
                                   brain=brain)
        env.add(agent)
    
    sim = DiscreteSimulator(env=env,
                            graphical=graphical)

    return sim
