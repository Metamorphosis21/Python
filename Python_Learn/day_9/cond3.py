st=int(input("enter your marks"))           # marks
if st >= 50:
    if st>=80:
        print("A")
    if st>=70 and st<80:
        print("B")
    if st>=60 and st<70:
        print("C")
    if st>=50 and st<60:
        print("D")
else:
    print("F")