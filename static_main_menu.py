from tools.generate_menu import print_menu
from machines.static_machine_menu import machine_menu
from tools.utils import log, read

def default_menu(config, console):
    default_options = [
        '1. Machines', 
        '0. Exit'
    ]
    console.clear()
    while True:
        print_menu(console, default_options, 'Main Menu')
        user_input = read("Please, type an option", '1')
        if user_input == '1':
            machine_menu(config, console)

        elif user_input == '0':
            console.clear()
            return

        else:
            console.clear()
            log('Invalid option, try again!', 'error')