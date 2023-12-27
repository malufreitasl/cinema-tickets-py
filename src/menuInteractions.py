from colors import *
from menuLists import *
from menuInteractions import *
from menuOptions import *
from ticketActions import *
from consultTickets import *
from ticketActions import create_ticket

# Actions of the main menu
def handle_main_menu_actions():
    while True:
        clear_screen()
        main_menu_option = lead_menu(MAIN_MENU_OPTIONS)

        if main_menu_option == 1:
            handle_buyer_menu_actions()

        elif main_menu_option == 2:
            handle_manager_menu_actions()

        else:
            clear_screen()
            print("Exiting the system... Goodbye!")
            return

# Actions of the buyer menu
def handle_buyer_menu_actions():
    while True:
        clear_screen()
        buyer_menu_option = tickets_menu(BUYER_MENU_OPTIONS)

        clear_screen()
        if buyer_menu_option == 1:
            update_ticket = create_ticket(current_ticket)
            if update_ticket is not None:
                result = display_ticket(update_ticket)
                if result:
                    break

        elif buyer_menu_option == 2:
            consult_ticket_options(current_ticket)

        elif buyer_menu_option == 3:
            break

# Actions of the manager menu
def handle_manager_menu_actions():
    while True:
        clear_screen()
        manager_menu_option = manager_menu(MANAGER_MENU_OPTIONS)

        if manager_menu_option == 1:
            display_all_tickets()

        elif manager_menu_option == 2:
            consult_total_tickets_sold()

        elif manager_menu_option == 3:
            consult_ticket_sold_by_date()

        elif manager_menu_option == 4:
            break
