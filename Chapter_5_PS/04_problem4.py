# Code_01_Tricky...
s = set()
s.add(20)
s.add(20.0)
# In python the value of a integer (10) and the value of float (10.0) are same.
s.add('20')
# length of s after these operations?
print(s)
 
# Code_02
s = set()
s.add(20)
s.add(20.0)
s.add('20')
# length of s after these operations?
print(len(s))
