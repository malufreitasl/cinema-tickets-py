import sqlite3
from menuLists import *
from menuInteractions import handle_payment, display_ticket
from menuOptions import *
import time

# Consult total tickets sold
def consult_total_tickets_sold():
    clear_screen()
    print("Consult Total Tickets Sold\n")

    try:
        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = """
        SELECT COUNT(*) as total_tickets_sold
        FROM ticket
        WHERE status LIKE 'paid';
        """
        cursor.execute(query)
        total_tickets_sold = cursor.fetchone()[0]

        clear_screen()
        print(f"Total Tickets Sold: {total_tickets_sold}")

        input("\nPress Enter to go back to the previous menu.")

    except sqlite3.Error as error:
        print(f"Error consulting total tickets sold: {error}")

    finally:
        if connection:
            connection.close()

# Display options for pending tickets
def display_pending_ticket_options(ticket_dict):
    clear_screen()
    print("Your ticket is in a pending status.\nDo you want to pay for it?")
    user_option = yes_no_menu(YES_NO_OPTIONS)
    time.sleep(1)

    if user_option == 1: 
        update_dict = handle_payment(ticket_dict)
        display_ticket(update_dict)

    elif user_option == 2: 
        print("Alright, here's your ticket")  
        time.sleep(1)
        display_ticket(ticket_dict)

    else:
        return

# Handle the ticket based on its status
def handle_ticket_status(ticket):
    if ticket["Status"] == "Pending":
        display_pending_ticket_options(ticket)
    else:
        display_ticket(ticket)  

# Consult ticket options based on the received code
def consult_ticket_options(ticket):
    clear_screen()
    print("You chose to consult your ticket\n")
    time.sleep(1)

    code = get_integer_input("Please enter your code: ", 1000000, 9999999)
    time.sleep(1)

    try:
        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = f"""SELECT movie, audio, hour, status, id, date 
                    FROM ticket WHERE id = '{code}';"""

        if cursor.execute(query):
            data = cursor.fetchone()
        ticket_list = list(data)

        i = 0
        for key in ticket:
            for i in range(len(ticket_list)):
                if ticket[key] == None:
                    ticket[key] = ticket_list[i]
                    ticket_list.remove(ticket_list[i])
                else:
                    continue
                i += 1

    except sqlite3.Error as error:
        print(f"Error consulting sold tickets: {error}")

    finally:
        if connection:
            connection.close()

    handle_ticket_status(ticket)

# Display all tickets in the database
def display_all_tickets():
    try:
        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = "SELECT id, movie, audio, hour, status, date FROM ticket;"
        cursor.execute(query)
        reservas = cursor.fetchall()
        clear_screen()
        blue("TICKETS:\n")

        for reserva in reservas:
            reserva_id, filme, tipo_audio, horario, estado_reserva, data_compra = reserva
            print(f"Ticket ID: {reserva_id}")
            print(f"Movie: {filme}")
            print(f"Audio Type: {tipo_audio}")
            print(f"Hour: {horario}")
            print(f"Payment Status: {estado_reserva}")
            print(f"Purchase Date: {data_compra}")
            print("\n" + "-" * 40 + "\n")  

    except sqlite3.Error as error:
        print(f"Error fetching data from Reservas table: {error}")

    finally:
        if connection:
            connection.close()

    input("(Press Enter to go back)")

# Consult tickets sold by date
def consult_ticket_sold_by_date():
    clear_screen()
    blue("CONSULT DATE\n")
    day = get_integer_input("Enter a day: ", 1, 31)
    month = get_integer_input("Enter a month (numeric): ", 1, 12)
    year = get_integer_input("Enter a year: ", 2023, 3000)

    try:
        connection = sqlite3.connect('./cinema_tickets.db')
        cursor = connection.cursor()

        query = f"""
        SELECT *
        FROM ticket
        WHERE date = '{year}-{month}-{day}';
        """
        cursor.execute(query)
        total_tickets_by_date = cursor.fetchall()

        clear_screen()
        blue("TICKETS:\n")

        if total_tickets_by_date:
            for reserva in total_tickets_by_date:
                reserva_id, filme, tipo_audio, horario, estado_reserva, data_compra = reserva
                print(f"Reservation ID: {reserva_id}")
                print(f"Movie: {filme}")
                print(f"Audio Type: {tipo_audio}")
                print(f"Hour: {horario}")
                print(f"Payment Status: {estado_reserva}")
                print(f"Purchase Date: {data_compra}")
                print("\n" + "-" * 40 + "\n")  
        else:
            red("No tickets sold on the selected date\n")

        input("Press Enter to go back to the previous menu.")

    except sqlite3.Error as error:
        print(f"Error consulting sold tickets: {error}")

    finally:
        if connection:
            connection.close()
