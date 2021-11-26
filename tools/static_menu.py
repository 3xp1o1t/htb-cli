from tools.generate_menu import print_menu
from machine import *

"""
TODO Tal vez esto se pueda simplificar usando una clase posteriormente generar metodos estaticos con el metodo getattr obtener la primera linea de su descripcion de DOC para generar el nombre y filtrarlos, posteriormente llamar el metodo, por el momento esta en el prototipo implementado, pero aqui hay que migrarlo.
"""

def default_menu(config, console):

    default_options = [
        '1. Machines', 
        '2. Challenges', 
        '0. Exit'
    ]

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
        '3. List all machines (slow)',
        '4. Search machine by filter (offline)',
        '5. Show spawned machine',
        '6. Spawn a new machine',
        '7. Stop spawned machine',
        '8. Send user flag',
        '9. Send root flag',
        '0. Back to Main Menu'
    ]

    while True:
        print_menu(console, default_options, 'Machine Menu')
        user_input = console.input("[bold cyan]Machine - [bold green] Option (default 1) > ")
        if user_input == '1' or user_input == '':
            list_ranking(config, console)
        elif user_input == '2':
            list_vip(config, console)

        elif user_input == '3':
            console.print('Option choice = 3')

        elif user_input == '4':
            console.print('Option choice = 4')

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