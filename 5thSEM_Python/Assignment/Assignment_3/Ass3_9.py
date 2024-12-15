def calculator():
    operation = input("Enter operation (1 '+'/2 '-'/3 '*'/4 '/'): ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    match operation:
        case '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected.")
calculator()