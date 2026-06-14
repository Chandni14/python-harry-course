# Code_01_(a.items)
marks = {
     "Harry": 100,
     "Shubham": 56,
     "Rohan": 78,
     0: "Harry"
 }
print(marks. items())


# Code_02_(a.keys)
marks = {
     "Harry": 100,
     "Shubham": 56,
     "Rohan": 78,
     0: "Harry"
 }
print(marks. keys())


# Code_03_(a.value)
marks = {
     "Harry": 100,
     "Shubham": 56,
     "Rohan": 78,
     0: "Harry"
 }
print(marks. values())

#  Code_04_(a.update)
marks = {
     "Harry": 100,
     "Shubham": 56,
     "Rohan": 78,
     0: "Harry"
 }
marks.update({"Harry":99})
print(marks)


#  Code_04_(a.update)
marks = {
     "Harry": 100,
     "Shubham": 56,
     "Rohan": 78,
     0: "Harry"
 }
marks.update({"Harry":99, "Renuka": 100})
print(marks)

#  Code_05_(a.get("name"))
marks = {
     "Harry": 100,
     "Shubham": 56,
     "Rohan": 78,
     0: "Harry"
 }
print(marks.get("Harry2"))
# Prints None
print(marks["Harry2"])
# Returns an error

