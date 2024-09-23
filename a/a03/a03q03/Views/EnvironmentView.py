import sys; sys.path.append('..')
import agent.Agent
import vacuum_cleaner.Room
import vacuum_cleaner.Clock

from ObjectView import RoomTextView
from ObjectView import AgentTextView
from ObjectView import ClockTextView


class EnvironmentViewFactory:
    def __init__(self, env, param='text'):
        self.env = env
        self.param = param
    def run(self):
        # hardcoding for now
        factory = {'text':{'Agent':AgentTextView,
                           'Room':RoomTextView,
                           'Clock':ClockTextView,
                           'Environment':EnvironmentTextView},
                     }
        env = self.env
        param = self.param
        views = []
        for obj in env.objs:
            kind = None
            #print("Agent:", Agent)
            #print("Room:", vacuum_cleaner.Room.Room)
            #print("Clock:", vacuum_cleaner.Clock.Clock)
            if isinstance(obj, agent.Agent.Agent):
                kind = 'Agent'
            elif isinstance(obj, vacuum_cleaner.Room.Room):
                kind = 'Room'
            elif isinstance(obj, vacuum_cleaner.Clock.Clock):
                kind = 'Clock'
            #print("kind:", kind)
            view = factory[param][kind](obj)
            views.append(view)
        return factory[param]['Environment'](views)
        
class EnvironmentView:
    def __init__(self, views):
        #print("EnvironemntView")
        self.views = views


class EnvironmentTextView(EnvironmentView):
    """
    This is a view of not one model, but a collection of
    models.
    """
    def __init__(self, views):
        EnvironmentView.__init__(self, views)
        self.buffer = ""
    def run0(self):
        s = ', '.join([v.run() for v in self.views])
        return "environment: %s" % s
    def run(self, __agent=None): # Name __agent since agent is package
        if __agent==None:
            print('\n%s' % self.run0())
        else:
            if not isinstance(__agent, agent.Agent.Agent):
                raise "Not an agent"
            s = "running agent %s ...\n" % __agent.name
            s += "percept    : %s\n" % __agent.percept
            s += "action     : %s\n" % __agent.action
            s += self.run0()
            print(s)
