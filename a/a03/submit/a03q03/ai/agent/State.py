"""
State

Note that this is the class for environment states and (although related) is
not the same as states in the problem solving process.
"""

#class State(object):
class State:
    def __init__(self, value):
        # values is a list of possible values. If specified, this is use as a check.
        self.__value = value
        
    @staticmethod
    def check(value):
        pass
    
    #=======================================================================
    # value property
    #=======================================================================
    def get_value(self):
        return self.__value
    def set_value(self, value):
        self.check(value)
        self.__value = value
    value = property(get_value, set_value)
    
    def __str__(self):
        return '%s' % str(self.__value)

#==============================================================================
# Example
#==============================================================================
class Human(State):
    keys = set(['age', 'energy'])
    def __init__(self, **arg):
        assert set(arg.keys()).issubset(Human.keys)
        state = dict([(key,None) for key in Human.keys])
        state.update(arg)
        super(Human, self).__init__(state)

    #==========================================================================
    # age property
    #==========================================================================
    def get_age(self):
        return self.state['age']
    def set_age(self, age):
        self.state['age'] = age
    age = property(get_age, set_age)

    #==========================================================================
    # energy property
    #==========================================================================
    def get_energy(self):
        return self.state['energy']
    def set_energy(self, age):
        self.state['energy'] = age
    energy = property(get_energy, set_energy)


if __name__ == '__main__':
    """
    state = State(0)
    print(state)
    state.state = 1
    print(state.state)

    john = Human(age=30)
    print(john)
    print(john.age)
    john.age = 50
    print(john)
    john.energy = 1000000
    print(john.energy)
    print(john)

    roomstate = RoomState('Clean')
    print(roomstate)
    roomstate.cleanliness = 'Dirty'
    print(roomstate)
    """



