# File: DLList.py
# Dir: a02/a02q01
# Author: Carl Dalebout

import DLNode as Node



class DLList:
    def __init__(self):
        self.__head = Node.DLNode(prev=None, is_sentinel= True)
        self.__tail = Node.DLNode(prev= self.__head, is_sentinel= True)
        self.__head.set_next(self.__tail)
        self.__size = 0
        self.__empty = True

    def get_head(self):
        return self.__head
    
    def insert_head(self, node):
        self.__head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.__head.next = node
        self.__size += 1
        self.__empty = False

    def delete_head(self):
        temp = self.head.next
        self.head.next = temp.next
        temp.next.prev = self.head
        del temp

    head = property(get_head, insert_head, delete_head)

    def get_tail(self):
        return self.__tail
    
    def insert_tail(self, node):
        self.__tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.__tail.prev = node
        self.__size += 1
        self.__empty = False

    def delete_tail(self):
        temp = self.tail.prev
        self.tail.prev = temp.prev
        temp.prev.next = self.tail
        del temp

    tail = property(get_tail, insert_tail, delete_tail)

    def __init__(self, list):
        self.__head = Node.DLNode(prev=None, is_sentinel= True)
        self.__tail = Node.DLNode(prev= self.__head, is_sentinel= True)
        self.__head.set_next(self.__tail)
        self.__size = 0
        self.__empty = True

        for i in range(len(list)):
            self.tail = Node.DLNode(list[i])

    def __len__(self):
        return self.__size

    def __repr__(self):
        temp = self.head.next
        ret = "<DLList %s [" %(id(self))
        dir = ""
        for i in range(self.__size):
            ret += dir + repr(temp)
            dir = ", "
            temp = temp.next
        ret += "]>"
        return ret

    def __str__(self):
        temp = self.head.next
        ret = "["
        dir = ""
        
        for i in range(self.__size):
            ret += dir + str(temp.value) 
            dir = ", "
            temp = temp.next
        
        ret += "]"

        return ret
    
    def __eq__(self, DLList):
        # WIP
        pass