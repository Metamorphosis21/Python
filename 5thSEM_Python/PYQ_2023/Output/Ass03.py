tup1=(1,2,3,4)
tup2=(2,3,4)
tup3=[i+j for i,j in zip(tup1,tup2)]
print(tup3)
# The list comprehension iterates over these pairs, adding the first element of each pair to the second element:
# For the pair (1, 2), it computes 1 + 2 = 3.
# For the pair (2, 3), it computes 2 + 3 = 5.
# For the pair (3, 4), it computes 3 + 4 = 7.
res=list(zip(tup1,tup2))
print(res)
# The zip() function pairs elements from tup1 and tup2 together, creating an iterable of tuples. For the given tuples, the pairs would be:
# (1, 2)
# (2, 3)
# (3, 4)
# Since tup2 has fewer elements than tup1, the zip() function stops when the shortest input iterable is exhausted


