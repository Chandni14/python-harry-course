# Code_01_Union
s1 = {1, 45, 67, 90}
s2 = {45, 56, 89, 95, 1}
print(s1.union(s2))


# Code_02_Intersection
s1 = {1, 45, 67, 90}
s2 = {45, 56, 89, 95, 1}
print(s1.intersection(s2))


# Code_03_Difference( returns elements present in first set only)
A ={1, 45, 23, 54} 
B = {4, 45, 87, 67,90}
result = A.difference(B)
print(result)

# We can also using (-) operator
A ={1, 45, 23, 54} 
B = {4, 45, 87, 67,90}
print(A-B)


# Code_04_Symmertic_difference(returns elements that are in either set, but not in both sets)
A = {4, 67, 89, 56}
B = {56, 1, 7, 9, 5, 34}
result = A.symmetric_difference(B)
print(result)

# We can also using (^) operator
A = {4, 67, 89, 56}
B = {56, 1, 7, 9, 5, 34}
print(A^B)


# Code_05_issubset(For true condition)(All elements of A are present in B)
A = {34, 15, 26, 67}
B = {54, 15, 26, 76, 67, 34}
print(A.issubset(B))

# Code_05_issubset(For false condition)
A = {1, 2, 3, 4, 5}
B = {7, 8, 9, 0, 5, 4, 3}
print(A.issubset(B))


# Code_06_issuperset(For true condition)(All elements of B are present in A)
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
print(A.issuperset(B))

# Code_06_issuperset(For false condition)(All elements of A are present in B)
A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4 ,5, 6, 7}
print(A.issuperset(B))


# Code_07_isdisjoint(For true condition)(two sets have no common elements)
A = {1, 2, 3, 4, 5}
B = {6, 7, 8, 9, 10, 11, 12, 13, 15}
print(A.isdisjoint(B))

# Code_07_isdisjoint(For false condition)(Because 3 is present in both sets)
A = {1, 2, 3, 4, 5}
B = {3, 13, 15}
print(A.isdisjoint(B))