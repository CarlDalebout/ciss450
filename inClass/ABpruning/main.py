"""
Simulation of ab pruning
"""

def successors(s):
  d = {"s1":[( 'a1',  's2'), ( 'a2',  's3'), ( 'a3',  's4')],
       "s2":[( 'a4',  's5'), ( 'a5',  's6'), ( 'a6',  's7')],
       "s3":[( 'a7',  's8'), ( 'a8',  's9'), ( 'a9', 's10')],
       "s4":[('a10', 's11'), ('a11', 's12'), ('a12', 's13')],
       "s5":[('a13', 's14'), ('a14', 's15'), ('a15', 's16')]
      }
  d1 = dict([("s%s" % _, []) for _ in range(6, 17)])
  d.update(d1)
  return d.get(s, None)

def termial_value(s):
  d = {
       6:12,
       7:8,
       8:2,
       9:4,
       10:6,
       11:14,
       12:9,
       13:2,
       14:7,
       15:42,
       16:-1,
       20:20
      }
  return d.get(int(s[1:]), None)

def termial_test(s):
  return termial_value(s) != None


def mm(s, player): # are you playing a max or min 
  """ Return the Action of the player """
  if termial_test(s):
    return (None, termial_value(s))
  
  elif player in ["MAX", "max", "Max"]:
    maximum = None
    maximum_action = [None]
    for action, state in successors(s):
      action_value = mm(state, "MIN")
      print(action_value)
      a, v = action_value
      if maximum == None or v > maximum:
        maximum = v
        maximum_action = [action, a]
    return (maximum_action, maximum)
  
  else: # MIN
    minimum = None
    minimum_action = [None]
    for action, state in successors(s):
      action_value = mm(state, "MAX")
      print(action_value)
      a, v = action_value
      if minimum == None or v < minimum:
        minimum = v
        minimum_action = [action, a]
    return (minimum_action, minimum)

def abmm(s, player, alpha = [None, -999999], beta = [None, 999999]):
  if termial_test(s):
    return(None, termial_value(s))
  
  elif player in ['MAX', 'Max', 'max']:
    maximum = -99999999
    maximum_action = None
    for action, state in successors(s):
      action_value = abmm(state, "Min", alpha, beta)
      a, v = action_value
      if v > maximum:
          maximum = v
          maximum_action = [action, a]
      if maximum > alpha[1]:
          alpha[1] = maximum
          alpha[0] = maximum_action

      if beta[1] <= alpha[1]:
        print('skipping past', state)
        break
    return (maximum_action, maximum)
  
  else:
    minimum = 99999999
    minimum_action = None
    for action , state in successors(s):
      action_value = abmm(state, "Max", alpha, beta)
      a, v = action_value
      if minimum == None or v < minimum:
        minimum = v
        minimum_action = [action, a]
      if minimum > beta[1]:
        beta[1] = minimum
        beta[0] = minimum_action
      if beta[1] <= alpha[1]:
        print('skipping past', state)
        break
    return (minimum_action, minimum)

if __name__ == "__main__":
  while 1:
    state = input("which state: ")

    print(f"\nmm {state}, 'MAX'")
    ret = mm(state, "MAX")
    print(f"{ret}\n")
  
    print(f"abmm {state}, 'MAX'")
    ret = abmm(state, "MAX")
    print(f"{ret}\n")

    print(f"mm {state}, 'MIN'")
    ret = mm(state, "MIN")
    print(f"{ret}\n")

    print(f"abmm {state}, 'MIN'")
    ret = abmm(state, "MIN")
    print(f"{ret}\n")
