import random; random.seed()
import copy

n = 30

def empty(n):
  return [[' ' for _ in range(n)] for _ in range(n)]

def printBoard(m):
  def line(n):
    return  '   ' + '+-' * n + '+'
  l = line(n)
  print(l)
  for i, row  in enumerate(m):
    print(i, " |%s|" %'|'.join(row))
    print(l)

def rand_state(n):
  m = empty(n)
  for r in range(n):
    m[r][random.randrange(0,n)] = 'Q'
  return m

def isdiag(p0, p1):
  r0,c0 = p0
  r1,c1 = p1
  dr = r0 - r1
  dc = c0 - c1
  return  dr == dc or dr == -dc

def isattacking(p0, p1):
  return isdiag(p0, p1) or p0[1] == p1[1]

def h(m):
  n = len(m)
  points = []
  for r, row in enumerate(m):
    for c, col in enumerate(row):
      if m[r][c] == "Q":
        points.append((r, c))
  # print(points)
  s = 0
  for i in range(0, n-1):
    for j in range(i+1, n):
      p0 = points[i]
      p1 = points[j]
      s += int(isattacking(p0, p1))
      # print((i, j), points[i], points[j], isattacking(p0, p1), s)
  # print(s)
  return s

def actions(m):
  '''
    return [((r, c), +), ((r, c), -1), ... ]
  '''
  n = len(m)
  ret = []
  for r, row in enumerate(m):
    for c, v in enumerate(row):
      if v == 'Q':
        point = (r, c)
        if c < n-1:
          ret.append((point, +1))
        if c > 0:
          ret.append((point, -1))
        break
  return ret

def solve():
  """ Solve useing SA and Hill Climbing"""
  
  m = rand_state(n)
  # best_state = [m] # (a,b)  = (action, state)
  best_h = h(m)
  print(best_h)
  printBoard(m)

  # hc ... go over all succ and pick the best

  t = 0
  a = 1
  while 1:  
    """ HC
    improve = False
    for action in actions(m):
      (r, c), dc = action
      m0 = copy.deepcopy(m)
      m0[r][c] = ' '
      m0[r][c + dc] = 'Q'
      obj0 = h(m0)
      if obj0 == best_h:
        best_state.append(m0)
      elif obj0 < best_h:
        improve = True
        best_h = obj0
        best_state = [m0]
      else: 
        pass # dont consider a bad option
    
    if not improve:
      break
    else:
      m = random.choice(best_state)
      printBoard(m)
      print(best_h)
    
    input("? ")
    """
    # Simulater Annealing
    actions_ = actions(m)
    if len(actions_) == 0:
      break
    action = random.choice(actions_)
    m0 = action
    (r, c), dc = action
    m0 = copy.deepcopy(m)
    m0[r][c] = ' '
    m0[r][c + dc] = 'Q'
    obj0 = h(m0)

    # now we have m.best_h and m0 .obj0
    if obj0 < best_h:
      m = m0
      best_h = obj0
    else:
      x = random.uniform(0.0, 1.0)
      if x < a: # initially a = 1.0, 0.6, 0.4, 0.3, 0.2, ...
        m = m0
        best_h = obj0
      # get random r in [0,1] as time goes on [0, a] accept and 
      # a -> 0 as t -> in
      pass

    printBoard(m)
    print(best_h)


    input("? ")
    t += 1
    a = a / t
    """
      action = random.choice(as_)
      print("action:", action)
      (r, c), dc = action
      m0 = copy.deepcopy(m)
      m0[r][c] = ' '
      m0[r][c + dc] = 'Q'
      obj0 = h(m0)
      printBoard(m0)
      print(obj0)
      break
    """

if __name__ == "__main__":
  solve()