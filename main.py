import sys
from hello import main as greeting
from bye import main as exiting


def main():
    try:
        if sys.argv[1] == 'greet':
            greeting()
        elif sys.argv[1] == 'goodbye':
            exiting()
        else:
            print('Unknown command')
    except IndexError:
        print('argument myst be great or goodbye')


if __name__ == '__main__':
    main()