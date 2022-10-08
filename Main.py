'''Main file of the program.'''


import random
import sys


def random_num():
    '''
    Generates random number between 1 and 9
    '''
    return random.randint(1, 9)


class Player:
    '''Class for the Player'''
    def __init__(self, nm) -> None:
        self.score = 0
        self.name = nm

    def update(self, score):
        '''Updates the score'''
        self.score += score

    def ret_name(self):
        '''Returns the name of player'''
        return self.name

    def ret_points(self):
        '''Returns the points of player'''
        return self.score


def calc(player, guess, number, case=0):
    '''Logic'''
    if guess == number:
        player.update(3)
        print("\nCorrect!!! Wery well played.....")

    elif abs(guess - number) <= 1:
        print("\nYou were very close, try again!!!")
        if case != 1:
            try:
                guess = int(input("\nEnter a number again : "))
            except ValueError:
                print("\nYour input is not a number, try with a number only!!!")
            calc(player, guess, number, 1)

    else:
        print(f"\nWrong guess , the answer was {number} better luck next time!!!")


def menu():
    '''Menu'''
    name = input("\nEnter your name : ")
    pls = Player(name)
    while True:
        print(f"\nWelcome {name} to Number Guesser Game")
        print("-"*15, "Menu", "-"*15)
        print("1    -->  Start Game")
        print("2    -->  Score")
        print("Else -->  Exit")
        try:
            inp = int(input("Enter : "))
        except ValueError:
            inp = -1

        if inp == 1:
            main(pls)
        elif inp == 2:
            print(f"\n{pls.ret_name()}'s Points : {pls.ret_points()}")
        else:
            print("\nThank you for playing this game!!!")
            sys.exit()


def main(pls):
    '''Main function'''
    cont = True
    input_num = 0
    while cont:
        rand_num = random_num()
        try:
            input_num = int(input("\nEnter a number : "))
        except ValueError:
            print("\nYour input is not a number, try with a number only!!!")
            #menu(pl)

        calc(pls, input_num, rand_num)
        i = input("\nDo you want to play again ? (Y/N) :")
        cont = bool(i.lower() == 'y')


if __name__ == "__main__":
    menu()
