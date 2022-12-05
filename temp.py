# # # # # # print('hello world', 1, 2, sep='\n')
# # # # # # print('* ' * 5)
# # # # # # print((5 * '# ' + '\n') * 5)
# # # # # #
# # # # # # a = ('# ' * 5) + '\n'
# # # # # # for i in range(1, 5):
# # # # # #     i = a * 5
# # # # # # print(ord('q'))
# # # # # num = int(input("Enter the integer (0 to 100): "))
# # # # # sum = 1
# # # # # i = 1
# # # # # while i != num:
# # # # #     i += 1
# # # # #     sum = sum + i
# # # # #     print(sum)
# # # # first = int(input("Enter the first integer: "))
# # # # second = int(input("Enter the second integer: "))
# # # # gcd = None
# # # # if first < second:
# # # #     gcd = first
# # # # else:
# # # #     gcd = second
# # # # while first % gcd != 0 or second % gcd != 0:
# # # #     gcd -= 1
# # # # print(gcd)
# # # data = '25'
# # # # print(data.isnumeric())
# # # number = int(input('Enter the: '))
# # # print(type(number))
# #
# # # num = None
# # # sum = 0
# # # while num != 0:
# # #     num = int(input("Enter integer (0 for output): "))
# # #     for i in range(num + 1):
# # #         sum += i
# # #         # print(i)
# # #         print(sum)
# #
# # message = input("Введите сообщение: ")
# # offset = int(input("Введите сдвиг: "))
# # encoded_message = ""
# # for i in message:
# #     if i.isupper():
# #         c_unicode = ord(i)
# #         c_index = ord(i) - ord("A")
# #         new_index = (c_index + offset) % 26
# #         new_unicode = new_index + ord("A")
# #         new_character = chr(new_unicode)
# #         encoded_message = encoded_message + new_character
# #     elif i.islower():
# #         c_unicode = ord(i)
# #         c_index = ord(i) - ord("a")
# #         new_index = (c_index + offset) % 26
# #         new_unicode = new_index + ord("a")
# #         new_character = chr(new_unicode)
# #         encoded_message = encoded_message + new_character
# #     elif i.isspace():
# #         encoded_message = encoded_message + " "
# #     elif i == "!":
# #         encoded_message = encoded_message + "!"
# # print(encoded_message)
# # print(ord('A'))
# # print(chr(65))
# # try:
# #     pool = 1000
# #     quantity = int(input("Enter the number of mailings: "))
# #     chunk = pool // quantity
# # except ZeroDivisionError:
# #     print('Divide by zero completed!')
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
from random import randint

while True:
    BOARD_SIZE = 3
    board = [i for i in range(9)]
    is_winner = False
    current_player = randint(0, 1)
    markers = {0: 'O', 1: 'X'}
    available_turns = (x for x in range(9))


    def draw_board():
        res = ""
        for i, v in enumerate(board):
            res += str(v) + " "
            if (i + 1) % BOARD_SIZE == 0:
                res += "\n"
        print(res)


    def validate(value=" "):
        if not value.isdigit() and int(value) not in available_turns:
            raise ValueError("Enter valid value and try again")
        if board[int(value)] in ('X', 'O'):
            raise ValueError("This value has already played")
        if '.' in value:
            raise ValueError('Number must be int')


    def check_winner():
        current_marker = markers[current_player]
        if board[0] == current_marker and board[4] == current_marker and board[8] == current_marker or \
                board[2] == current_marker and board[4] == current_marker and board[6] == current_marker or \
                board[0] == current_marker and board[1] == current_marker and board[2] == current_marker or \
                board[3] == current_marker and board[4] == current_marker and board[5] == current_marker or \
                board[6] == current_marker and board[7] == current_marker and board[8] == current_marker or \
                board[0] == current_marker and board[3] == current_marker and board[6] == current_marker or \
                board[1] == current_marker and board[4] == current_marker and board[7] == current_marker or \
                board[2] == current_marker and board[5] == current_marker and board[8] == current_marker:
            return True
        else:
            return False


    for i in range(9):
        try:
            input_error = True
            draw_board()
            while input_error:
                choice = input(f"Player {markers[current_player]} enter your number:\n")
                validate(choice)
                input_error = False
            board[int(choice)] = markers[current_player]
            if current_player == 1:

            # проверить победителя
                is_winner = check_winner()
            if is_winner == True:
                print(f'Player {markers[current_player]} won the game!!')
                break
            current_player = 0 if current_player == 1 else 1
            # if is_winner == True:
        except ValueError as ex:
            print(ex)

    if is_winner == False:
        print('Draw')
    replay = input("Желаете переиграть? (Y or N)")
    if replay == "Y":
        continue
    else:
        break