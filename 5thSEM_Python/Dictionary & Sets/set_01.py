# Sets
number={1,2,3,1,2,3,4,5,5}
print(number)
print(len(number))
print(4 in number)
print(14 in number)
for n in number:
    print(n,"- ",end="")

# Creating a set with built in function
num_list=[1,2,3,4,5,6,2,3,4,6,1]
num_tup=(1,2,3,4,5,6,2,3,4,6,1)
print(set(num_list))
print(set(num_tup))

text = 'to be or not to be that is the question'
u_words = set(text.split())
print(u_words)

print({1,3,5}=={3,1,5})
print({1,3,5}>{1,3})
print({1,3,5}.issuperset({1,3}))

set('abc def ghi jkl mno').issuperset('hi mom')