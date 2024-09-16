from Agent import Agent

    
class Environment:
    
    def __init__(self,
                 objs=None,
                 ):
        if objs == None: objs = []
        self.objs = []
        for obj in objs:
            self.add(obj)

    def add(self, obj):
        self.objs.append(obj)
        
    def get_percept(self, agent):
        """ Get percept for an agent """
        pass

    def act(self, agent, action):
        """ Make agent's action modify the environment state """
        pass

    def __str__(self):
        return ', '.join(["%s:%s"% (obj.name,
                                    obj.state) \
                          for obj in self.objs])

    def find(self, kls):
        # Find objects by class
        ret = []
        for obj in self.objs: 
            if isinstance(obj, kls):
                ret.append(obj)
        return ret

    def find_agents(self):
        #return self.find(Agent)

        # 2022/9/15: isinstance in find error. Temporary fix.
        ret = []
        for obj in self.objs: 
            if obj.is_agent:
                ret.append(obj)
        return ret
    
    def find_first(self, kls):
        for obj in self.objs:
            if isinstance(obj, kls):
                return obj
        return None
    
    def find_first_by_name(self, name):
        for obj in self.objs:
            try:
                if obj.name == name:
                    return obj
            except AttributeError:
                raise str(obj)
        return None

    
