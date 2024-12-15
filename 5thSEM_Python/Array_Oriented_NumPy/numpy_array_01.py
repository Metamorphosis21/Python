import numpy as np

# creating array with existing data

num = np.array([1,2,3,4,5])
num2d = np.array([[1,2,3],[4,5,6]])
print(type(num),"\t",num)
print(type(num2d),"\t",num2d)

np_array_list = np.array([e for e in range(2,20,2)]) # if e%2==0])
print(np_array_list)

np_arrya_2dlist = np.array([[e for e in range(2,11,2)],[e for e in range(1,10,2)]])
print(np_arrya_2dlist)




# array attributes

float = np.array([1.1,1.0,1.2,1.3,1.4,1.090])
print(float)        # does not show trailing 0s after decimal point

dtype = np.array([1,1.0,True])
print(num.dtype)        
print(float.dtype)   # determines the data type of the array
print(dtype.dtype)

print(num.ndim,'\t',num2d.ndim)
print(num.shape,'\t',num2d.shape)

print(num.size,'\t',float.size)
print(num.itemsize,'\t',float.itemsize,'\t',dtype.itemsize)

for row in num2d:
    for col in row:
        print(col,end=' ')
    print()
    
    
    
    
# filling arrays with specific values

zeros = np.zeros((5,5))     # by default, they are float data types but you change them to int using dtype
print(zeros)

ones = np.ones((2,4), dtype=int)
print(ones)

full = np.full((3,3), 15.5) 
print(full)




# creating arrays from ranges

range1 = np.arange(5)
range2 = np.arange(5,11)
range3 = np.arange(10,5,-1)
print(range1,'\n',range2,'\n',range3)
range4 = np.linspace(0,10,num=5)
print(range4)
range5 = np.arange(15000).reshape(500,30)
print(range5)


even_arange = np.arange(2,41,2).reshape(4,5)
print(even_arange)