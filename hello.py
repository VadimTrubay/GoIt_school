def get_name():
    name = input('write your name: ')
    return name


def greeting(name):
    print(f'Hello {name}')

def main():
    name = get_name()
    greeting(name)


main()