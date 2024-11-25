"""
A logic library for CSP and logic agents

X = PropVar("X")
Y = PropVar("Y")
Z = PropVar("Z")
print(X, Y, Z)

e = X and Y <-- logic of X,Y
notation: e = AND(X, Y)
print(e) ----> "X & Y"

e1 = SUBST(e, [(X, TRUE)])
print(e1) ----> "TRUE & Y"

e2 = SIMPLIFY(e1)
print(e1) ----> "Y" (in dm225: X and True = X, True & True = True)

ONly propositional logic.
No predicate logic.

Sentence -> AtomicSentence | CompoindSentence
AtomicSentence -> Constant | PropVar
CompountSentence -> Sentence & Sentence
                  | Sentence | Sentence
                  | - Sentence
                  | Sentence -> Sentence
                  | Sentence <- Sentence
                  | Sentence <> Sentence

"""

class Atomic:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return self.name

class Constant(Atomic):
  def __init__(self, name):
    Atomic.__init__(self, name)
  def __str__(self):
    return self.name

TRUE = Constant("TRUE")
FALSE = Constant("FALSE")

class PropVar(Atomic):
  """
    Each propositional variable must be uniquely defined
    by their name
  """
  def __init__(self, name="[None]"):
      Atomic.__init__(self, name)
  def __str__(self):
    return self.name

class AND:
  def __init__(self, x, y):
    self.left  = x
    self.right = y
  def __str__(self):
    return "(%s & %s)" % (self.left, self.right)

class OR:
  def __init__(self, x, y):
    self.left  = x
    self.right = y
  def __str__(self):
    return "(%s | %s)" % (self.left, self.right)

def SUBST(e, assignment):
  """
    e = X & Y, X = TRUE ----> return TRUE & Y

    SUBST(X & Y, X=TRUE)
    = SUBST(AND(X, Y), X=TRUE)
    = AND(SUBST(X, X=TRUE), SUBT(Y, X=TRUE))

  """
  if isinstance(e, Constant):
    return e

  if isinstance(e, PropVar):
    for var, val in assignment:
      if e.name == var.name: # <--- WARNING: 
        return val
      else:
        return e
      
  elif isinstance(e, AND):
    left  = SUBST(e.left,  assignment)
    right = SUBST(e.right, assignment)
    return AND(left, right)
  
  elif isinstance(e, OR):
    left = SUBST(e.left, assignment)
    right = SUBST(e.right, assignment)
    return OR(left, right)

def SIMPLIFY(e):
  if isinstance(e, Atomic):
    return e
  
  elif isinstance(e, AND):
    left = e.left
    right = e.right
    # if left.name == TRUE:


if __name__ == "__main__":
  X = PropVar("X")
  Y = PropVar("Y")
  Z = PropVar("Z")
  print(X, Y, Z)
  
  e = AND(X,Y)
  # print(e)
  
  f = AND(e, Z) # ((X & Y) & Z)
  # print(f)
  
  g = OR(e, Z)  # ((X & Y) | Z)
  print(g)  
  
  e1 = SUBST(e, [(X, TRUE)])
  print("e1:", e1)

  f1 = SUBST(f, [(X, TRUE)])
  print("f1:", f1)

  g1 = SUBST(g, [(X, TRUE)])
  print("g1:", g1)

  e2 = SIMPLIFY(e1)
  print("e2:", e2)