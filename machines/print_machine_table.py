from time import sleep
from contextlib import contextmanager
from rich.live import Live
from rich.table import Table
from rich.align import Align
from rich import box

"""
Related methods for printing tables with machine information.
"""

# Controling animation duration
BEAT_TIME = 0.01

@contextmanager
def beat(length: int = 1) -> None:
    """
    beat works as a decorator for 'with'.
    """
    yield
    sleep(length * BEAT_TIME)

def print_table(console, machine_list, table_title):
    """
    print_machine: Draw a table with a simple animation for all machine list
    :param console: Console() from rich to print table
    :param machine_list: List of machine from a response
    """
    console.clear()
    table = Table(show_footer = True, box = box.ASCII)
    table_align = Align.left(table)
    column_titles = ['ID', 'Name', 'Os', 'IP', 'Points', 'Difficulty', 'User Owned?', 'System Owned?']
    column_styles = ['bright_cyan', 'bright_green', 'bright_yellow', 'bright_magenta', 'deep_sky_blue1', 'salmon1', 'white', 'white']
    column_align = ['center', 'left', 'left', 'left', 'center', 'left', 'center', 'center']
    total_user_owned = 0
    total_root_owned = 0

    # vertical_overflow = autoscroll when renderin, better if use show_footer = True
    with Live(table_align, console = console, screen = False, refresh_per_second = 12, vertical_overflow = 'visible'):

        #list_length: Column_titles = Column_styles = Column alignment - Probably a bad programming practice :(
        for value in range(len(column_titles)):
            with beat(10):
                table.add_column(column_titles[value], footer=column_titles[value], style = column_styles[value], justify = column_align[value], no_wrap = True)

        with beat(10):
            table.title = table_title

        for index in range(len(machine_list['info'])):
            user_owned = ":x:" 
            root_owned = ":x:"
            if machine_list['info'][index]['authUserInUserOwns'] is not None:
                user_owned = ":white_check_mark:"
                total_user_owned += 1

            if machine_list['info'][index]['authUserInRootOwns'] is not None:
                root_owned = ":white_check_mark:"
                total_root_owned += 1

            with beat(10):
                table.add_row(
                    str(machine_list['info'][index]['id']),
                    machine_list['info'][index]['name'],
                    machine_list['info'][index]['os'],
                    machine_list['info'][index]['ip'],
                    str(machine_list['info'][index]['points']),
                    machine_list['info'][index]['difficultyText'],
                    user_owned,
                    root_owned
                )
        
        with beat(10):
            table.border_style = "bright_cyan"

    console.print(f'[+] Total found: {index + 1}\t\t[+] Total User Owned: {total_user_owned}\t\t[+] Total Root Owned: {total_root_owned}', style = 'bold')
        
