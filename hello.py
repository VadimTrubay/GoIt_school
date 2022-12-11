def get_name():
    name = input('write your name: ')
    return name


def greeting(name):
    print(f'hello {name}')


def main():
    name = get_name()
    greeting(name)


if __name__ == '__main__':
    main()
