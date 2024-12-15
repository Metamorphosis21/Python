# Mathematical set operations
print({1,3,5} | {2,4,6})
print({1,3,5}.union({2,4,6}))

print({1,3,5,7,9} & {3,5,2,4,6})
print({1,3,5,7,9}.intersection({3,5,2,4,6}))

print({1,2,3,4,5} - {2,4,6})
print({1,2,3,4,5}.difference({2,4,6}))

print({1,2,3,4,5,6} ^ {2,4,6,7,8,9})
print({1,2,3,4,5,6}.symmetric_difference({2,4,6,7,8,9}))
print({1,2,3,4,5,6}.union({2,4,6,7,8,9}).difference({1,2,3,4,5,6}.intersection({2,4,6,7,8,9})))

print({1,2,3,4}.isdisjoint({5,6,7,8}))

# Mutable mathmatical set operations
number={1,3,5}

number|={2,4,6}
print(number)

number&={1,5}
print(number)

number-={1,3,5}
print(number)

number.update(range(11))
print(number)

# Method to add and remove elements
number.add(11)      # takes only one argument
print(number)
number.remove(1)  
number.discard(2)
print(number)
print(number.pop()) # returns the first element of yhe array
number.clear()
print(number)   

# Set comprehension
s_list=[1,2,3,4,5,6,7,8,9,10]
set_even={i for i in s_list if i%2==0}
print(set_even)