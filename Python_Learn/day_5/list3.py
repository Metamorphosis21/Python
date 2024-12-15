ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages),max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages)
sum=sum(ages)
print(sum)
print(len(ages))
print(sum/len(ages))
print(max(ages)-min(ages))

