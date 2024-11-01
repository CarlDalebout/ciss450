
def secessors(s):
  a, b, c = s
  ret = []

  a0, b0, c0 = (a+1, b-2, c-1)
  if a0 >= 0 and b0 >= 0 and c0 >= 0:
    ret.append((a0, b0, c0))

  a0, b0, c0 = (a+1, b-1, c-3)
  if a0 >= 0 and b0 >= 0 and c0 >= 0:
    ret.append((a0, b0, c0))
  
  a0, b0, c0 = (a+1, b, c-5)
  if a0 >= 0 and b0 >= 0 and c0 >= 0:
    ret.append((a0, b0, c0))
  
  a0, b0, c0 = (a, b+1, c-2)
  if a0 >= 0 and b0 >= 0 and c0 >= 0:
    ret.append((a0, b0, c0))
  
  return ret

def h(s):
  return sum(s)

s = (0,0,275)
h_ = h(s)
while 1:
  print()
  print("top .... ", s, h)
  states = secessors(s)
  if len(states) == 0:
    print("NO SUCCESSOR")
    break
  xs = [(h(_), _) for _ in states]
  print(xs)

  xs.sort()
  print(xs)
  best = best_h, best_s = xs[0]
  print(best)

  if best_h >= h_:
    break 
  else:
    s, h_ = best_s, best_h