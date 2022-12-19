def counter_char(string):
    dict_counter = {}
    for char in string:
        try:
            count = dict_counter[char]
        except KeyError:
            count = 0
        count += 1
        dict_counter[char] = count
    return print(dict_counter)