"""
Simulation of ab pruning
"""

def successors(s):
  d = {"s1":[( 'a1',  's2'), ( 'a2',  's3'), ( 'a3',  's4')],
       "s2":[( 'a4',  's5'), ( 'a5',  's6'), ( 'a7',  's8')],
       "s3":[( 'a7',  's8'), ( 'a8',  's9'), ( 'a9', 's10')],
       "s4":[('a10', 's11'), ('a11', 's12'), ('a12', 's13')]
      }
  d1 = dict([("s%s" % _, []) for _ in range(5, 14)])
  d.update(d1)
  return d.get(s, None)

def termial_value(s):
  d = {5:3,
       6:12,
       7:8,
       8:2,
       9:4,
       10:6,
       11:14,
       12:5,
       13:2
      }
  return d.get(int(s[1:]), None)

def termial_test(s):
  return termial_value(s) != None


def mm(s, player): # are you playing a max or min 
  """ Return the Action of the player """
  if termial_test(s):
    return (None, termial_value(s))
  
  if player == "MAX":
    maximum = None
    maximum_action = None
    for action, state in successors(s):
      action_value = mm(state, "MIN")
      a, v = action_value
      if a == None:
        a = action
      if maximum == None or v > maximum:
        maximum = v
        maximum_action = a
    return (maximum_action, maximum)
  else: # MIN
    pass
    # minimum = None
    # minimum_action = None
    # for action, state in successors(s):
    #   action_value = mm(state, "Max")
    #   a, v = action_value
    #   if a == None:
    #     a = action
    #   if minimum == None or v < minimum:
    #     minimum = v
    #     minimum_action = a
    # return (minimum_action, minimum)


if __name__ == "__main__":
  # ret = mm("s1", "MAX")
  # print(ret)
  ret = mm("s2", "MAX")
  print(ret)
  ret = mm("s3", "MAX")
  print(ret)            
  ret = mm("s4", "MAX")
  print(ret)