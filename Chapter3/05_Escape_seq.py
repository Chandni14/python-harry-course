# Note = Escape_Sequence_Characters
# example = \n, \t, \" or  \', \ \etc.

# Example = 1(\n for Newline)
a = "Chandni is a good girl\nbut not a bad girl\nshe is a smart girl"
print(a)



# Ex = 2(\t for Tab)
a = "Chandni is a good girl\nbut not a bad girl\tshe is a smart girl"
print(a)



# Ex = 3(\" for doublequote)
# a = "Chandni is a good girl\nbut not a bad girl\nshe is a smart " girl""(Error genrated)
# print(a)
a = "Chandni is a good girl\nbut not a bad girl\nshe is a smart \" girl\""
print(a)


# Ex = 4(special case)
a = "Chandni is a good girl\nbut not a bad girl\nshe is a smart ' girl'"
print(a)


# Ex = 5(\' for singlequote)
# a = 'Chandni is a good girl\nbut not a bad girl\nshe is a smart ' girl''(Error genrated)
# print(a)
a = 'Chandni is a good girl\nbut not a bad girl\nshe is a smart \' girl\''
print(a)


