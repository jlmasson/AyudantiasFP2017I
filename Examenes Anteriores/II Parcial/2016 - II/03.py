A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9}
C = {5, 4, 7, 0, 1}
Y = {len(A), len(B), len(C)} # Y = {5, 6}

# Literal a
X = A | B # X = {1, 2, 3, 4, 5, 6, 7, 8, 9}
Z = X ^ C # Z = {0, 2, 3, 6, 8, 9}
E = X - C # E = {2, 3, 6, 8, 9}
print(A.issubset(E)) # False

# Literal b
Y = A & Y # Y = {5}
Z = Y - C # Z = set() -> conjunto vacío
print(Z)
