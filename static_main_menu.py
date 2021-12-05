from tools.generate_menu import print_menu
from machines.static_machine_menu import machine_menu

def default_menu(config, console):
    default_options = [
        '1. Machines', 
        '0. Exit'
    ]
    console.clear()
    while True:
        print_menu(console, default_options, 'Main Menu')
        user_input = console.input("[bold green]Please, enter your option (default 1) > ")
        if user_input == '1' or user_input == '':
            machine_menu(config, console)

        elif user_input == '0':
            console.clear()
            return

        else:
            console.print("Invalid option, try again!", style="error")