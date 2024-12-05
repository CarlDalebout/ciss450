"""
machine learning
f function has paramters and you tweak parameters to make f match some data
think: curve fitting
give u 3 points p0, p1, p2,
(x - x0)^2 + (y - y0)^2 = r^2
3 paramters - x0, y0, r.
in HS, you have formulas to compute x0, y0, r.

machine learnign:
start with (x0, y0, r) = (1.2, 7.5, 2.8)
and then try to change these parameters and get f to be as close as possible
to the given circle.
instead of giving you the circle, maybe u are given a collection of points to match.

Neural networks
model -- the function to use made up of artifical neurons
         neural network is a bunch of neurons

1 input neuron:

  N(x) = N(1, x) = 1 * w0 + x * w1, the '1' is called a bias

w0, w1 - weights. Usually you want to send this through a "pass filter".
In AI, these are called activation function.
So this becomes

    N_{A, (w0, w1)}(x) = A(1 * w0 + x * w1) = A(<1, x>, <w0, w1>)

A 2 - input neuron look slike this:

    N_{A, (w0, w1, w2)}(x1, x2) = A(1 * w0 + x1 * w1 + x2 * w2) 
                                = A(<1, x1,  x2>,<w0,  w1,  w2>)
                                = A(bold x, bold w)

An n-input neuron looks likewise.

There are many activation functions. Historically the 1st important one is 
Sigmoid S(z)

  S(z) = 1/(1 + e^(-z))

Goal:
Create neuron N_{A, w}(x1, x2) so that this acts like the AND(x1, x2) gate
"""

import math
e = math.e

class Activation:
  def __init__(self):
    pass

class Sigmoid(Activation): # reLU
  def __init__(self):
    Activation.__init__(self)
  def __call__(self, z):
    return 1.0/(1.0 + e**(-z))

class Identity(Activation):
  def __init__(self):
    Activation.__init__(self)
  def __call__(self, z):
    return z

class Threshold:
  def __init__(self, cutoff):
    self.cutoff = cutoff
  def __call__(self, z):
    if z <= self.cutoff: return 0
    else: return 1

class Neuron:
  def __init__(self, A, w):
    self.A = A
    self.w = w
  def __call__(self, *x):
    x = (1,) + x
    s = sum(a * b for (a,b) in zip(self.w, x))
    
    return self.A(s)

if __name__ == "__main__":
  # N = Neuron(A = Sigmoid(), w = [0, 1])   # N = S(0*1 + 1 * x)
  # print(N([1]))                           #   = S(x)
  #                                         #   = 1/1+e^(-x) = 1/1+e^(-1)
  # N = Neuron(A = Sigmoid(), w = [0.5, 0]) # N = S(0.5 * 1 + 0 * x)
  # print(N([1]))                           #   = S(0.5)
  #                                         #   = 1/1+e^(-x) = 1/1+e^(-0.5)
  # S = Sigmoid()
  # print(S(0.5))

  N = Neuron(A = Sigmoid(), w = [0.1, 0.2, 0.3])
  for x in [0, 1]:
    for y in [0, 1]:
      print(x, y, N(x, y))

  tests = [(0,0,0), (0,1,0), (1,0,0), (1,1,1)]
  AND = Neuron(A = Threshold(0.5), w = [0.1, 0.3, 0.3])
  for test in tests:
    x, y, correct = test
    print(x, y, AND(x, y), correct)