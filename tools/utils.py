from configparser import ConfigParser
from os import path
from sys import exit
from json import dump, load

"""
Collection of methods that works as helpers.
"""
# Bad programming practice, idk how to fix this.
SECTIONS = ['default', 'htb', 'htb_auth', 'htb_machine_api', 'htb_headers']

def read_config(filename: str) -> ConfigParser:
    """
    read_config: find and load the config.cfg file contents
    :param filename: file name to open
    :return: ConfigParser object
    TODO: 
        - Do something with global var
    """
    config = ConfigParser()

    if not path.exists(filename):
        exit(f"Error - {filename} not found!")

    config.read(filename)

    if len(config.sections()) != len(SECTIONS):
        exit("Error - Invalid config file!")

    for section in SECTIONS:
        if not config.has_section(section):
            exit(f"Error - Invalid {section} in config file!")

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