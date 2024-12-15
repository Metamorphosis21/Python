a= {19, 22, 24, 20, 25, 26}
b= {19, 22, 20, 25, 26, 24, 28, 27}
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)
print(a.issubset(b))
print(a.isdisjoint(b))
print(a.difference(b))
print(a.symmetric_difference(b))
del c