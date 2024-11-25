"""
CSP
variables X1, X2, X3, ...
domains D1, D2, D3, ...
constraints C1, C2, C3, ...


logic
X = VAR("X")
Y = VAR("Y")
Z = VAR("Z")
P = AND(X, Y)
Q = AND(X, NOT(Z))
R = OR(P, Q)
S = SUBST(R, (X, True))
"""

class CSP:
    def __init__(self,
                 vars,    # example: ["X1", "X2, "X3"]
                 domains, # example: {"X1":['r', 'g', 'b'],
                          #           "X2":['r', 'g', 'b'],
                          #           "X3":['r', 'g', 'b']}
                 constraints, # example: ["X1 != X2", "X1 != X3"]
    ):
        self.vars = vars
        self.domains = domains
        self.constraints = constraints
    def __str__ (self):
        return """<CSP
vars: %s
domains: %s
constrains: %s
>""" % (self.vars, self.domains, self.constraints)

''' use graph coloring problem
X -- Y -- W
|   /
|  /
| /
|/
Z
'''
X = 'X'
Y = 'Y'
Z = 'Z'
W = 'W'
r = 'r'
g = 'g'
b = 'b'

csp = CSP(vars=[X, Y, Z, W],
          domains={X:[r, g, b],
                   Y:[r, g, b],
                   Z:[r, g, b],
                   W:[r, g, b]},
          constraints = {(X, Y): "X != Y",
                         (X, Z): "X != Z",
                         (Y, Z): "Y != Z",
                         (W, Y): "W != Y"}
)

# assume BT selects X = r ...
assignment = [(X, r)]
var = assignment[0][0]
val = assignment[0][1]
# compute new vars
vars2 = [_ for _ in csp.vars if _ != assignment[0][0]]

# compute new constraints
print("csp.constraints:", csp.constraints)
constraints2 = {}
for k,v in csp.constraints.items():
    #print("k, v:", k, v)
    if var in k:
        v = v.replace(var, '"%s"' % str(val))
        k = tuple(_ for _ in k if _ != var)
        #print("case 0 ... k, v:", k, v)
    constraints2[k] = v
# print("constraints2:", constraints2)
    
# compute new domains
domains2 = {}
for k,v in constraints2.items():
    print("k:", k)
    if len(k) == 1:
        # print("k, prop:", k, v)
        domains2[k[0]] = []
        for x in csp.domains[k[0]]:
            v0 = v.replace(k[0], '"%s"' % x)
            if eval(v0) == True:
                domains2[k[0]].append(x)
    else: # non-unary propositions
        None

constraints2 = dict([(k, v) for (k, v) in constraints2.items() if len(k) != 1])

for v in vars2:
    if v not in domains2:
        domains2[v] = csp.domains[v]
        # print(v, domains2[v])
# print(domains2)

csp2 = CSP(vars=vars2, domains=domains2, constraints=constraints2)

print("csp:", csp)
print("csp2:", csp2)

asd

'''
for var1 in vars2:
    print("(var, var1):", (var, var1))
    if (var, var1) in csp.constraints.keys():
        c = csp.constraints[(var, var1)]
        print("c:", c)
        c = c.replace(var, '"%s"' % val)
        print("c:", c)
        D = []
        for v in csp.domains[var1]:
            c1 = c.replace(var1, '"%s"' % v)
            print("c1:", c1)
            if eval(c1):
                D.append(v)
                print("D:", D)
        domains2[var1] = D
'''
print("domains2:", domains2)

asd
constraints2 = None
csp2 = CSP(vars = vars2,
           domains = domains2,
           constaints = constraints2)
          