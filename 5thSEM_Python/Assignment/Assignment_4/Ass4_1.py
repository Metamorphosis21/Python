def remove_tuples_of_length_k(tuple_list, k):
    return [tup for tup in tuple_list if len(tup) != k]

tuple_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10, 11), (12, 13, 14)]
k = int(input("Enter the length of tuples to remove: "))

result = remove_tuples_of_length_k(tuple_list, k)
print("Updated list:", result)
