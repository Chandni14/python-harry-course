# Interger type
a = 31
t = type(a)
print(t)

# Float type
a = 41.6
t = type(a)
print(t)

# String type
a = "Chandni"
t = type(a)
print(t)

# Tricky
a = "35.66"
t = type(a)
print(t)

# change Float into String
a = 32.2
b = float(a)
# a but the type should be float 
t = type(b)
print(t)


# change String into Float
a = "Harry"
b = str(a)
# a but the type should be string
t = type(b)
print(t)

# change Float into Integer
a = 31.7
b = int(a)
# a but the type should be interger
t = type(b)
print(t)