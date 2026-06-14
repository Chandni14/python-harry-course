# PROPERTIES OF SETS
# Sets are unordered =>Elements order does not matter
# Sets are unindexed =>Cannot access elements by index
# There is no way to change items in sets. 
# Sets cannot contain duplicate values.

# Code_01
s = {1, 5, 87, 5, 6, 5, 98, 5, "Harry"}
print(s, type(s))

# Code_02(s.add())
s = {1, 5, 87, 5, 6, 5, 98, 5, "Harry"}
print(s, type(s))
s.add(566)
print(s, type(s))

# Code_03(s.remove() OR s.discard())
s = {1, 5, 87, 5, 6, 5, 98, 5, "Harry"}
print(s, type(s))
s.remove(87)
print(s, type(s))

# Code_04(s.pop())
# (Removes an arbitrary element from the set and return the element removed).
s = {1, 5, 87, 5, 6, 5, 98, 5, "Harry"}
print(s, type(s))
s.add(566)
s.remove(87)
s.pop()
print(s, type(s))

# Code_05(s.clear())
s = {1, 5, 87, 5, 6, 5, 98, 5, "Harry"}
print(s, type(s))
s.add(566)
s.remove(87)
s.clear()
print(s, type(s))

Code_06
A = {34, 15, 26, 67}
B = {54, 15, 26, 76, 67, 34}
print(A.issubset(B))


A = {1, 2, 3, 4, 5}
B = {7, 8, 9, 0, 5, 4, 3}
print(A.issubset(B))