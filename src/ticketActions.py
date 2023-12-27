import random
import sqlite3
import time
from colors import *
from menuLists import *
from menuOptions import *
from menuInteractions import *
from datetime import date

# Function to create a ticket
def create_ticket(ticket_dict):
    while True:
        clear_screen()
        movie = movies_menu(MOVIE_OPTIONS)
        if movie == 5:
            movie = 0
            return
        ticket_dict["movie"] = MOVIE_OPTIONS[movie-1]

        while True:
            clear_screen()
            audio = audio_menu(AUDIO_OPTIONS, MOVIE_OPTIONS[movie-1])
            if audio == 3:
                audio = 0
                break
            ticket_dict["audio"] = AUDIO_OPTIONS[audio-1]

            while True:
                clear_screen()
                hour = hour_menu(HOUR_OPTIONS, MOVIE_OPTIONS[movie-1], AUDIO_OPTIONS[audio-1])
                if hour == 5:
                    hour = 0
                    break
                ticket_dict["hour"] = HOUR_OPTIONS[hour-1]

                ticket_dict["id"] = create_code()

                return handle_payment(ticket_dict)

# Function to create a ticket code
def create_code():
    while True:
        code = random.randint(1000000, 9999999)

        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = f"""
        SELECT id
        FROM ticket
        WHERE id = '{code}';
        """
        cursor.execute(query)
        result = cursor.fetchone()

        if result is None:
            connection.close()
            return code

# Function to display the ticket
def display_ticket(ticket):
    if ticket['movie'] is None:
        return True

    clear_screen()
    print("Here is your ticket:\n")

    header_blue("CINEMA TICKET")

    purple("Movie:".center(40).upper())
    print(f"{ticket['movie']}\n".center(40).upper())
    purple("Hour:".center(40).upper())
    print(f"{ticket['hour']}\n".center(39))
    purple("Audio:".center(40).upper())
    print(f"{ticket['audio']}".center(39).upper())
    print(line())

    if ticket['status'] == "pending":
        yellow("       Payment:        Code:".upper())
        print(f"       {ticket['status']}        {ticket['id']}")
    elif ticket['status'] == "paid":
        yellow("       Payment:        Code:".upper())
        print(f"        {ticket['status']}           {ticket['id']}")
    print(line())

    input("\n(Press enter to go back)")
    return True

# Function to handle cash payment and update ticket status
def handle_money_payment(ticket):
    print("...")
    time.sleep(1)

    clear_screen()
    print(line())
    purple(f"{ticket['movie']}".center(40).upper())
    purple(f"{ticket['audio']}".center(40).upper())
    purple(f"{ticket['hour']}".center(40).upper())
    print(line())

    print("You chose to pay with money")
    time.sleep(1)

    print("...")
    time.sleep(1)

    print("The total is 14,00€")
    time.sleep(1)

    input("(Press enter to pay))\n")

    clear_screen()

    green("Successfully paid!")
    time.sleep(1)

    input("\n(Press enter to continue)")

    ticket['status'] = "paid"

    return

# Function to handle card payment and update ticket status
def handle_card_payment(ticket):
    print("...")
    time.sleep(1)
    clear_screen()
    print(line())

    purple(f"{ticket['movie']}".center(40).upper())
    purple(f"{ticket['audio']}".center(40).upper())
    purple(f"{ticket['hour']}".center(40).upper())
    print(line())

    print("You chose card payment")

    time.sleep(1)
    print("...")
    time.sleep(1)

    print("The total is 14,00€")

    input("(Press enter to pay)")
    clear_screen()

    print("Processing...")
    time.sleep(2)
    clear_screen()

    green("Successfully paid!")
    time.sleep(1)

    input("\n(Press enter to continue)")

    ticket['status'] = "pending"

    return

# Function to handle payment options
def handle_payment(ticket_dict):
    while True:
        clear_screen()
        payment = payment_menu(PAYMENT_OPTIONS, ticket_dict)

        # If paying with cash
        if payment == 1:
            handle_money_payment(ticket_dict)
            ticket_dict["date"] = date.today()
            insert_into_database(ticket_dict)
            update_ticket_status(ticket_dict["id"], "paid")
            update_ticket_date(ticket_dict["date"], date.today())
            return ticket_dict

        # If paying with a card
        elif payment == 2:
            handle_card_payment(ticket_dict)
            ticket_dict["date"] = date.today()
            insert_into_database(ticket_dict)
            update_ticket_status(ticket_dict["id"], "paid")
            update_ticket_date(ticket_dict["date"], date.today())
            return ticket_dict

        # If not paying
        elif payment == 3:
            ticket_dict["date"] = date.today()
            ticket_dict["status"] = "pending"
            insert_into_database(ticket_dict)
            update_ticket_date(ticket_dict["date"], date.today())
            return ticket_dict

        # Go back
        elif payment == 4:
            return

# Function to update the ticket status in the database
def update_ticket_status(code, new_status):
    try:
        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = "UPDATE ticket SET status = ? WHERE id = ?"
        cursor.execute(query, (new_status, code))
        connection.commit()

    except sqlite3.Error as error:
        print(f"Error while trying to update ticket status: {error}")

    finally:
        if connection:
            connection.close()

# Function to update the ticket date in the database
def update_ticket_date(code, new_date):
    try:
        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = "UPDATE ticket SET date = ? WHERE id = ?"
        cursor.execute(query, (new_date, code))
        connection.commit()

    except sqlite3.Error as error:
        print(f"Error while trying to update ticket date: {error}")

    finally:
        if connection:
            connection.close()

# Function to insert ticket data into the database
def insert_into_database(ticket):
    try:
        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = "INSERT INTO ticket (movie, audio, hour, status, id, date) VALUES (?,?,?,?,?,?)"
        tuple_ticket = (ticket['movie'], ticket['audio'], ticket['hour'], ticket['status'], ticket['id'], ticket['date'])

        cursor.execute(query, tuple_ticket)
        connection.commit()

    except sqlite3.Error as error:
        print(f"Error while trying to insert ticket: {error}")

    finally:
        if connection:
            connection.close()