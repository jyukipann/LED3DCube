import pulp
lp = pulp.LpProblem('lp', pulp.LpMaximize)
x1 = pulp.LpVariable('x1', 0)
x2 = pulp.LpVariable('x2', 0)
lp += x1 + x2
lp += x1 + 3*x2 <= 30
lp += x1 + x2 <= 15
lp += x2 <= 8
lp.solve()
print("x1=",x1.value())
print("x2=",x2.value())
