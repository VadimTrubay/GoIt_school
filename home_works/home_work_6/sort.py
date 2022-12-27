from pathlib import Path
from string import *
import sys

UPPER_CASE = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G',
              'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
              'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K',
              'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
              'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
              'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts',
              'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '',
              'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu',
              'Я': 'Ya'}

LOWER_CASE = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
              'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
              'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
              'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
              'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
              'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
              'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
              'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
              'я': 'ya'}

ascii_letters = ascii_lowercase + ascii_uppercase
ascii_letters += digits


def normalize():
    user_input = sys.argv[1]
    path = Path(user_input)
    if path.exists():
        items = path.glob('**/*')  # search all files
        for item in items:
            if item.is_dir():
                item = str(item.name)
                trans_string_dir = ''
                finaly_string_dir = ''
                for index, char in enumerate(item):
                    if char in LOWER_CASE.keys():
                        char = LOWER_CASE[char]
                    elif char in UPPER_CASE.keys():
                        char = UPPER_CASE[char]
                        if len(item) > index + 1:
                            if item[index + 1] not in LOWER_CASE.keys():
                                char = char.upper()
                        else:
                            char = char.upper()
                    trans_string_dir += char
                for j in trans_string_dir:
                    if j in ascii_letters:
                        finaly_string_dir += j
                    else:
                        finaly_string_dir += '_'
                print(finaly_string_dir)
            else:
                if item.is_file():
                    item = str(item.name)
                    trans_string_file = ''
                    finaly_string_file = ''
                    poz_symbol = item.rindex('.')
                    full_suffix = item[poz_symbol:]
                    new_name = item[:poz_symbol]
                    for index, char in enumerate(new_name):
                        if char in LOWER_CASE.keys():
                            char = LOWER_CASE[char]
                        elif char in UPPER_CASE.keys():
                            char = UPPER_CASE[char]
                            if len(item) > index + 1:
                                if item[index + 1] not in LOWER_CASE.keys():
                                    char = char.upper()
                            else:
                                char = char.upper()
                        trans_string_file += char
                    for j in trans_string_file:
                        if j in ascii_letters:
                            finaly_string_file += j
                        else:
                            finaly_string_file += '_'
                    finaly_string_file += full_suffix

                    print(finaly_string_file)


def main():
    normalize()

# poz_symbol = name.rindex('.')
# suffix = name[poz_symbol + 1:]
# if suffix in list_suffix:
# #    list_suffix = ['jpeg', 'png', 'jpg', 'svg', 'avi', 'mp4', 'mov',
#                    'mkv', 'doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx',
#                    'mp3', 'ogg', 'wav', 'amr', 'zip', 'gz', 'tar']
#
# def get_phone_numbers_for_countries(list_phones):
#     return_phones = {
#         'UA': [],
#         'JP': [],
#         'TW': [],
#         'SG': []
#     }
#     for i in list_phones:
#         b = sanitize_phone_number(i)
#         print(b)
#         if b.startswith('81'):
#             return_phones['JP'].append(b)
#             continue
#         if b.startswith('65'):
#             return_phones['SG'].append(b)
#             continue
#         if b.startswith('886'):
#             return_phones['TW'].append(b)
#             continue
#         if b.startswith('380'):
#             return_phones['UA'].append(b)
#             continue
#         else:
#             return_phones['UA'].append(b)
#     return return_phones

if __name__ == "__main__":
    main()
