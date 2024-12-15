number = int(input("Enter a four-digit integer: "))

digit1 = number // 1000          
digit2 = (number % 1000) // 100  
digit3 = (number % 100) // 10    
digit4 = number % 10             

digit_sum = digit1 + digit2 + digit3 + digit4

print("The sum of the digits is:", digit_sum)
