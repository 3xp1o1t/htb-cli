from rich.live import Live
from rich.style import Style
from contextlib import contextmanager
from time import sleep

"""
Simple method to print an animated introduction to the HTB-CLI tool
"""

@contextmanager
def beat(length: int = 1) -> None:
    """
    beat: To control animation time
    Function taken from rich docs.
    """
    yield
    sleep(length * 0.02)

def intro(console):
    """
    intro: Just prints an animated htb logo with some color
    """
    logo_style = Style(color="bright_red", blink=True, bold=True)
    
    with Live(console=console, screen=False, refresh_per_second=60):
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠀⠀⠀⠀⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⣠⣤⣤⣄⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⠀⣀⣠⣶⣿⣿⣿⣿⣿⣿⣶⣄⣀⠀⠀⠈⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠐⠺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⠂⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣷⣦⣄⡀⠀⠀⠀⠈⠙⠋⠁⠀⠀⠀⢀⣠⣴⣾⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠉⠙⢿⣿⡇⠀⠀⢸⣿⡿⠋⠉⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠁⠀⠀⠈⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿", style=logo_style)
        with beat(10):
            console.print("[bold bright_green]\t H A C K  T H E  B O X  -  C L I")

    sleep(3)