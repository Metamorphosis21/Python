marks=[80,90,70,81,92,66]
new_marks=list(map(lambda x:x+5,marks))
print(new_marks)

# The map() function is used here. It applies a function to every item in the given iterable (in this case, the list marks).

# A lambda function is defined as lambda x: x + 5. This is an anonymous function that takes one argument x and returns x + 5. Essentially, it increases each element in the marks list by 5.

# The map() function returns an iterator, so we wrap it with list() to convert the result into a list.

# As a result, new_marks will contain the values of marks each increased by 5.