from sympy import symbols, diff, sqrt

# Define the symbols
x, y, z = symbols('x y z')

# Define the functions p, q, r given in the problem
p = x + y + z
q = x - y + z
r = x + y - z

# Function u in terms of p, q, r
u = (p - q) / q * r

# Express u directly in terms of x, y, z by substituting p, q, and r
u = u.subs({'p': p, 'q': q, 'r': r})


