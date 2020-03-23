import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("In front of you are two passageways.")


intro()
