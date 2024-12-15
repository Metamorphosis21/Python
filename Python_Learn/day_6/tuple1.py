tup=()
tup1=('amy','mary','yumeko','rosey')
tup2=('dazai','norm','light','subaru','kazuma')
tup3=tup1+tup2
print(tup3)
print(len(tup3))
lst3=list(tup3)
print(lst3)
lst3.append('loid') #type:ignore
lst3.append('yor')  #type:ignore
print(lst3)
tup3=tuple(lst3)
print(tup3)