def n_fibonacci(n):
    if n <= 0:
        return 0
    elif(n==1):
        return 1
    a,b=0,1
    for i in range(2,n):
        a,b=b,a+b
    print(b)
n_fibonacci(10)