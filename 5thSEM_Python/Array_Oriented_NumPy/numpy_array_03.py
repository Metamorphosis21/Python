import numpy as np

# reshape vs resize
# reshape = np.array([[1,2,3],[4,5,6]])
# print(reshape)
# print(reshape.reshape(1,6))   # shallow copies
# print(reshape)
# print(reshape.resize(1,6))  # None
# print(reshape)

# flatten vs gravel
# flatten = np.array([[1,2,3],[4,5,6]])
# flatten2 = flatten.flatten()
# print(flatten,'\t',flatten2)
# flatten[1][2] = 1000
# flatten2[5] = 999
# print(flatten,'\t',flatten2)    # deep copies 
# ravel = np.array([[1,2,3],[4,5,6]])
# ravel2 = ravel.ravel()
# print(ravel,'\t',ravel2)
# ravel[1][2] = 1000
# ravel2[2] = 999
# print(ravel,'\t',ravel2)    # shallow copies

# Transposing rows and columns
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)  
# print('\n',arr.T)




# Horizontal and vertical stacking
# arr1 = np.array([[1,2,3],[6,7,8],[7,8,9]])
# arr2 = np.array([[10,11,12],[13,14,15],[16,17,18]])
# print(np.hstack((arr1,arr2)))   # must have same number of rows 
# print(np.vstack((arr1,arr2)))   # must have same numbers of column

a = np.arange(1, 7).reshape(2, 3)
print(a)
x = np.hstack((a,a))
x = np.vstack((x,x))
y = np.vstack((a,a))
y = np.hstack((y,y))
print(x,'\n\n',y)