from time import sleep
from contextlib import contextmanager
from rich.live import Live
from rich.table import Table
from rich.align import Align
from rich import box

"""
Default file to print all functions related with tables and data 
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

def print_machine_table(console, machine_list):
    """
    print_machine: Draw a table with a simple animation for all machine list
    :param console: Console() from rich to print table
    :param machine_list: List of machine from a response
    """
    console.clear()
    table = Table(show_footer = False, box = box.ASCII)
    table_align = Align.left(table)
    column_titles = ['ID', 'Name', 'Os', 'IP', 'Points', 'Difficulty', 'User Owned?', 'System Owned?']
    column_styles = ['cyan', 'green', 'yellow', 'magenta', 'deep_sky_blue1', 'salmon1', 'white', 'white']
    column_align = ['center', 'left', 'left', 'left', 'center', 'left', 'center', 'center']

    with Live(table_align, console = console, screen = False, refresh_per_second = 60):

        #list_length: Column_titles = Column_styles = Column alignment - Probably a bad programming practice :(
        for value in range(len(column_titles)):
            with beat(10):
                table.add_column(column_titles[value], style = column_styles[value], justify = column_align[value], no_wrap = True)

        with beat(10):
            table.title = "HTB Ranking Machines"

        for index in range(len(machine_list['info'])):
            user_owned = ":x:" 
            root_owned = ":x:"
            if machine_list['info'][index]['authUserInUserOwns'] is not None:
                user_owned = ":white_check_mark:"

            if machine_list['info'][index]['authUserInRootOwns'] is not None:
                root_owned = ":white_check_mark:"

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

