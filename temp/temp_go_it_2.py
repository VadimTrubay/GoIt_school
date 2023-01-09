# from pathlib import *
# import pprint
# p = Path("temp/").mkdir(parents=True, exist_ok=True)
# help(open)
# file = open('temp_go_it.py', 'r', encoding='UTF8')
# for line in file:
#     print(line)

# while True:
# data = file.read(1024)  # read chang
# data = file.readline()
# print(data)
# if not data:
#     break

# res = file.read(1)
# res = file.readline()
# pprint.pprint(res)

# file.close()
# print(file.name)
# print(file.closed)

# meneger context
# with open('temp_go_it.py', 'a', encoding='UTF8') as file:
#     print(file.readline()[-1])
# NAME = 'Last name'
# MAIL = 'Login email'
# with open('email.csv', 'r') as file:
#     with open('email.html', 'a') as html:
#         html.write('<ul>\n')
#         headers = []
#         for line in file:
#             data = line.split(',')
#             data[-1] = data[-1][:-1]
#             if not headers:
#                 headers = data
#                 mail_index = headers.index(MAIL)
#                 name_index = headers.index(NAME)
#                 continue
#             name = data[name_index]
#             mail = data[mail_index]
#             html.write(f'    <li><a href={mail}>{name}</a></li>\n')
#         html.write('<ul>\n')

# def total_salary(path):
#     fh = open(path, 'r')
#     sum = float(0)
#     while True:
#         line = fh.readline()
#         if not line:
#             break
#         a = line.split(',')
#         sum += int(a[1])
#     fh.close()
#     return sum
# print(total_salary('text.txt'))

# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     for i in employee_list:
#         for j in i:
#             fh.write(j + '\n')
#     fh.close()
# print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],
#                               'text.txt'))

# a = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# for i in a:
#     for j in i:
#         print(j)

# def read_employees_from_file(path):
#     fh = open(path, 'r')
#     lst = []
#     while True:
#         line = fh.readline()
#         if not line:
#             break
#         if '\n' in line:
#             lst.append(line[:-1])
#         else:
#             lst.append(line)
#     fh.close()
#     return lst
# print(read_employees_from_file('text.txt'))

# def add_employee_to_file(record, path):
#     fh = open(path, 'a')
#     fh.write(record + '\n')
#     fh.close()
# print(add_employee_to_file("Drake Mikelsson, 19", 'text.txt'))

# def get_cats_info(path):
#     with open(path, 'r') as fh:
#         a = []
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             l = line.split(',')
#             if '\n' in line:
#                 b = {'id': l[0], 'name': l[1], 'age': l[2][:-1]}
#             else:
#                 b = {'id': l[0], 'name': l[1], 'age': l[2]}
#             a.append(b)
#         return a
#
# print(get_cats_info('text.txt'))


# def get_recipe(path, search_id):
#     with open(path, 'r') as fh:
#         a = None
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             l = line.split(',')
#             if search_id in line:
#                 a = {'id': l[0], 'name': l[1], 'ingredients': [l[2], l[3], l[4][:-1]]}
#     return a
# print(get_recipe('text.csv', '60b90c3b13067a15887e1ae4'))


# def sanitize_file(source, output):
#     with open(source, 'r') as fh:
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             a = ''
#             for i in line:
#                 if i.isdigit():
#                     i = ''
#                     a += i
#                 else:
#                     a += i
#     with open(output, 'w') as data:
#         data.write(a)
# print(sanitize_file('text.txt', 'text1.txt'))

# def save_applicant_data(source, output):
#     with open(output, 'w') as fh:
#         for i in source:
#             p = ''
#             for j in i.values():
#                 p += str(j) + ','
#             fh.write(p[:-1] + '\n')

# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)

# s = "Привет!"
#
# utf8 = s.encode()
# print(utf8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'
#
# utf16 = s.encode('utf-16')
# print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'
#
# s_from_utf16 = utf16.decode('utf-16')
# print(s_from_utf16 == s)

# def is_equal_string(utf8_string, utf16_string):
#     utf8 = utf8_string.decode('utf-8')
#     utf16 = utf16_string.decode('utf-16')
#     return True if utf8.casefold() == utf16.casefold() else False

# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as fh:
#         for k, v in users_info.items():
#             f = f'{k}:{v}\n'
#             h = f.encode()
#             fh.write(h)
# save_credentials_users('text.bin',  {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'})

# def get_credentials_users(path):
#     with open(path, 'rb') as fh:
#         a = []
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             h = line.decode()
#             if '\n' in h:
#                 a.append(h[:-1])
#             else:
#                 a.append(h)
#     return a
# print(get_credentials_users('text.bin'))

# import shutil
# def create_backup(path, file_name, employee_residence):
#     p = path + '/' + file_name
#     with open(p, 'wb') as file_name:
#         for k, v in employee_residence.items():
#             f = (f'{k} {v}\n')
#             h = f.encode()
#             file_name.write(h)
#     archive_name = shutil.make_archive('backup_folder', 'zip', 'folder' )
#     return archive_name

# import shutil
#
# def unpack(archive_path, path_to_unpack):
#     p = path_to_unpack
#     shutil.unpack_archive(archive_path, p)

# import re
# def find_word(text, word):
#     a = re.search(f'{word}', text)
#     if a:
#         return {
#             'result': True,
#             'first_index': a.span()[0],
#             'last_index': a.span()[1],
#             'search_string': word,
#             'string': text
#         }
#     else:
#         return {
#             'result': False,
#             'first_index': None,
#             'last_index': None,
#             'search_string': word,
#             'string': text
#         }
#
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, "
#     "as a successor to the ABC programming language, and "
#     "first released it in 1991 as Python 0.9.0.", "Python"))

# import re
# def find_all_words(text, word):
#     a = re.findall(f'{word}', text, flags=re.IGNORECASE)
#     return a

# import re
# def replace_spam_words(text, spam_words):
#     l_1 = len(spam_words[0])
#     l_2 = len(spam_words[1])
#     p = re.sub(f'{spam_words[0]}', l_1 * '*', text, flags=re.IGNORECASE)
#     p = re.sub(f'{spam_words[1]}', l_2 * '*', p, flags=re.IGNORECASE)
#     return p
#
# print(replace_spam_words('Guido van Rossum began working on Python ', ['began', 'Python']))

# import re
# def find_all_emails(text):
#     result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9_.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', text)
#     return result
# print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))

# text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
# result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9_.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', text)
# print(result)


# import re
# def find_all_phones(text):
#     a = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{2}[-]\d{2}', text)
#     b = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{1}[-]\d{3}', text)
#     c = b + a
#     return c
# print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 '
#                       'aloha a@test.com abc111@test.com.net '
#                       '+380(67)111-777-777+380(67)777-77-787'))

# import re
# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r"\w{4,5}[:]{1}[/]{2}\w+[.]\w+[.]\w+|\w{4,5}[:]{1}[/]{2}\w+[.]\w+", text)
#     for match in iterator:
#         result.append(match.group())
#     return result
# print(find_all_links('The main search site in the world is '
#                      'https://www.google.com The main social '
#                      'network for people in the world is '
#                      'https://www.facebook.com But programmers '
#                      'have their own social network '
#                      'http://github.com There they share their code. '
#                      'some url to check '
#                      'https://www..facebook.com www.facebook.com '))

# def cost_delivery(quantity, *_, discount=0):
#     print(quantity)
#     fin_sum = (5 + 2 *(quantity - 1))
#     print(fin_sum)
#     fin_sum = fin_sum - (fin_sum * discount)
#     print(fin_sum)
#     return fin_sum
# cost_delivery(2, 1, 2, 3, discount=0.5)

# import os
# import time
#
# for i in range(10):
#     print(i)
#     time.sleep(1)
#     os.system('cls')

# a = open('wer.txt')
# # print(a.readline())
# # print(a.readline())
# # print(a.readline())
# import shutil
#
# from pathlib import Path
# from shutil import *
# Path(r'D:\work_it\GitHub\GoIt_school\vad_dir').mkdir()
# Path(r'D:\work_it\GitHub\GoIt_school\vad_dir').rmdir()

# p = Path('vad')
# p.mkdir()  # создание папки
# shutil.copy(r'D:\work_it\GitHub\GoIt_school\wer.txt',  # копирование файла
#          r'D:\work_it\GitHub\GoIt_school\vad')
# shutil.move(r'D:\work_it\GitHub\GoIt_school\wer.txt',  # перенос файла
#          r'D:\work_it\GitHub')


# src = 'path/to/file.txt'
# dst = 'path/to/dest_dir'
# shutil.copy(src, dst)

# def alphabet_soup(txt):
#     return ''.join(sorted(txt))
# print(alphabet_soup("привет")) # "веипрт"
#
# def alphabet_soup(txt):
#     a = []
#     b = ''
#     for i in txt:
#         a.append(ord(i))
#     a.sort()
#     for j in a:
#         b += chr(j)
#     return b
# print(alphabet_soup("привет")) # "веипрт"

# b = ''.join(sorted("привет"))
# print(b)

# import re
# name = 'длтамвыдз4837е()?57432!нр99'
# cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# translation = (
#     "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#     "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja")
#
# trans = {}
# for c, l in zip(cyrillic, translation):
#     trans[ord(c)] = l
#     trans[ord(c.upper())] = l.upper()
# new_name = name.translate(trans)
# new_name = re.sub(r'\W', '_', new_name)
# print(new_name)

# fh = open(r'..\files\text.txt')
# print(fh.read(12))  # read string from file
# print(fh.tell())  # search for cursor
# fh.seek(0)  # move cursor to beginning of file
# print(type(fh))  # type of file
# print(fh)
# print(fh.readlines())  # read lines from file
# print(fh.readline())  # read line from file
# fh.close()  # close file

# with open(r'..\files\logo.png', 'rb') as fh:
#     data = fh.read()
#     # print(len(data))
#     # d = data[:50]
# with open(r'..\files\new_logo.png', 'wb') as file:
#     file.write(data)

# import shutil
# print(shutil.make_archive('must', 'zip', r'\work_it\GitHub\GoIt_school\files\must_sort'))  # pack files
# shutil.unpack_archive('must.zip', r'\work_it\GitHub\GoIt_school\files\must_sort1')  # unpack files

# import shutil
# shutil.rmtree(r'\work_it\GitHub\GoIt_school\files\must_sort1')  # delete directory
# shutil.copy(r'\work_it\GitHub\GoIt_school\files\logo.png', r'\work_it\GitHub\GoIt_school\files\must_sort')  # copy files
# shutil.move(r'\work_it\GitHub\GoIt_school\temp\logo.png', r'\work_it\GitHub\GoIt_school\files\logo.png')  # move files


import utils
print(utils.FILE_VERSION)
utils.greeting('vad')
utils.summa(5, 6)
print(__name__)
# print(dir(utils))

# import  sys
# print(sys.builtin_module_names)
# print(sys.path)















































