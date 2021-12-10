from tools.generate_menu import print_menu
from tools.utils import log, read
from machines.machine import *

"""
Related methods for printing and performing operations with the machines.
"""

def machine_menu(config, console):
    default_options = [
        '1. List ranking machines',
        '2. List vip machines (Slow)',
        '3. Update machine list (Slow, store data to file)',
        '4. Search machine by filter (Works offline)',
        '5. Machine options (Show/Stop/Send Flag)',
        '0. Back to Main Menu'
    ]
    console.clear()
    while True:
        print_menu(console, default_options, 'Machine Menu')
        user_input = read('Machine - Option', '1')
        if user_input == '1':
            list_ranking(config, console)

        elif user_input == '2':
            list_vip(config, console)

        elif user_input == '3':
            list_all(config, console)

        elif user_input == '4':
            search_machine_menu(config, console)

        elif user_input == '5':
            show_spawned_machine(config, console)

        elif user_input == '0':
            console.clear()
            return

        else:
            log('Invalid option, try again!', 'error')


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
        user_input = read('Machine Search by Filter', '1')
        if user_input == '1':
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
            console.clear()
            return

        else:
            log('Invalid option, try again!', 'error')