# # Writing to a file: with statement
# with open('text_file.txt', mode = 'w') as wtxt:
#     wtxt.write('Text Content 01')
#     wtxt.write('\nText Content 02')
#     print('\nText Content 03', file = wtxt)

# with open('text_file.txt', 'w') as ftxt2:
#     ftxt2.write('New Text Content')

# # Reading from a text file:
# with open('text_file.txt', 'r') as rtxt:
#     for line in rtxt.readlines(30):
#         print(line)
        
# # Seeking to specfic file section:
# # file_object.seek(0)

# # Updating a file:
# rfile = open('text_file.txt', 'r')
# tempfile = open('temp_file.txt', 'w')
# with rfile, tempfile:
#     for line in rfile:
#         type , format , number = line.split()
#         if number!='02':
#             tempfile.write(line)
#         else:
#             newline = ' '.join(['Binary', format, number])
#             tempfile.write(newline+'\n')
 
# # Delete and Rename a file:
# import os
# os.remove('text_file.txt')
# os.rename('temp_file.txt', 'text_file.txt')

# # Serialization with JSON:
# account_directory = {
#     'accounts':[
#         {'ac_no':100, 'ac_name':'Honey', 'ac_balance':100.95},
#         {'ac_no':105, 'ac_name':'Baby', 'ac_balance':1100.95},
#         {'ac_no':110, 'ac_name':'Bae', 'ac_balance':10.55},
#         {'ac_no':115, 'ac_name':'Cutey', 'ac_balance':303.15},
#     ]
# }

# import json
# with open('accounts.json', 'w') as accounts:
#     json.dump(account_directory, accounts)
    
# # deserialization with JSON:
# with open('accounts.json', 'r') as accounts:
#     acc_file = json.load(accounts)
# print(acc_file)
# print(acc_file['accounts'])
# print(acc_file['accounts'][0])

# dispalying json text:
# with open('accounts.json', 'r') as accounts:
#     print(json.dumps(json.load(accounts), indent=4))

# Handling Execeptions:
# while True:
#     try:
#         n1 = int(input("Enter number 1:"))
#         n2 = int(input("Enter number 2:"))
#         res = n1/n2
#     except ValueError:
#         print("Both must be numbers")
#     except ZeroDivisionError:
#         print("Cannot divide by Zero")
#     else:
#         print(f"{n1:.3f}/{n2:.3f} = {res:.3f}")

# def try_it(value):
#     try:
#         x = int(value)
#     except ValueError:
#         print(f'{value} could not be converted to an integer')
#     else:
#         print(f'int({value}) is {int(value)}')
# try_it(10.7)
# try_it("Hello")

# try, except, else, finally clause
# try:
#     print('try suite that raises an exception')
#     int('hello')
#     print('this will not execute')
# except ValueError:
#     print('a ValueError occurred')
# else:
#     print('else will not execute because an exception occurred')
# finally:
#     print('finally always executes')

# Raising exception explicitly
# def fn1():
#     fn2()
# def fn2():
#     raise Exception("Explicitly raised Exception")
# fn1()