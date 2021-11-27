from rich.table import Table
from rich.style import Style
from rich import box

"""
Simple method to print out static menus
"""

def print_menu(console, options, column_title):
    """
    print_menu: Metodo global para imprimir un menu en base a una lista
    :param console: Objeto console para imprimir menu
    :param options: Lista con las opciones de menu
    :param column_title: Titulo de la columna
    """
    table_header = Style(color = "bright_red", blink = True, bold = True)
    table_menu = Table(title = '[bright_magenta]HTB-CLI (Unofficial)', show_header = True, header_style = table_header, box = box.ASCII, style = "bright_cyan")

    table_menu.add_column(column_title, style = "bright_green")
    table_menu.add_row("") # Just to keep clean

    for option in options:
        table_menu.add_row(option)

    table_menu.add_row("")

    console.print(table_menu)