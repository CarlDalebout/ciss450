import sys
from Named import Named

class Object(Named):
    '''
Base class for objects with names and states.

Objects in the system must have unique names.
    '''
    
    def __init__(self,
                 name='',
                 state=None):
        Named.__init__(self, name)
        self.__state = state
        self.is_agent = False
        
    #--------------------------------------------------------------------------
    # state property
    #--------------------------------------------------------------------------
    def get_state(self):
        return self.__state
    def set_state(self, state):
        self.__state = state
    state = property(get_state, set_state)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Object %s name:%s state:%s>" % \
               (id(self), self.name, self.state) 
    
if __name__ == '__main__':
    chair1 = Object('chair A')
    print(chair1)
    print(repr(chair1))
    print(chair1.name)
    chair1.name = 'chair 0'
    print(chair1)

    try:
        chair2 = Object('chair A')
    except ValueError:
        print("pass")
