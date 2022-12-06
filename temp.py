# print('hello world', 1, 2, sep='\n')
# print('* ' * 5)
# print((5 * '# ' + '\n') * 5)
#
# a = ('# ' * 5) + '\n'
# for i in range(1, 5):
#     i = a * 5
# print(ord('q'))
# num = int(input("Enter the integer (0 to 100): "))
# sum = 1
# i = 1
# while i != num:
#     i += 1
#     sum = sum + i
#     print(sum)
# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))
# gcd = None
# if first < second:
#     gcd = first
# else:
#     gcd = second
# while first % gcd != 0 or second % gcd != 0:
#     gcd -= 1
# print(gcd)
# data = '25'
# print(data.isnumeric())
# number = int(input('Enter the: '))
# print(type(number))
#
# num = None
# sum = 0
# while num != 0:
#     num = int(input("Enter integer (0 for output): "))
#     for i in range(num + 1):
#         sum += i
#         # print(i)
#         print(sum)
#
# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for i in message:
#     if i.isupper():
#         c_unicode = ord(i)
#         c_index = ord(i) - ord("A")
#         new_index = (c_index + offset) % 26
#         new_unicode = new_index + ord("A")
#         new_character = chr(new_unicode)
#         encoded_message = encoded_message + new_character
#     elif i.islower():
#         c_unicode = ord(i)
#         c_index = ord(i) - ord("a")
#         new_index = (c_index + offset) % 26
#         new_unicode = new_index + ord("a")
#         new_character = chr(new_unicode)
#         encoded_message = encoded_message + new_character
#     elif i.isspace():
#         encoded_message = encoded_message + " "
#     elif i == "!":
#         encoded_message = encoded_message + "!"
# print(encoded_message)
# print(ord('A'))
# print(chr(65))
# try:
#     pool = 1000
#     quantity = int(input("Enter the number of mailings: "))
#     chunk = pool // quantity
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# result = None
# operand = None
# operator = None
# wait_for_number = True
#
# while True:
#     if operator == '=':
#         print(f"Result: {result}")
#         break
#     elif wait_for_number == True:
#         while True:
#             try:
#                 operand = float(input("Enter number: "))
#             except ValueError:
#                 print("Oops! It is not a number. Try again.")
#             else:
#                 if result == None:
#                     result = operand
#                 else:
#                     if operator == '+':
#                         result = result + operand
#                     elif operator == '-':
#                         result = result - operand
#                     elif operator == '*':
#                         result = result * operand
#                     elif operator == '/':
#                         result = result / operand
#                 break
#         wait_for_number = False
#     else:
#         while True:
#             operator = input("Enter one of operators +, -, *, /, =: ")
#             if operator in ('+', '-', '*', '/', '='):
#                 break
#             else:
#                 print("Oops! It is not a valid operator. Try again.")
#         wait_for_number = True

# import math
# print(math.ceil(2.1))
# print(math.floor(2.7))
# print(round(2.1))

# print('ltrh' not in 'Hello')
# operator = 4
# if operator == 4:
#     print('Hello')

# import re
# s = "I am 25 years old"
# age = re.search('\d+', s)
# print(age)

# age = 9
# if age % 2 == 0:
#     print('hello')
#     exit(4)
# print('vasia')

# number = int(input('Введите трехзначное число>: '))
# new_number_1 = number % 10
# print(new_number_1)
# temp_number = number // 10
# print(temp_number)
# new_numbers_2 = temp_number % 10
# print(new_numbers_2)
# new_numbers_3 = temp_number // 10
# print(new_numbers_3)
#
# print(f'Новое перевернутое число: {new_number_1}{new_numbers_2}{new_numbers_3}')

# first_haus = 3.5 * 50
# second_haus = 4 * 60
# count = 3 * 2 * 0.25
# finally_1 = first_haus // count
# finally_2 = second_haus // count
# print(finally_1, finally_2)

a = float(input('enter a: '))
b = float(input('enter b: '))
print(- b / a)
