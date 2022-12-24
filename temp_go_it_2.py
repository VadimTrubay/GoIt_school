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