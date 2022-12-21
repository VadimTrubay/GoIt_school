# def is_palindrome(word):
#     return True if word[::-1] == word else False
# print(is_palindrome("abba"))

# a = {'F': 'Unsatisfactorily',
#      'FX': 'Unsatisfactorily',
#      'E': ['Enough', 'Unsatisfactorily'],
#      'D': 'Satisfactorily',
#      'C': 'Good',
#      'B': 'Very good',
#      'A': 'Perfectly',
# 'discount': 50
# }
# print(a.get('discount', False))
# print(a['E'][1])
# for i in a:
#      print(a[i])

# students = [
#     {
#         'name': 'Petr',
#         'mark': {
#             '19.09': {
#                 'value': 80,
#                 'description': '...'
#             },
#             '29.09': {
#                 'value': 100,
#                 'description': None
#             },
#             '05.10': {
#                 'value': 99,
#                 'description': '...'
#             }
#         },
#         'email': 'petr@gmail.com',
#         'visits': [True, False, True, True],
#     },
#     {
#         'name': 'Vasya',
#         'mark': {
#             '19.09': {
#                 'value': 100,
#                 'description': '...'
#             },
#             '29.09': {
#                 'value': 100,
#                 'description': None
#             },
#             '05.10': {
#                 'value': 99,
#                 'description': '...'
#             }
#         },
#         'email': 'vasya@gmail.com',
#         'visits': [True, True, True, True],
#     },
# ]
#
# for name in students:
#     print(name['name'])

# def volume_of_box(sizes):
#     a = sizes.values()
#     result = 1
#     for i in a:
#         result = result * i
#         print(i)
#     return result

# def volume_of_box(sizes):
#     w, l, h = sizes.values()
#     return w * l * h
# print(volume_of_box({ "ширина": 2, "длина": 5, "высота": 1 }))

# from counter_char import *
#
# text = 'Lorem ipsum dolor sit amet ' \
#        'consectetur adipiscing elit ' \
#        'sed do eiusmod'
# counter_char(text)
#
# from char_set import *
#
# text = 'Quis autem vel eum iure reprehenderit, ' \
#        'qui in ea \\ voluptate velit esse, ' \
#        'quam nihil molestiae! consequatur, ' \
#        'vel illum, qui dolorem eum fugiat, ' \
#        'quo voluptas nulla pariatur? 33 ' \
#        'At vero eos et accusamus et'
# char_set(text)
#
# from cast_split import *
#
# text = 'Lorem ipsum, dolor sit amet ' \
#        'consectetur adipiscing elit ' \
#        'sed do eiusmod!!!'
# cast_split(text)

# которая принимает список (целые числа), находит среднее значение
# балла в списке и делит его на два списка. В первый попадают значения
# меньше среднего, включая среднее значение, а во второй — строго
# больше среднего. Функция возвращает кортеж этих двух списков.
# Для пустого списка возвращаем два пустых списка.
# def split_list(grade):
#     low = []
#     high = []
#     result = (low, high)
#     try:
#         average_value = sum(grade) / len(grade)
#     except ZeroDivisionError:
#         return result
#     average_value = round(average_value)
#     print(average_value)
#     for i in grade:
#         if i <= average_value:
#             low.append(i)
#         else:
#             high.append(i)
#         result = (low, high)
#     return low, high
# print(split_list([1, 7, 3, 4, 5, 6, 8, 2, 9, 12]))


# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9
# }
# def calculate_distance(coordinates):
#     result = 0
#     while len(coordinates) > 1:
#         a, b = coordinates[0], coordinates[1]
#         c = (a, b)
#         del coordinates[0]
#         for key, val in points.items():
#             if c[0] > c[1]:
#                 c = (b, a)
#             elif c == key:
#                 result += val
#     return result
# print(calculate_distance([0, 1, 3, 2, 0]))

# user_1 = {"name": "Jane", "age": 21}
# user_2 = {"name": "Moris", "age": 23}
# user_3 = {"name": "Steve", "age": 24}
#
# persons = [user_1, user_2, user_3]
#
# for user in persons:
#     for field in user:
#         print(user.get(field))

# def game(terra, power):
#     for i in terra:
#         for j in i:
#             if power >= j:
#                 power += j
#             else:
#                 break
#     return power
# print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))

# Убедитесь в том, что среди этих пин-кодов в списке
# не будет дубликатов, все они хранятся в виде строк,
# их длина равна 4 символам и содержат они только цифры
# def is_valid_pin_codes(pin_codes):
#     if len(pin_codes) < 1:
#         return False
#     for i in pin_codes:
#         if not type(i) == str:
#             return False
#         if len(i) != 4:
#             return False
#         if not i.isnumeric():
#             return False
#         if pin_codes.count(i) > 1:
#             return False
#     else:
#         return True
# print(is_valid_pin_codes(['0090', '9034', '0000']))

# from random import randint
#
# def get_random_password():
#     string = ''
#     for i in range(8):
#         random_num = randint(40, 126)
#         symbol = chr(random_num)
#         string += symbol
#     return string
# print(get_random_password())
#
# def is_valid_password(password):
#     u = 0
#     l = 0
#     dig = 0
#     for i in password:
#         if i.isdigit():
#             dig += 1
#         elif i.isupper():
#             u += 1
#         elif i.islower():
#             l += 1
#     if len(password) == 8 and u != 0 and l != 0 and dig != 0:
#         return True
#     else:
#         return False
# # print(is_valid_password('cSfg5yhd'))
#
# from random import randint


# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result
#
#
# def is_valid_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# def get_password():
#     i = 0
#     while i <= 100:
#         password = get_random_password()
#         print(password)
#         if is_valid_password(password):
#             return password
#         else:
#             continue
#
# print(get_password())
# from pathlib import Path
# print(Path())
# my_path = Path('D:\\work_it\\Github\\GoIt_school\\temp_go_it_1.py')
# my_path = Path('D:\work_it\Github')
# my_path = my_path.parent
# my_path = my_path.name
# my_path = my_path.suffix
# my_path = my_path.exists()
# my_path = my_path.is_dir()
# my_path = my_path.is_file()
# my_path = my_path.iterdir()
# for i in my_path.iterdir():
#     if not i.is_file():
#         print(i)
# print(my_path)

# import sys
# print(sys.argv)

# from pathlib import Path
# import pprint
#
# def parse_folder(path):
#     files = []
#     folders = []
#     p = Path()
#     for i in p.iterdir():
#         if i.is_dir():
#             folders.append(i.name)
#         else:
#             files.append(i.name)
#     return f'files = {files}', f'folders = {folders}'
#
# pprint.pprint(parse_folder('D:\work_it\Github\GoIt_school'))

# import sys
# def parse_args():
#     result = sys.argv[1:]
#     ' '.join(result)
#     return result
# print(parse_args())

# import sys
# print(sys.argv)