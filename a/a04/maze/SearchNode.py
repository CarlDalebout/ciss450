class SearchNode:

    def __init__(self,
                 state,
                 action = None,
                 parent=None,
                 parent_action=None,
                 path_cost=0):
        self.state = state
        self.action = action
        self.parent = parent
        self.parent_action = parent_action
        self.path_cost = path_cost

    def __str__(self):
        return '<SearchNode %s %s %s %s %s>' % (id(self),
                                                self.state,
                                                id(self.parent),
                                                id(self.parent_action),
                                                self.path_cost)
    def solution(self):
        pass
        

if __name__ == '__main__':
    print("Testing (0,0) -> (1,0) -> (1,1) by actions ['E', 'S']")
    state00 = (0, 0)
    node00 = SearchNode(state00)
    state01 = (0, 1)
    node01 = SearchNode(state01, node00, 'E', 1)
    state11 = (1, 1)
    node11 = SearchNode(state11, node01, 'S', 1)
    print(node00)
    print(node01)
    print(node11)
    print(node11.solution())
    print("Expected: ['E', 'S']")
