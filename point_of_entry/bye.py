from hello import get_name


def goodbye(name):
    print(f'goodbye {name}')


def main():
    name = get_name()
    goodbye(name)


if __name__ == '__main__':
    main()
