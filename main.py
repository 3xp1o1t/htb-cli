from tools.intro import intro
from tools.utils import read_config
from tools.auth import login
from rich.console import Console
from time import sleep

# Some bad programming practices ;(
console = None 
# load config
config = None

def check_login():
    """
    check_login: Verify if login was correct
    """
    is_logged = False
    while is_logged != True:
        is_logged = login(config)
        if is_logged:
            break;
        choice = console.input("[bold bright_red]Wrong email, password or OTP,please enter to try again or x to quit: ")
        if choice.lower() == 'x':
            break;
    
    sleep(2)
    console.clear()

def main():
    """
    main: Just a simple main function
    """
    intro()
    check_login()

# Initialize all stuff    
if __name__ == '__main__':
    console = Console()
    config = read_config('config.cfg')
    main()
