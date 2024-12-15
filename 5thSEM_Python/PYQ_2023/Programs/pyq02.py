# def shift(str):
#     for i in range(0,6):
#         # shifted_str = str[i:] + str[:i]
#         # print(shifted_str)

# shift("SHIFT")
def shift(string):
    length = len(string)
    for i in range(length+1):
        shifted_str = ''
        for j in range(length):
            shifted_str += string[(i + j) % length]
        print(shifted_str)

shift("SHIFT")