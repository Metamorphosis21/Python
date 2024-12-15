import random as rd
import numpy as np
import time

# timing gerneration of list vs array with 6000000 elements

start_time = time.time()
roll_list = [rd.randrange(1, 7) for i in range(0, 6000000)]   # List Generation with Random
list_time = time.time() - start_time

start_time = time.time()
roll_array = np.random.randint(1, 7, 6000000)   # NumPy Array Generation
array_time = time.time() - start_time

print(f"List Generation Time: {list_time} seconds")
print(f"NumPy Array Generation Time: {array_time} seconds")
print(f"List Length: {len(roll_list)}")
print(f"NumPy Array Length: {len(roll_array)}")
print(f"List First 10 elements: {roll_list[:10]}")
print(f"NumPy Array First 10 elements: {roll_array[:10]}")


# # Sum of range 0 to 9999999 in list vs array

start_time = time.time()
sum([x for x in range(10_000_000)])
list_time = time.time() - start_time

start_time = time.time()
np.arange(10_000_000).sum()
array_time = time.time() - start_time

print(f"List Generation Time: {list_time:.3f} seconds \t Array Generation time: {array_time:.3f} seconds")




# Arithmetic operation and comparing between two arrays

arr1 = np.array([1,3,5,7,9])
arr2 = np.array([2,4,6,8,10])

print(arr1*2)
print(arr1**2)
print(arr1+10)
print(arr1*arr2)

print(arr1 >= 3)
print(arr1 >= arr2)
print(arr2 == [2,2,6,4,6])

print(np.arange(1,6) ** 2)




# NumPy calculation method

grades = np.array([[10,20,30],[23,34,56],[95,94,93]])
print(grades)
print(f"Grades Sum: {grades.sum()}")
print(f"Grades Min: {grades.min()}")
print(f"Grades Max: {grades.max()}")
print(f"Grades Mean: {grades.mean(axis=0)}")    # axis=0(performs mean opertion on column) & axis=1(performs mean operation on rows)
print(f"Grades Std: {grades.std():.3f}")
print(f"Grades Var: {grades.var():.3f}")

grade_arr = np.random.randint(60,101,12).reshape(3,4)
print(grade_arr)
print(f"Average:{grade_arr.mean():.3f}")        
# print(f"Average:{grade_arr.sum()/grade_arr.size:.3f}")
print(f"Average of each row:{[f'{avg:.2f}' for avg in grade_arr.mean(axis=1)] }")
print(f"Average of each column:{[f'{avg:.2f}' for avg in grade_arr.mean(axis=0)]}")





# Universal functions: 

uni_arr = np.array([1,4,9,16,25])
uni_arr2 = np.arange(1,6)*10

print(np.sqrt(uni_arr))
print(np.add(uni_arr,uni_arr2)) 
print(np.multiply(uni_arr,5))

# Math—add, subtract, multiply, divide, remainder, exp, log, sqrt, power, and more.
# Trigonometry—sin, cos, tan, hypot, arcsin, arccos, arctan, and more.
# Bit manipulation—bitwise_and, bitwise_or, bitwise_xor, invert, left_shift and
# right_shift.
# Comparison—greater, greater_equal, less, less_equal, equal, not_equal, logical_and,
# logical_or, logical_xor, logical_not, minimum, maximum, and more.
# Floating point—floor, ceil, isinf, isnan, fabs, trunc, and more.




# Indexing nd Slicing

ind_slc = np.arange(1,16).reshape(3,5)
print(ind_slc)

print(ind_slc[1])
print(ind_slc[0:2])
print(ind_slc[[0,2]])

print(ind_slc[:,1])
print(ind_slc[:,2:5])
print(ind_slc[:,[0,2,4]])





# Shallow copies/Views:

shallow = np.arange(1,6)
print(shallow)
shallow2 = shallow.view()
print(shallow2)
shallow[2] = 1000
print(shallow,'\t',shallow2)
shallow2[2] = 3
print(shallow,'\t',shallow2)

shallow2 = shallow[0:3]
print(shallow2)  
print(id(shallow) == id(shallow2))  # false tells that these are different objects
shallow[2] = 199
print(shallow,'\t',shallow2)  





# Deep Copies:

deep = np.arange(1,6)
deep2 = deep.copy()
print(deep)
deep[2] = 1000
print(deep,'\t',deep2)
deep2[2] = 212
print(deep,'\t',deep2)