def number_length(num):
    # print(len(str(input("Enter a number: ")))) 
    c=0
    while(num!=0):
        x=num%10
        c=c+1
        num=num//10
    print(c)
num=int(input("Enter a number: "))
number_length(num)