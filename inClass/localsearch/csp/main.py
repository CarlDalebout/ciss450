"""
CSP = constarainst satisfaction problems

Variables     Domains
X1            D1
X2            D2
X3            D3

find assignment (X1, v1), ..., v1 in D1, ....
such that
X1, X2, X3 satisfies some "constraints:

X1 + X2 + X3 <= 10
X1 >= 3

graph coloring is a CSP

A-------B
|       |
|       |
C-------D

A, B, C, D domains {Red, Green, Blue}
A != B
A != C
B != D

solutions:
1. start with assignment. keep adding assignments until full.

{} -> {A = Red} -> {A = Red, C = Green} -> ...

2. Start with random assignment. do local search.

FOCUS: 1.

General idea:
Pick 1 var, for that var pick 1 value. Add (var, val) to assignment.
Repeat. Each time making sure the new (var, val) is "consistent" .. i.e.,
does not violate the constraints.

i.e., using backtracking.

The difference between this and regular graph coloring bt is: 
pick variable using a heuristic
for that var, order the values in the domain using a heuristic.
"""

D = list(range(1, 10))
C = 'A1 != A3'
assignment = [("A3", 3)]
a, b = assignment[0]
print(a,b)
C = C.replace(a, str(b))
print("C:", C)
print("D:", D)

v = D[0]
print("v:", v)
# C = C.replace("A1", str(v))
print("C:", C)
# print(eval(C))
D = [v for v in D if eval(C.replace("A1", str(v)))]
print("D:", D)