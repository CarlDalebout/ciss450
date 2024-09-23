#class Named(object):
class Named:
    
    names = set()

    def __init__(self,
                 name=None):
        if name in Named.names:
            raise ValueError('An object with name "%s" already exists.' % name)
        if name==None:
            print("WARNING: name is None")
        else:
            Named.names.add(name)
        self.__name = name

    def get_name(self):
        return self.__name
    name = property(get_name, None)
    
    def __str__(self):
        return self.__name

    def __repr__(self):
        return "<Named %s name:%s>" % (id(self), self.name) 
    
if __name__ == '__main__':
    X = Named('X')
    print(X)
    X.name = 'Y'
    print(X)
    roomA = Named('room A')
    print(roomA)
