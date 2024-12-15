months={'Jan':1 , 'Feb':2 , 'Mar':3 , 'Apr':4 , 'May':5}
for m_keys,m_values in months.items():          # items()
    print(f"{m_keys} - {m_values}" , end=" ")
print('\n')
for m_keys in months.keys():                    # keys()
    print(m_keys , end=" , ")
print("\n")
for m_values in months.values():                # values()
    print(m_values , end=" , ")

m_keys = months.keys()
print(m_keys)      # dict_keys(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
m_values = months.values()
print(m_values)    # dict_values([1, 2, 3, 4, 5])
m_items = months.items()
print(m_items)     # dict_items([('Jan', 1), ('Feb', 2), ('Mar', 3), ('Apr', 4), ('May', 5)])

# Converting keys, values, key_value pairs to list
m_keys_list = list(months.keys())
print(m_keys_list)
m_values_list = list(months.values())
print(m_values_list)
m_items_list = list(months.items())
print(m_items_list)

# Sorting the dictionary
for m_keys in sorted(months.keys()):
    print(m_keys, end=" - ")
print('\n')
for m_values in sorted(months.values()):
    print(m_values, end=" - ")
print('\n')
for m_items in sorted(months.items()):
    print(m_items, end=" - ")
print('\n')

# Comparision of dictionaries
dictionary1 = {'a':1 , 'b':2 , 'c':3 }
dictionary2 = {'A':1 , 'b':2 , 'c':3 }
dictionary3 = {'c':3 , 'b':2 , 'A':1 }
print(dictionary1 == dictionary2)  # False
print(dictionary1 == dictionary1)  # True
print(dictionary2 == dictionary3)  # True

# Update method in Dictionary
animals={'Cat':1, 'Dog':2, 'Bird':3}

animals.update({'Reptile':5})
animals.update({'Cow':4})
animals.update({'Cow':14})
print(animals)
animals.update(Reptile=10)
print(animals)

# Dictionary Comprehension
numbers={'One':1, 'Two':2, 'Three':3}
num1={num:name for name, num in numbers.items()}
print(numbers,"\n",num1)

num_cubes={num:num**3 for num in range(1,6)}
print('\n',num_cubes)