from tools.intro import intro
from tools.utils import read_config
from tools.auth import login
from tools.static_menu import default_menu
from rich.theme import Theme
from rich.console import Console
from time import sleep

# log theme for warnings, errors and info
log_theme = Theme({
    "info": "bright_cyan",
    "warning": "bright_yellow",
    "error": "bold bright_red",
    "prompt": "bright_green",
})
# Some bad programming practices ;(
console = Console(theme=log_theme)
# load config
config = read_config('config.cfg')

def check_login():
    """
    check_login: Verify if login was correct
    """
    is_logged = False
    while is_logged != True:
        is_logged = login(config, console)
        if is_logged:
            break;
        choice = console.input("[bold bright_red]Wrong email, password or OTP,please enter to try again or x to quit: ")
        if choice.lower() == 'x':
            break;
    
    console.clear()

def main():
    """
    main: Just a simple main function
    """
    #intro(console)
    #check_login()
    default_menu(config, console)

# Initialize all stuff    
if __name__ == '__main__':
    main()
