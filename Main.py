import random


def Random_num():
    return random.randint(1, 10)


def main():
    # Todo: to print some welcome message
    # print("Welcome")
    cont = True
    while cont:
        num = Random_num()


if __name__ == '__main__':
    main()
