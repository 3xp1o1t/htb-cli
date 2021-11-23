from rich.live import Live
from rich.style import Style
from rich.console import Console
from contextlib import contextmanager
from time import sleep

@contextmanager
def beat(length: int = 1) -> None:
    """
    beat: To control animation time
    Function taken from rich docs.
    """
    yield
    sleep(length * 0.02)

def intro():
    """
    intro: Just prints an animated htb logo with some color
    """
    console = Console()
    console.clear()
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