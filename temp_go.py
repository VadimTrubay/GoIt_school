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

# def google(number):
#     for i in range(number):
#         number -= 1
#         print(f"G{'o' * number}gle")
# google(3)

# start = int(input('enter start>: '))
# stop = int(input('enter stop>: '))
# for i in range(start, stop + 1):
#     print(i, end=', ')

# def new_word(word):
# 	return word[::-1], word[1::]
# print(new_word('apple'))

# try:
# 	while True:
# 		print('end')
# 		int('asd')
# except KeyboardInterrupt or TypeError:
# 	print('wtf')
# except ValueError as error:
# 	print(error)

# try:
# 	int('asd')
# except (ValueError, TypeError, OverflowError):
# 	print('wtf')
# except:
# 	print('wtf!!!!!')

# while True:
# 	try:
# 		user_data = int(input('enter your old>: '))
# 	except ValueError as error:
# 		print(f'incorrect input, chould be {error}')
# 	else:
# 		break
# current_year = 2022
# year_of_birth = current_year - user_data
# print(year_of_birth)

# result = 0
# first = 1
# positions = 25
#
# print(f"step 0 = 0")
# for _ in range(first, positions):
# 	first, result = result, first + result
# 	print(f"step {i} = {result}")

# result = 0
# first = 1
# positions = 25
# for _ in range(0, 25):
# 	first, result = result, first + result
# print(first, result)

# while True:
# 	try:
# 		a = input('enter the numb>: ')
# 		int_a = int(a)
# 		if not int_a % 2:
# 			print("numb is even")
# 			continue
# 		else:
# 			print("numb is odd")
# 			continue
# 	except ValueError:
# 			print(f"{a} is not number")

# def NOT(num):
# 	return 1 if not num else 0
# print(NOT(0))

# def AND(num, num2):
# 	return 1 if num and num2 else 0
# print(AND(0, 0))
#
# def OR(num, num2):
#     return 1 if num or num2 else 0
# print(OR(0, 1))

# def distance_home(my_list):
#     return abs(sum(my_list))
# print(distance_home([-1, -4, -3, -2]))

# def should_serve_drinks(age, on_break):
#     return True if age >= 18 and not on_break else False
# print(should_serve_drinks(3, False))

# def flip(y):
# 	return 0 if y == 1 else 1

# def how_many_stickers(n):
#     return (n ** 2) * 6
# print(how_many_stickers(4))

# def inches_to_feet(inches):
#     return inches / 12 if inches >= 12 else 0

# def max_num(a, b):
#     if a > b:
#         print(f'max = a = {a}')
#     elif a < b:
#         print(f'max = b = {b}')
#     else:
#         print('a = b')
# max_num(3, 2)

# def total(*args):
#     for i in args:
#         print(i)
# print(total(10, 1, 2, 3, 4))
#
# def totall(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# print(totall(Jack=1123, John=2231, Inge=1560))

# def total(*tuples_1, **tuples_2):
#     print(tuples_1, tuples_2)
#     for it in tuples_1:
#         print(it)
# total(1, 2, 3, vad = 12, add = 23, vsub = 24 )

# my_tuple = tuple()
# another_tuple = ()
#
# empty_dict = {}
# another_empty_dict = dict()
#
# some_dict = {
#     "key": "value",
#     1: "one",
# }

# not_empty = {"key": "value"}
# not_empty["new_key"] = "new value"
# not_empty['1'] = '2'
# print(not_empty)

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         print(n)
#         return n * factorial(n - 1)
#
# print(factorial(5))

# import math
# sin_pi = math.sin(math.pi)
# print(sin_pi)

# from math import sin, pi
# sin_pi = sin(pi)
# print(sin_pi)

# def is_safe_bridge(s):
#     space = 0
#     for symbol in s:
#         if symbol.isspace():
#             space += 1
#     if space != 0:
#         return False
#     else:
#         return True
# print(is_safe_bridge('# ####'))

# def has_key(dictionary, key):
#     return True if key in dictionary else False
#
# print(has_key({"ночной": True, "дожор": True}, "дозор"))
# print(has_key({"кот": 1, "коt": "код", "рот": 3}, "код"))

# def how_many_potatoes(some_string):
#     a = some_string.split()
#     print(a)
#     b = 0
#     for i in range(len(a)):
#         if a[i] == 'картошка' or a[i] == 'картошка,':
#             b += 1
#     return b
# print(how_many_potatoes("лук, картошка, капуста, картошка, картошка"))

# def is_empty(dictionary):
#     return True if len(dictionary) == 0 else False
# print(is_empty({}))  # True
# print(is_empty({"a": 1}) ) # False

# def match(s1, s2):
#     s1 = s1.lower()
#     s2 = s2.lower()
#     return True if s1 == s2 else False
#
# print(match("привет", "прИВеТ")) # True
# print(match("кот", "код")) # False

# def last_ind(lst):
#     return lst[-1] if lst else None
#
#
# print(last_ind([0, 4, 19, 34, 50, -9, 2])) # 2
# print(last_ind("Серая лисичка перепрыгнула ленивую собаку")) # "у"
# print(last_ind([])) # None

# string = 'agsa'
# if string == string[:: -1]:
#     print('yes')
# else:
#     print('no')

# import random
# help(random)

# base_rate = 40
# price_per_km = 10
# total_trip = 0
# def trip_price(path):
#     global total_trip
#     total_trip += 1
#     total = base_rate + price_per_km * path
#     return float(total)
# trip_price(11)
# print(total_trip)

# def discount_price(price, discount):
#     price = int(price)
#     discount = float(discount)
#     def apply_discount():
#         nonlocal price
#         price = price - (price * discount)
#     apply_discount()
#     return price
# print(discount_price(200, 0.07))

# def get_fullname(first_name, last_name, middle_name = None):
#     if first_name and middle_name and last_name:
#         return f'{first_name} {middle_name} {last_name}'
#     elif first_name and last_name:
#         return f'{first_name} {last_name}'
# print(get_fullname('vad', 'trub', 'valent'))

# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     elif len(string) < length:
#         space = (length - len(string)) // 2
#         print(space)
#         string = ' ' * space + string
#         return  string
#         print(string)
# print(format_string(length=15, string='abaa'))

# def first(size, *poz_1):
#     return size + len(poz_1)
# def second(size, **poz_2):
#     return size + len(poz_2)
# first(5, "first", "second", "third")
# first(1, "Alex", "Boris")
# second(3, comment_one="first", comment_two="second", comment_third="third")
# second(10, comment_one="Alex", comment_two="Boris")


# def cost_delivery(quantity, *_, discount=0):
#     result = (5 + 2 * (quantity - 1)) * (1 - discount)  # решение с сайта
#     fin_sum =  (5 + 2 *(quantity - 1))  # мое решение
#     fin_sum = fin_sum - (fin_sum * discount)
#     return fin_sum
# print(cost_delivery(2, 1, 2, 3)) #== 7
# print(cost_delivery(3, 3)) #== 9)
# print(cost_delivery(1)) #== 5
# print(cost_delivery(2, 1, 2, 3, discount=0.5)) #== 3.5

# def factorial(a):
#     if a < 2:
#         return 1
#     else:
#         return a * factorial(a - 1)
#
# def number_of_groups(n, k):
#     res = factorial(n)/ (factorial(n - k) * factorial(k))  #Cnk = n! / ((n - k)! · k!)
#     return int(res)
#
# print(number_of_groups(50, 7))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(9))

# def amount_payment(payment):
#     result = 0
#     for i in payment:
#         if i > 0:
#             result += i
#     return result
#
# print(amount_payment([1, -2, 3, 4, -3, 8, -5, 9, -10, 11]))






