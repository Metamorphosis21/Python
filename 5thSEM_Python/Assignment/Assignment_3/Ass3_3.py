def square_sum():
    s=0
    for i in range (1,51):
        if(i%2==0):
            s=s+i*i
    print(s)
square_sum()