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

# n = int(input('enter n: '))
# number = 0
# while number < n:
# 	number += 3
# 	print(number)

# a = int(input('enter a: '))
# b = int(input('enter b: '))
# n = a * '*'
# h = 0
# while h != b:
# 	h += 1
# 	print(n)

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

# a = float(input('enter a: '))
# b = float(input('enter b: '))
# print(- b / a)

# from decimal import Decimal
# sec = Decimal(input('enter the sec: '))
# hours = sec // Decimal(3600)
# hours_2 = hours * Decimal(3600)
# minutes = (sec - hours) // Decimal(60)
# seconds = sec - hours - (minutes * Decimal(60))
# print(hours, ':', minutes, ':', seconds)

# N = int(input('Enter N>: '))
# h = 1
# while N >= 1:
#     print((N - 1) * ' ' + h * '*')
#     h += 1
#     N -= 1
#
# num = int(input('enter num: '))
# print('even' if num % 2 == 0 else 'odd')

# arr = [34, 15, 88, 2]
# def sum_arr(arr):
#     sum = 0
#     for i in arr:
#         sum += i
#     print(sum)
# sum_arr(arr)

# if len(arr) == 1:
#     return arr[0]
# else:
#     return arr[0] + find_smallest_int(arr[1:])

# arr = [78, 56, 232, 12, -11, 43]
#
# def find_smallest_int(arr):
#     min_int = arr[0]
#     for i in arr:
#         if i < min_int:
#             min_int = i
#     return min_int
# print(find_smallest_int(arr))

# arr = [78, 56, 232, 12, -11, 43]
# print(min(arr))
#
# arr = [78, 56, 232, 12, -11, 43]
# arr.sort()
# print(arr[0])

# def football_points(wins, draws, losses):
#     sum = wins * 3 + draws * 1 + losses * 0
#     return sum
# print(football_points(3, 4 , 2))

# def are_numbers_equal(a, b):
#     return True if a == b else False

# def find_smallest_number(my_list):
#     a = my_list[0]
#     for i in my_list:
#         if i < a:
#             a = i
#     return a
#
# def less_than_100(a, b):
#     return True if (a + b) < 100 else False

# def difference(nums):
#     return max(nums) - min(nums)
# print(difference([10, 15, 20, 2, 10, 6]))

# def hello_name(name):
#     return f'Привет, {name}!'

# print(0/ 100)
# def divisible(num):
# 	return True if num / 100 == 0 or \
# 	num // 100 > 0 or num / 100 <= - 1 else False
# print(divisible(0))

# def is_empty(string):
# 	return False if string else True
# print(is_empty(' '))
#
# while True:
#     try:
#         age = int(input('How old are you?: '))
#         if age >= 18:
#             print('Access allowed')
#             break
#         else:
#             print('Access denied')
#             break
#     except ValueError:
#         print(f'age is not a number, please enter a number')
#     finally:
#         print('-' * 30)

# def divides_evenly(a, b):
#     return True if a % b == 0 else False
# print(divides_evenly(85, 4))

# def isEvenOrOdd(number):
# 	return 'четное' if number % 2 == 0 else 'нечетное'


# def greeting():
#     print('Hello world')
# greeting()

# print(bool(1 and 1))

# def flip_bool(boolean):
# 	return False if boolean == 1 else True

# default_name = 'Unknown'
# name = input('Please enter a name: ')
# current_name = name or default_name
# print(f'you name is {current_name}')

#
# while True:
#     name = input('Please enter a name: ')
#     print(name)
#     if not name:
#         print('end')
#         break # break or continue

# list_goods = ''
# while True:
#     goods = input('take a goods: ') + ',' + '\n'
#
#     if goods == 's' + ',' + '\n' :
#         new_list = list_goods[:-2]
#         break
#     list_goods += goods
#
# print(new_list)

# a = input('Enter a>: ')
# if a not in 'vadim':
#     print('yes')
# elif...:
#     pass
# else:
#     print('no')

# a = 'abcdefghijklmnopqrstuvwxyz'
# for latter in a:
#     print(latter)
#     if latter == 'b':
#         break
# print('end')


def google(number):

    for i in range(number):
        number -= 1
        print(f"G{'o' * number}gle")


google(10)
































