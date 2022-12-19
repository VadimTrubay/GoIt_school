def counter_char(string):
    dict_counet = {}
    for char in string:
        try:
            count = dict_counet[char]
        except KeyError:
            count = 0
        count += 1
        dict_counet[char] = count
    return print(dict_counet)