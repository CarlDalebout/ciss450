from copy import deepcopy
from view import View
from Simulator import Simulator

class DiscreteSimulator(Simulator):
    '''
    Action: string that is either 'Left', 'Right', or 'Suck'
    
    Percept: dictionary. Example: {'room_state': 'Clean', 'location': 'A'}
             This tells the agent receiving the percept that the agent is in
             room A and that room is clean.
    '''
    def __init__(self,
                 maxtime=None,
                 agents=None,
                 env=None,
                 graphical=False):
        Simulator.__init__(self,
                           env=env,
                           agents=agents,
                           graphical=graphical)

    def run_agent(self, agent):
        percept = self.env.get_percept(agent)
        action = agent.run(percept)
        self.env.act(agent=agent, action=action)
        return action # TMP: this is only for the sake of graphical display
            
    def run(self):
        
        # WARNING: Note that the agent action is order-dependent
        # on the agents. The first agent in agents list gets to
        # make the first action.
        #print(self.env_view.run())
        self.env_view.run()
        
        if self.graphical:
            v = View(self.env) # graphical-animation view

        clock = self.env.find_first_by_name('clock')        
        while not clock.stopped():
            clock.run()
            self.env_view.run()

            # Run agents
            for obj in self.env.find_agents():
                action = self.run_agent(obj)
                self.env_view.run(obj) # view action of this agent

            if self.graphical:
                env = deepcopy(self.env)
                v.run(env)

        print()
        print("simulator ended")
        if self.graphical:
            input("press enter to end ... ")
