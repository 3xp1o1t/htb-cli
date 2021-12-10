from tools.intro import intro
from tools.utils import read_config, read, log
from tools.auth import login
from static_main_menu import default_menu
from rich.console import Console
import signal

# A ctrl+c handler from code-maven.com
def handler(signum, frame):
    is_exiting = read('Ctrl + C was pressed. Do you really want to exit?', '', True)
    if is_exiting:
        exit(1)

signal.signal(signal.SIGINT, handler)

# Some bad programming practices ;(
console = Console()
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
        log("Wrong email, password or OTP, please enter to try again!", 'error', True)
    
    console.clear()

def main():
    """
    main: Just a simple main function
    """
    intro(console)
    check_login()
    default_menu(config, console)

# Initialize all stuff    
if __name__ == '__main__':
    main()
