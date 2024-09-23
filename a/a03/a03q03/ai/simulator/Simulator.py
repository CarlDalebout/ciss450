"""
The Simulator is responsible for "running" the agents or objects, i.e., it
provides a time slice to each agent/object to run. Right now there's no way
to enforce strict timing, i.e., if dt is allocated to an agent, the simulator
does not halt the agent. I.e., right now, the simulator handles the
sequencing of agent/object processes.

Note that the timer/clock and GUI is also also a runnable object.

GUI: Note that GUI can run
1. After the agent has made an action
2. While the agent is thinking

The Simulator stops when the timer/clock reaches a maximum preset value.
TODO: Allows Simulator to stop based on some condition other than time, i.e.,
Simulator.stopped() -> bool
needs to be more general.

Environment:
The role includes:
* Communicates between objects. For instance an agent gets percept through
  the environment.
* An agent sends an action to the environment which modifies the appropriate
  state.
* Should objects be placed in the environment? That's not necessary. But
  might be convenient.


Agent:
* Given an agent, an agent can run (agent.run()). This will do three things:
    1. Run the sensors to get a percept
    2. Think i.e., compute an action
    3. Send action to actuators
  1 and 2 requires the environment. Technically speaking the sensor(s) and
  actuator(s) need the environment.

  Note that the location sensor tells the VC agent which room it's in. Say
  it's in room A. This information can be stored in the VC agent. But it can
  also be a data stored in the environment.

"""


from copy import deepcopy
from view import View
from Clock import Clock
from ClockView import ClockTextView
from EnvironmentView import EnvironmentViewFactory
from Agent import Agent

class Simulator:
    """
    The purpose of the simulator is to feed time slices to the
    agents.
    """
    def __init__(self,
                 env=None,
                 agents=None,
                 maxtime=None,
                 timeslice=None,
                 graphical=False):
        self.env = env
        #self.clock = Clock(maxtime=maxtime, timeslice=timeslice) # Should clock be in the env?
        #self.clock_view = ClockTextView(self.clock) 
        self.env_view = EnvironmentViewFactory(env).run()
        self.graphical = graphical
    def run(self):
        while not self.clock.stopped():
            pass
            self.clock.run()
