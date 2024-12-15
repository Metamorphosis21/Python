dict={'key1': 11, 'key2': 'string2', 'key3': [1,2,3]} 
print(dict)

# Checking fif the dictionary is empty or not
print(len(dict))
# print(dict.clear())
if dict:
    print('Hello')
else:
    print('World')

# Iteration through the dictionary
for k,v in dict.items():
    print(f'{k} = {v}')

# Operation of the dictionary
roman={'I':1 , 'II':2 , 'III':3 , 'IV':4 , 'V':5 , 'X':10}

print(roman['V'])   # Accessing the value of a key dictionary

roman['I'] = 10     # Updating the value of a key dictionary
print(roman)

roman['L'] = 50     # Adding new key - value pair in dictionary
print(roman)

del roman['I']      # Delete the key - value of dictionary
print(roman)
print(roman.pop('II'))      # Pop the value of the key and delete the key - value pair of dictionary
print(roman)

print(roman['C'])       # KeyError - Key not found
print(roman.get('C'))   # keyError is not shown but if the key is not present then displays None
print(roman.get('C', 'C not present'))      # if key is not present shows the other msg
print(roman['L'])      # give the value as output

# to check if a key is present in the dictionary or not
print('L' in roman)      # True
print('C' not in roman)      # True





