import random


def Random_num():
    return random.randint(1, 10)


def evaluate():
    pass


def main():
    # Todo: to print some welcome message
    # print("Welcome")
    cont = True
    while cont:
        num = Random_num()
        n = int(input("Enter a number : "))
        if evaluate(n, num):
            pass


if __name__ == '__main__':
    main()
