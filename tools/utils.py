from configparser import ConfigParser
from json import dump, load
from rich import print, box
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

"""
Collection of methods that function as helpers
"""

def read_config(filename: str) -> ConfigParser:
    """
    read_config: find and load the config.cfg file contents
    :param filename: file name to open
    :return: ConfigParser object
    """
    config = ConfigParser()
    config.read(filename)

    return config

def update_config(filename: str, section: str, option: str, new_value: str) -> bool:
    """
    update_config: Update a specific section in config file
    :param filename: Config file name to update
    :param section: Section name in file name 
    :param option: Option to set new value
    :param value: New value
    :return: True if successful, Exception otherwise
    """
    config = read_config(filename)
    config.set(section, option, new_value)

    with open(filename, 'w') as config_file:
        config.write(config_file)
    
    return True

def save_machine_list(filename: str, machine_list):
    """
    save_machine_list: Save all machine list into file 
    :param filename: Machine list file name to store data
    :machine_list: List of machine's
    :return: True if successful, Exception otherwise
    """
    with open(filename, 'w') as file_handle:
        dump(machine_list, file_handle)

    return True   

def load_machine_list(filename: str):
    """
    load_machine_list: Open and load machine list from file
    :param filename: Machine list file name with data
    :return: Machine list if successful, Exception otherwise
    """
    with open(filename, 'r') as file_handle:
        return load(file_handle)
    
def log(message, message_style, wait_for_input: bool = False):
    """
    log: Print formated log
    :param message: Message to print out
    :param message_style: Style message (error, info, warning)
    :param wait_for_input: In case user need to read the log obligatorily
    """
    style = {
        'info':'bold bright_cyan',
        'warning':'bold bright_yellow',
        'error':'bold bright_red'
    }
    print("\n", Panel.fit(message, box.DOUBLE_EDGE, title=message_style.upper(), border_style = style[message_style]), "\n")

    if wait_for_input:
        read('Press enter to continue', '[enter]')


def read(message, default_value, is_confirm: bool = False):
    """
    read: Read user input and return what reads or False
    :param message: Messate to prompt
    :param default_value: Default value in case user don't specify
    :param is_confirm: Confirm only have 2 choices, y/n
    """

    message = '[bold bright_green]' + message

    if is_confirm:
        is_yes = Confirm.ask(message)
        return is_yes

    user_choice = Prompt.ask(message, default = default_value)
    
    return user_choice
    
    


