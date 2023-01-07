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











































