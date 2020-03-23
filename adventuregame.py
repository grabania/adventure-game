import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a gorgon is somewhere around"
                " here, and has been terrifying the nearby village.")
    print_pause("In front of you in the house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty(but not very"
                " effective)dagger.\n\n")


def first_choice():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door"
                " opens and out steps a troll.")
    print_pause("Eep! This is the troll's house!")
    print_pause("The troll attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                " what with only having a tiny dagger\n\n")


def second_choice():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the"
                " sword with you.")
    print_pause("You walk back out to the field.\n\n")


def choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    enter = input("(Please enter 1 or 2.)\n")
    if enter == 1:
        first_choice()
    elif enter == 2:
        second_choice()
    else:
        enter


def final_question():
    ask = input("Would you like to play again? (y/n)")
    if ask == ("y"):
        intro()
    elif ask == ("n"):
        print_pause("Thanks for playing! See you next time.")
    else:
        ask


intro()
choice()
first_choice()
second_choice()
