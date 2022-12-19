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

# from pathlib import Path
# print(Path())
# my_path = Path('D:\\work_it\\Github\\GoIt_school\\temp_go_it_1.py')
# my_path = Path('D:\\work_it\\Github')
# my_path = my_path.parent
# my_path = my_path.name
# my_path = my_path.suffix
# my_path = my_path.exists()
# my_path = my_path.is_dir()
# my_path = my_path.is_file()
# my_path = my_path.iterdir()
# for i in my_path.iterdir():
#     print(i)
# print(my_path)

# import sys
# print(sys.argv)

# word_map = []
# def print_map(word_map):
#     for row in word_map:
#         print(f'|{"|".join(row)}')
# word_map()

# from string import *
# alphabet = ascii_lowercase
# text = 'Lorem ipsum dolor sit amet ' \
#        'consectetur adipiscing elit ' \
#        'sed do eiusmod'
# words = []
# start = 0
# for index, char in enumerate(text):
#     if not char.lower() in alphabet:
#         word = text[start:index]
#         words.append(word.strip())
#         start = index
# print(words)

from counter_char import *
text = 'Lorem ipsum dolor sit amet ' \
       'consectetur adipiscing elit ' \
       'sed do eiusmod'
counter_char(text)