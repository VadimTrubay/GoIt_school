from pathlib import *
from string import *
import sys

# UPPER_CASE = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G',
#               'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
#               'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K',
#               'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
#               'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
#               'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts',
#               'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '',
#               'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu',
#               'Я': 'Ya'}
#
# LOWER_CASE = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
#               'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
#               'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
#               'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
#               'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
#               'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
#               'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
#               'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
#               'я': 'ya'}
#
# ascii_letters = ascii_lowercase + ascii_uppercase
# ascii_letters += digits
#
#
# def normalize(arg):
#     trans_string = ''
#     finaly_string = ''
#     for index, char in enumerate(arg):
#         if char in LOWER_CASE.keys():
#             char = LOWER_CASE[char]
#         elif char in UPPER_CASE.keys():
#             char = UPPER_CASE[char]
#             if len(arg) > index + 1:
#                 if arg[index + 1] not in LOWER_CASE.keys():
#                     char = char.upper()
#             else:
#                 char = char.upper()
#         trans_string += char
#     for j in trans_string:
#         if j in ascii_letters:
#             finaly_string += j
#         else:
#             finaly_string += '_'
#     return finaly_string

dir_suff_dict = {"Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
                 "Documents": [".md", ".epub", ".txt", ".docx", ".doc", ".ods", ".odt", ".dotx", ".docm", ".dox",
                               ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".xml"],
                 "Archives": [".iso", ".tar", ".gz", ".7z", ".dmg", ".rar", ".zip"],
                 "Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"],
                 "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mpg", ".mpeg", ".3gp"],
                 "PDF": [".pdf"],
                 "HTML": [".html", ".htm", ".xhtml"],
                 "EXE_MSI": [".exe", ".msi"],
                 "PYTHON": [".py", ".pyw"]}


def sort_func(path):
    cur_dir = Path(path)
    if cur_dir.is_dir():
        for file in cur_dir.iterdir():
            if cur_dir.is_dir():
                sort_func(file)
            for suff in dir_suff_dict:
                if file.suffix.lower() in dir_suff_dict[suff]:
                    dir_img = cur_dir / suff
                    dir_img.mkdir(exist_ok=True)
                    file.rename(dir_img.joinpath(file.name))
    # if file.stat().st_size == 0:
    #     file.r mdir()



        # if file.is_dir():
        #     if file.stat().st_size == 0:
        #         file.rmdir()

def main():
    path = Path('\work_it\GitHub\GoIt_school\home_works\home_work_6\mess')
    # path = Path(sys.argv[1])
    if not Path(path).exists():
        print('[-] Директории не существует')
    else:
        sort_func(path)
    print('[!] Сортировка завершена')

#
#


    # print(path.absolute())
    # print(sort_dir_file(path))


# def scan_dir(path):
#     save_path = path
#     if path.exists():
#         if path.is_dir():
#             for file in path.iterdir():
#                 file = normalize(file)
#                 save_path.rename(file)
#             print(save_path)
#         else:
#             scan_dir(path)


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

#                 normalize(item)
#             elif item.is_file():
#                 item = str(item.name)
#                 poz_symbol = item.rindex('.')
#                 full_suffix = item[poz_symbol:]
#                 new_name = item[:poz_symbol]
#                 normalize(new_name + full_suffix)
#     return finaly_string
if __name__ == "__main__":
    main()
