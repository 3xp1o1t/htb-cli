from tools.generate_menu import print_menu
from machines.machine import *

"""
Related methods for printing and performing operations with the machines.
"""

def default_menu(config, console):
    default_options = [
        '1. Machines', 
        '2. Challenges', 
        '0. Exit'
    ]
    console.clear()
    while True:
        print_menu(console, default_options, 'Main Menu')
        user_input = console.input("[bold green]Please, enter your option (default 1) > ")
        if user_input == '1' or user_input == '':
            machine_menu(config, console)

        elif user_input == '2':
            console.print("Loading challenges menu!", style="info")

        elif user_input == '0':
            return

        else:
            console.print("Invalid option, try again!", style="error")
        

def machine_menu(config, console):
    default_options = [
        '1. List ranking machines',
        '2. List vip machines (slow)',
        '3. Update machine list (slow, store to file)',
        '4. Search machine by filter (offline)',
        '5. Show spawned machine',
        '6. Spawn a new machine',
        '7. Stop spawned machine',
        '8. Send user flag',
        '9. Send root flag',
        '0. Back to Main Menu'
    ]
    console.clear()
    while True:
        print_menu(console, default_options, 'Machine Menu')
        user_input = console.input("[bold cyan]Machine - [bold green] Option (default 1) > ")
        if user_input == '1' or user_input == '':
            list_ranking(config, console)

        elif user_input == '2':
            list_vip(config, console)

        elif user_input == '3':
            list_all(config, console)

        elif user_input == '4':
            search_machine_menu(config, console)
        elif user_input == '5':
            console.print('Option choice = 5')

        elif user_input == '6':
            console.print('Option choice = 6')

        elif user_input == '7':
            console.print('Option choice = 7')

        elif user_input == '8':
            console.print('Option choice = 8')

        elif user_input == '8':
            console.print('Option choice = 8')

        elif user_input == '0':
            return

        else:
            console.print("Invalid option, try again!", style="error")


def search_machine_menu(config, console):
    default_options = [
        '1. Filter machines by Name',
        '2. Filter machines by OS',
        '3. Filter machines by IP',
        '4. Filter machines by Difficulty',
        '5. Filter machines by Creator',
        '0. Back to Machine Menu'
    ]
    console.clear()
    while True:
        print_menu(console, default_options, 'Machine Search Menu')
        user_input = console.input("[bold cyan]Machine Search - [bold green] Option (default 1) > ")
        if user_input == '1' or user_input == '':
            search_by_filter(config, console, 'name')

        elif user_input == '2':
            search_by_filter(config, console, 'os')

        elif user_input == '3':
            search_by_filter(config, console, 'ip')

        elif user_input == '4':
            search_by_filter(config, console, 'difficultyText')

        elif user_input == '5':
            search_by_maker(config, console)

        elif user_input == '0':
            return

        else:
            console.print("Invalid option, try again!", style="error")