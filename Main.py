import random


def Random_num():
    # Generates random number between 1 and 10
    return random.randint(1, 9)


def main():
    # Todo: to print some welcome message
    # print("Welcome")
    cont = True
    while cont:
        num = Random_num()
        n = int(input("\nEnter a number : "))

        if abs(n - num) <= 1:
            print("\nYou were very close try again!!!")

        elif n == num:
            print("\nCorrect!!! Wery well played.....")

        else:
            print(
                f"\nWrong guess , the answer was {num} better luck next time!!!")

        i = input("\nDo you want to play again ? (Y/N)")
        if i.lower() == 'y':
            cont = True
        else:
            cont = False


if __name__ == '__main__':
    main()
