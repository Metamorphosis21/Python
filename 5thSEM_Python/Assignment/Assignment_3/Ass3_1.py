def greatest_num(a):
    f=0
    s=0
    t=0
    while(a!=0):
        n=a%10
        a=a//10
        if(n>f):
            t=s
            s=f
            f=n
        elif(n>s and n!=f):
            t=s
            s=n
        elif(n>t and n!=s and n!=f):
            t=n
    print(f," , ",s," , ",t)
a=int(input("Enter the number: "))
greatest_num(a)