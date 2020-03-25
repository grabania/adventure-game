import time
import random
import sys

sys.setrecursionlimit(1500)

enemy = ["dragon", "troll", "gorgon", "pirate"]
name = random.choice(enemy)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.7)


def enter_1_or_2():

    print_pause("(Please enter 1 or 2)\n")
    knock_or_peer = input()
    if knock_or_peer == '1':
        house()
        fight_or_run_away()
        final_question()
        intro()
    elif knock_or_peer == '2':
        cave()
        choice()
    else:
        enter_1_or_2()


def intro():
    print_pause("You find yourself standing in an open field"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + name + "is somewhere around"
                " here, and has been terrifying the nearby village.")
    print_pause("In front of you in the house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty(but not very"
                " effective)dagger.\n")


def choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    enter_1_or_2()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door"
                " opens and out steps a " + name + ".")
    print_pause("Eep! This is the " + name + "'s house!")
    print_pause("The " + name + " attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                " what with only having a tiny dagger.\n")


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the"
                " sword with you.")
    print_pause("You walk back out to the field.\n")


def fight():
    print_pause("You do your best...")
    print_pause("but your dagger is not match for the " + name + ".")
    print_pause("You have been defeated!")


def run_away():
    print_pause("You run back into the field. Luckily, "
                " you don't seem to have been followed.\n")


def fight_or_run_away():
    response = input("Would you like to (1) fight or (2) run away?")
    if response == '1':
        fight()
        final_question()
    elif response == '2':
        run_away()
        choice()
    else:
        final_question()


def final_question():
    print_pause("Would you like to play again? (y/n)")
    play_again()


def play_again():
    again = input().lower()
    if again == "n":
        print_pause("Thanks for playing! See you next time.")
    elif again == "y":
        print_pause("Excellent! Restarting the game...")
        play_game()
    else:
        final_question()


def play_game():
    intro()
    choice()
    play_again()


play_game()
