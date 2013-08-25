def add2Vectors(u, v) : return [u[i]+v[i] for i in range(len(u))]

def scalar_vector_mult(alpha, v) : return [alpha*number for number in v]


def convex_combo(alpha, u, v) : return [add2Vectors(scalar_vector_mult(alpha, u), scalar_vector_mult(1-alpha, v))]

def list_dot(u, v): return sum( [ a*b for (a,b) in zip(u, v) ])