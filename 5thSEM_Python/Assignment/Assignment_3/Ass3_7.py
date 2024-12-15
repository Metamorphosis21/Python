def armstrong(num2):
    n=len(num2)
    num1=int(num2)
    s=0
    while(num1!=0):
        r=num1%10
        s+=r**n
        num1//=10
    if(s==int(num2)):
        print("Armstrong")
    else:
        print("not an armstrong number")
armstrong("1634")