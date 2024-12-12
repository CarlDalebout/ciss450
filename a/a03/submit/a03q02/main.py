import sys
sys.path.append('ai')
sys.path.append('ai/basic')
sys.path.append('ai/brain')
sys.path.append('ai/agent')
sys.path.append('ai/simulator')

from GLOBALS import *
from build_sim import build_sim

steps = int(input('number of time steps: '))

room_states = []
for room_name in ROOMS:
    while 1:
        room_state = input('status of room %s (Clean or Dirty): ' % \
                           room_name)
        if room_state in ['Clean', 'Dirty']:
            break
        else:
            print("Invalid room status")
    room_states.append(room_state)

agent_data = []
while 1:
    name = input('name of agent (return to end): ')
    if name == '': break
    brain_type = int(input('type of brain (0-random): '))
    location = input('location of agent (%s): ' % ' or '.join(ROOMS))
    agent_data.append((name, brain_type, location))

graphical = input('graphical animation? (y/n): ')
graphical = graphical in ['y', 'Y']

sim = build_sim(steps=steps,
                room_states=room_states,
                agent_data=agent_data,
                graphical=graphical)
sim.run()
