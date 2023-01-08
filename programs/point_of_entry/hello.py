def get_name():
    name = input('write your name>: ')
    return name


def greet(name):
    print(f'hello {name}')


def main():
    name = get_name()
    greet(name)


if __name__ == '__main__':
    main()
