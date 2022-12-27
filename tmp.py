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

#meneger context
with open('temp_go_it.py', 'r', encoding='UTF8') as file:
    print(file.readline())