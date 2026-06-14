# Code_01_(dictionary.pop(key))
# (Specific key remove)
student = {
    "name":"Harry",
    "age":20,
    "course":"Python"
}
removed_value = student.pop("age")

# Code_02_(dictionary.pop(key, default_value))
# With Default Value
print("Removed value:", removed_value)
print("Updated dictionary:",student)

student = {"name":"Harry"}
value = student.pop("age", "key not found")
print(value)


# Code_03_(dictionary.popitem())
# (Last inserted(Add) item remove) 
student = {
    "name":"Harry",
    "age":20,
    "course":"Python"
}
item = student.popitem()
print("Removed item:", item)
print("Updated dictionary:",student)