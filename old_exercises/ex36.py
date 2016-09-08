import os
os.system('clear')

def start_room():
    print "You find yourself in a dimly lit room."
    print "Which way do you go?"
    print "1. North"
    print "2. East"
    print "3. South"
    print "4. West"

    choice = raw_input('> ')

    if choice == "1":
        os.system('clear')
        north_room()
    elif choice == "2":
        os.system('clear')
        east_room()
    elif choice == "3":
        os.system('clear')
        south_room()
    elif choice == "4":
        os.system('clear')
        west_room()
    else:
        os.system('clear')
        print "You stumble around\n"
        start_room()


def north_room():
    print "You are standing at the edge of the abyss."
    print "What do you do?"
    print "1. Throw a rock in it."
    print "2. Run away."

    choice = raw_input('> ')

    if choice == "1":
        os.system('clear')
        print "You send ripples through all of space and time, and you die."
        exit(0)
    elif choice == "2":
        os.system('clear')
        print "RUN AWAY!\n"
        start_room()
    else:
        os.system('clear')
        print "You stand there gazing into the darkness.\n"
        north_room()


def east_room():
    print "You are in a room with a bear eating honey."
    print "What do you do?"
    print "1. Take the honey."
    print "2. Run away."

    choice = raw_input('> ')

    if choice == "1":
        os.system('clear')
        print "The bear eats you instead."
        exit(0)
    elif choice == "2":
        os.system('clear')
        print "RUN AWAY!\n"
        start_room()
    else:
        os.system('clear')
        print "You and the bear share a moment.\n"
        east_room()

def south_room():
    print "What's that?"
    print "1. What's what?"
    print "2. Look up."

    choice = raw_input('> ')

    if choice == "1":
        os.system('clear')
        print "You get crushed and die."
        exit(0)
    elif choice == "2":
        os.system('clear')
        print "You step back just in time to avoid getting crushed.\n"
        start_room()
    else:
        os.system('clear')
        print "SPLAT!"
        exit(0)


def west_room():
    print "You see a bright white light."
    print "Do you follow it?"
    print "1. yes"
    print "2. no"

    choice = raw_input('> ')

    if choice == "1":
        os.system('clear')
        print "You have found paradise, YOU WIN!"
        exit(0)
    elif choice == "2":
        os.system('clear')
        print "Light is over-rated anyway.\n"
        start_room()
    else:
        os.system('clear')
        print "That sure is a bright light.\n"
        west_room()

start_room()
