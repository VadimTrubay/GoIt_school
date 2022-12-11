def get_name():
    name = input('write your name: ')
    return name
def greeting(name):
    print(f'goodbye {name}')
def main():
    name = get_name()
    greeting(name)
main()