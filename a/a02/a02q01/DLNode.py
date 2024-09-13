# File: DLNode.py
# Dir:  a02/a02q01
# Author: Carl Dalebout

class DLNode:
    def __init__(self, value=None, next=None, prev=None,
                                              is_sentinel=False):
        # To make things simple, I'm using sentinel nodes. Also,
        # I do not use a separate class for sentinel nodes. I simply
        # include a variable __is_sentinel to tell me if the node is
        # a sentinel node.
        self.__value = value
        self.__next = next
        self.__prev = prev
        self.__is_sentinel = is_sentinel
    
    def get_next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next
    
    next = property(get_next, set_next)

    def get_prev(self):
        return self.__prev
    
    def set_prev(self, prev):
        self.__prev = prev
    
    prev = property(get_prev, set_prev)

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value
    
    value = property(get_value)

    def get_is_sentinel(self):
        return self.__is_sentinel
        # Add properties prev, next_, is_sentinel, value.
        # Use next_ to avoid confusion with the next keyword.
    
    is_sentinel = property(get_is_sentinel)

    def __repr__(self):
        return "<DLNode %s value:%s, prev:%s, next:%s>" % (id(self),
                                                           self.__value,
                                                           id(self.__prev),
                                                           id(self.__next))
    
    def __str__(self):
        return "%s" % self.__value
    
    def __eq__(self, node):
        # ***** TO BE COMPLETED *****
        # Returns true if self.__value and node.__value are the same
        return (self.__value == node.__value)
