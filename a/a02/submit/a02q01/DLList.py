# File: DLList.py
# Dir: a02/a02q01
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
    
    value = property(get_value, set_value)

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


class DLList:

    def __init__(self):
        # self.__head = Node.DLNode(prev=None, is_sentinel= True)
        # self.__tail = Node.DLNode(prev= self.__head, is_sentinel= True)
        # self.__head.set_next(self.__tail)
        head_sentinal = DLNode(is_sentinel = True) 
        tail_sentinal = DLNode(is_sentinel = True) 
        head_sentinal.set_next(tail_sentinal)
        tail_sentinal.set_prev(head_sentinal)
        self.__head = head_sentinal
        self.__tail = tail_sentinal
        self.__size = 0
        self.__empty = True

    def get_head(self):
        if self.__empty:
            return None
        return self.__head.next.value
    
    def set_head(self, key):
        self.__head.next.value = key

    def delete_head(self):
        if self.__size == 0:
            return None
        temp = self.__head.next
        self.__head.next = temp.next
        temp.next.prev = self.__head
        ret = temp.value
        del temp
        self.__size -= 1
        return ret

    head = property(get_head, set_head, delete_head)

    def get_tail(self):
        if self.__empty:
            return None
        return self.__tail.prev.value

    def set_tail(self, key):
        self.__tail.prev.value = key

    def delete_tail(self):
        if self.__size == 0:
            return None
        temp = self.__tail.prev
        self.__tail.prev = temp.prev
        temp.prev.next = self.__tail
        ret = temp.value
        del temp
        self.__size -= 1
        return ret

    tail = property(get_tail, set_tail, delete_tail)

    def is_empty(self):
        if self.__size == 0:
            return True
        return False


    def __init__(self, list = None):
        # self.__head = Node.DLNode(prev=None, is_sentinel= True)
        # self.__tail = Node.DLNode(prev= self.__head, is_sentinel= True)
        # self.__head.set_next(self.__tail)
        head_sentinal = DLNode(is_sentinel = True) 
        tail_sentinal = DLNode(is_sentinel = True) 
        head_sentinal.set_next(tail_sentinal)
        tail_sentinal.set_prev(head_sentinal)
        self.__head = head_sentinal
        self.__tail = tail_sentinal
        self.__size = 0
        self.__empty = True
        
        if list != None:
            for i in list:
                self.insert_tail(i)

    def __len__(self):
        return self.__size

    def __repr__(self):
        temp = self.__head.next
        ret = "<DLList %s [" %(id(self))
        dir = ""
        for i in range(self.__size):
            ret += dir + repr(temp)
            dir = ", "
            temp = temp.next
        ret += "]>"
        return ret

    def __str__(self):
        temp = self.__head.next
        ret = "["
        dir = ""
        
        for i in range(self.__size):
            ret += dir + str(temp.value) 
            dir = ", "
            temp = temp.next
        
        ret += "]"

        return ret
    
    def __eq__(self, DLList):
        if len(DLList) != self.__size:
            return False
        
        else:
            temp1 = self.__head.next
            temp2 = DLList.__head.next
        
            for i in range(self.__size):
                if temp1 != temp2:
                    return False
                temp1 = temp1.next
                temp2 = temp2.next
        
        return True
        
    def get_list(self):
        temp = self.__head.next
        ret = []
        for i in range(self.__size):
            ret.append(temp.value)
            temp = temp.next
        return ret
    
    def insert_head(self, key):
        node = DLNode(key)
        self.__head.next.prev = node

        node.set_next(self.__head.next) 
        node.set_prev(self.__head)
        
        self.__head.set_next(node)

        self.__size += 1
        self.__empty = False

    def insert_tail(self, key):
        node = DLNode(key)

        self.__tail.prev.next = node
        
        node.next = self.__tail
        node.prev = self.__tail.prev
        
        self.__tail.prev = node
        self.__size += 1
        self.__empty = False

    def insert_before(self, key, node):
        pass

    def insert_after(self, key, node):
        pass