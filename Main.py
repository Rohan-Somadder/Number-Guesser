import random


def Random_num():
    # Generates random number between 1 and 10
    return random.randint(1, 10)


def main():
    # Todo: to print some welcome message
    # print("Welcome")
    cont = True
    while cont:
        num = Random_num()
        n = int(input("Enter a number : "))

        if abs(n - num) <= 1:
            print("You were very close try again!!!")

        elif n == num:
            print("Correct!!! Wery well played.....")

        else:
            print("Wrong guess , better luck next time!!!")

        i = input("Do you want to play again ? (Y/N)")
        if i.lower() == 'y':
            cont = True


if __name__ == '__main__':
    main()
