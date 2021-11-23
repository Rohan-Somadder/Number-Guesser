import random


def Random_num():
    # Generates random number between 1 and 10
    return random.randint(1, 9)


def calc(guess, no, s=0):
    if abs(guess - no) <= 1:
        print("\nYou were very close try again!!!")

    elif guess == no:
        print("\nCorrect!!! Wery well played.....")
        if s != 1:
            try:
                no = int(input("\nEnter a number again : "))
            except ValueError:
                print("Your input is not a number, try with a number only!!!")
            calc(guess, no, 1)

    else:
        print(f"\nWrong guess , the answer was {no} better luck next time!!!")


def main():
    # Todo: to print some welcome message
    # print("Welcome")
    cont = True
    while cont:
        num = Random_num()
        try:
            n = int(input("\nEnter a number : "))
        except ValueError:
            print("Your input is not a number, try with a number only!!!")

        calc(n, num)
        i = input("\nDo you want to play again ? (Y/N)")
        cont = bool(i.lower() == 'y')


if __name__ == '__main__':
    main()
