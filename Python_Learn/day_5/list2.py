t_cmp=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
t_cmp.sort()
print(t_cmp)
t_cmp.sort(reverse=True)
print(t_cmp)
print(t_cmp[0:3])
print(t_cmp[-1:-4:-1])
print(t_cmp[0:8:3])
t_cmp.pop(0)
print(t_cmp)
t_cmp.pop()
print(t_cmp)
del t_cmp[0:len(t_cmp)]
print(t_cmp)
del t_cmp

lst_1= ['HTML', 'CSS', 'JS', 'React', 'Redux']
lst_2= ['Node','Express', 'MongoDB']
lst_T=lst_1+lst_2
print(lst_T)
full_stack=['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,'python')
full_stack.insert(6,'sql')
print(full_stack)