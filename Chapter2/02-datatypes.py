a = 1    
# a is an integer
b = 5.22
# b is a floating point number
c = "chandni"
# c is a string
d = False
# d is a boolean variable
e = None
# e is a none type variable

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))


print("\n---Type Casting ---")

# 1. change int into float 
x = 10
print("Original:",x, type(x))
y = float(x)
print("After float():",y, type(y))

# 2. change int into string
z = str(x)
print("After str():",z, type(z))

# 3. change string into int
num_str = "25"
num = int(num_str)
print("String '25' to int:", num, type(num))
# 4. change float into int
price = 99.99
final_price = int(price)
print("Float 99.99 to int:", final_price, type(final_price))