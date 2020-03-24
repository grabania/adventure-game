import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a gorgon is somewhere around"
                " here, and has been terrifying the nearby village.")
    print_pause("In front of you in the house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty(but not very"
                " effective)dagger.\n")


def first_choice():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door"
                " opens and out steps a troll.")
    print_pause("Eep! This is the troll's house!")
    print_pause("The troll attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                " what with only having a tiny dagger\n")


def second_choice():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the"
                " sword with you.")
    print_pause("You walk back out to the field.\n")


def third_choice():
    print_pause("You do your best...")
    print_pause("but your dagger is nit match for the dragon.")
    print_pause("You have been defeated!")


def fourth_choice():
    print_pause("You run back into the field. Luckily, "
                " you don't seem to have been followed.\n")


def fight_or_run_away():
    response = input("Would you like to (1) fight or (2) run away?")
    if response == '1':
        third_choice()
        final_question()


def choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    enter = input("(Please enter 1 or 2.)\n")
    if enter == '1':
        first_choice()
        fight_or_run_away()
        final_question()
        intro()
    elif enter == '2':
        second_choice()
        choice()
    else:
        enter


def final_question():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("Excellent! Restarting the game...")
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.\n")
    else:
        again


def play_game():
    intro()
    choice()
    final_question()


play_game()
