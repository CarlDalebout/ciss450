import random; random.seed()
import copy

n = 5

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
  """ Solve useing SA """
  
  m = rand_state(n)
  obj = h(m)
  printBoard(m)
  print(obj)

  while 1:
    as_ = actions(m)
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

if __name__ == "__main__":
  solve()