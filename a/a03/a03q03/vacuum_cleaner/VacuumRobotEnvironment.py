from GLOBALS import *
from Environment import *

class VacuumRobotEnvironment(Environment):
    
    def __init__(self,
                 agents=None,
                 locations=None,
                 room_statuses=None
                 ):
        Environment.__init__(self, agents=agents)

        """
        self.state describes the state of things in the environment.
        
        Examople: 
        
              self.state['room']['A']
              
        is the state of room A which is either 'Clean' or 'Dirty'.
        
        Examople: 
        
              self.state['agent'][8000000]['location']
              
        is the location of the agent with id 8000000 (say), which can be
        either 'A' or 'B' and

              self.state['agent'][8000000]['agent']
                      
        is a reference to the agent itself.
        """
        
        if agents == None: agents = []
        
        self.state['room'] = {}
        for room, room_status in zip(ROOMS, room_statuses):
            self.state['room'][room] = room_status

        for agent, location in zip(agents, locations):
            self.state['agent'][id(agent)] = {'agent': agent,
                                              'location': location}

    def get_percept(self, agent):
        location = self.state['agent'][id(agent)]['location']
        room_status = self.state['room'][location]
        return {'location':location, 'room_status':room_status}

    def act(self, agent, action):
        if action == 'Suck':
            location = self.state['agent'][id(agent)]['location']
            self.state['room'][location] = 'Clean'
        elif action == 'Left' and self.state['agent'][id(agent)]['location'] != ROOMS[0]:
            self.state['agent'][id(agent)]['location'] = str(ord(self.state['agent'][id(agent)]['location']) - 1) #current room minus one
        elif action == 'Right' and self.state['agent'][id(agent)]['location'] != ROOMS[-1]:
            self.state['agent'][id(agent)]['location'] = str(ord(self.state['agent'][id(agent)]['location']) + 1) #current room minus one

    def __repr__(self):
        xs = []

        for k,v in self.state['room'].items():
            xs.append('%s: %s' % (k, v))
            
        for k,v in self.state['agent'].items():
            agent, location = v['agent'], v['location']
            xs.append('%s: %s' % (agent.name(), location))

        return '{%s}' % (', '.join(xs))
