# 01_String_Concatenate_in_Python.
a  = "Hello"
b = "World"
main_str = 'a, b'
print(a+b)


# 02
a  = "Hello"
b = "World"

# + operator
print(a + " " + b)
# For Space between 'a' and 'b


#03
a  = "Hello"
b = "World"
print(a + " " + b)
print('_'.join([a, b]))
# For hyphen

print('_'.join([a, b, 'Disha'])) 
# To add a string
 
# Join
print(' '.join([a, b]))
# second way for Space between 'a' and 'b'

# % Formater
print('%s %s' % (a, b))
# Third way for Space between 'a' and 'b'

# Format
print('{} {}'.format(a, b))
# Fourth way for Space between 'a' and 'b'

# F-strings
'a b'
"a b"
"""a b"""
print(f'{a} {b}')