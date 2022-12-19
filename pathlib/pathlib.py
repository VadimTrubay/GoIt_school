import pathlib
import sys


def main():
    user_input = input('enter>: ')
    path = Path(user_input)
    if len(sys.argv) < 2:
        user_input = ''
    else:
        user_input = sys.argv[1]

    if path.exists():
        if path.is_dir():
            # items = path.iterdir()
            # items = path.glob('*.py')
            # items = path.glob('**/*')
            items = path.suffix
            for item in items:
                print(item)
        else:
            print(f'{path} is a file')
    else:
        print(f'{path.absolute()} is a not exists')


if __name__ == "__main__":
    main()
