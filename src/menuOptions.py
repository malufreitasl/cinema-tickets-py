import os
from colors import *
from menuLists import *

# Function to clear the command line
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to receive integer input
def get_integer_input(msg, min, max):
    while True:
        try:
            user_input = int(input(msg))
        except (ValueError, TypeError):
            red("ERROR! Insert a integer number")
        else:
            if user_input < min or user_input > max:
                red("ERROR! Options doesn´t exist")
            else:
                return user_input

# Function to print the lead menu and receive the user's choice
def lead_menu(menu):
    header_yellow("CINEMA TICKETS")
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    option = get_integer_input("Choose an option: ", 1, len(menu))
    return option

# Function to print ticket area options and receive the user's choice
def tickets_menu(menu):
    header_blue("ÁREA DE BILHETES")
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    option = get_integer_input("Choose an option: ", 1, len(menu))
    return option

# Function to print manager area options and receive the user's choice
def manager_menu(menu):
    header_cyan("MANAGEMENT AREA")
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    option = get_integer_input("Choose an option: ", 1, len(menu))
    return option

# Function to print movie options and receive the user's choice
def movies_menu(menu):
    header_blue("MOVIES")
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    option = get_integer_input("Choose an option: ", 1, len(menu))
    return option

# Function to print audio options and receive the user's choice
def audio_menu(menu, movie):
    print(line())
    purple(f"{movie}".center(40).upper())
    header_blue("AUDIO TYPE")
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    option = get_integer_input("Choose an option: ", 1, len(menu))
    return option

# Function to print hour options and receive the user's choice
def hour_menu(menu, movie, audio):
    print(line())
    purple(f"{movie}".center(40).upper())
    purple(f"{audio}".center(40).upper())
    header_blue("HOURS")
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    option = get_integer_input("Choose an option: ", 1, len(menu))
    return option

# Function to print payment options and receive the user's choice
def payment_menu(menu, ticket):
    print(line())
    purple(f"{ticket['movie']}".center(40).upper())
    purple(f"{ticket['audio']}".center(40).upper())
    purple(f"{ticket['hour']}".center(40).upper())
    header_green("PAYMENT")
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    payment_option = get_integer_input("Choose an option: ", 1, len(menu))
    return payment_option

# Function to print yes/no options and receive the user's choice
def yes_no_menu(menu):
    print(line())
    i = 1
    for item in menu:
        print("({}) {}".format(i, item))
        i += 1
    print(line())
    option = get_integer_input("Choose an option: ", 1, len(menu))
    return option
