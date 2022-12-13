import pathlib
import sys


def main():
    file_name = pathlib.Path(sys.argv[0])
    print(file_name.name)


if __name__ == '__main__':
    main()
