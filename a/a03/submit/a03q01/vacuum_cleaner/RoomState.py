import sys; sys.path.append('../ai/')
import agent.State 

class RoomState(agent.State.State):
    def __init__(self, value):
        agent.State.State.__init__(self, value)
        RoomState.check(value)
        
    @staticmethod
    def check(value):
        if value not in ['Clean', 'Dirty']:
            raise ValueError("Invalid RoomState value %s" % value)


if __name__ == '__main__':
    print("Testing RoomState")
    for value in ['Clean', 'Dirty']:
        try:
            s = RoomState(value)
            print("pass")
            for value in ['Clean', 'Dirty']:
                try:
                    s.value = value
                    print("pass")
                except:
                    print("FAIL")
            for value in ['A', 'B']:
                try:
                    s.value = value
                    print("FAIL")
                except:
                    print("pass")
        except:
            raise
            print("FAIL")
        
    for value in ['A', 'B']:
        try:
            s = RoomState(value)
            print("FAIL")
        except:
            print("pass")