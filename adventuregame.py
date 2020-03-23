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
                " effective)dagger.")


intro()
