from tools.generate_menu import print_menu
from machines.machine import *

"""
Related methods for printing and performing operations with the machines.
"""

def machine_menu(config, console):
    default_options = [
        '1. List ranking machines',
        '2. List vip machines (slow)',
        '3. Update machine list (slow, store to file)',
        '4. Search machine by filter (offline)',
        '5. Show spawned machine',
        '6. Stop spawned machine',
        '7. Spawn a new machine',
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
            spawn_machine(config, console)

        elif user_input == '2':
            list_vip(config, console)
            spawn_machine(config, console)

        elif user_input == '3':
            list_all(config, console)

        elif user_input == '4':
            search_machine_menu(config, console)

        elif user_input == '5':
            show_spawned_machine(config, console)

        elif user_input == '6':
            show_spawned_machine(config, console)

        elif user_input == '7':
            spawn_machine(config, console)

        elif user_input == '8':
            console.print('Option choice = 8')

        elif user_input == '8':
            console.print('Option choice = 8')

        elif user_input == '0':
            console.clear()
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
            spawn_machine(config, console)

        elif user_input == '2':
            search_by_filter(config, console, 'os')
            spawn_machine(config, console)

        elif user_input == '3':
            search_by_filter(config, console, 'ip')
            spawn_machine(config, console)

        elif user_input == '4':
            search_by_filter(config, console, 'difficultyText')
            spawn_machine(config, console)

        elif user_input == '5':
            search_by_maker(config, console)
            spawn_machine(config, console)

        elif user_input == '0':
            console.clear()
            return

        else:
            console.print("Invalid option, try again!", style="error")