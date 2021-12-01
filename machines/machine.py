from rich import style
from tools.utils import save_machine_list, load_machine_list
from tools.api import api_get, api_post
from machines.print_machine_table import print_table
from rich.style import Style

"""
Related methods for playing the machines 
"""

def list_ranking(config, console):
    """
    list_ranking: List ranking machines
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['active']
    headers = dict(config['htb_headers'])

    with console.status("[bold bright_cyan]Requesting active machines", spinner = "aesthetic") as status:
        machine_list = api_get(url, endpoint, headers)

    print_table(console, machine_list, "HTB Ranking Machines")
        
def list_vip(config, console):
    """
    list_vip: List retired machines
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['retired']
    headers = dict(config['htb_headers'])

    with console.status("[bold bright_cyan]Requesting active machines", spinner = "aesthetic") as status:
        machine_list = api_get(url, endpoint, headers)

    print_table(console, machine_list, "HTB VIP Machines")

def list_all(config, console):
    """
    list_all: Get and store all machines ranking/vip ones.
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['all']
    endpoint_active = config['htb_machine_api']['active']
    headers = dict(config['htb_headers'])

    with console.status("[bold bright_cyan]Updating machine list db...", spinner = "aesthetic") as status:
        # First all available vip/no ranking free machines
        all_machine_list = api_get(url, endpoint, headers)
        # All ranking machines, for some reason /list/all don't return ranking machines.

        ranking_list = api_get(url, endpoint_active, headers)

        # Merge list 
        all_machine_list['info'].extend(ranking_list['info'])

        # Store list on file to use for search.
        save_machine_list(config['default']['machine_list'], all_machine_list)

    console.print(f"Total machines: {len(all_machine_list['info'])}", style = 'info')

    user_choice = console.input("[bold bright_green]Machine DB successfully updated!, Do you want to print the output? y/n: ")
    if user_choice.lower() != 'y':
        console.clear()
        return
    
    print_table(console, all_machine_list, "HTB All Machines")

def search_by_filter(config, console, filter):
    """
    search_by_filter: Search machines by filter in db file
    """
    # Dict with machine list from file machine.txt
    machine_list = load_machine_list(config['default']['machine_list'])

    user_choice = console.input(f"[bold bright_cyan]Please insert the {filter}: ")

    # Search result = Dict like machine_list to reuse print_table
    search_result = {"info": []}

    for index in range(len(machine_list['info'])):
        if machine_list['info'][index][filter].lower() == user_choice.lower():
            # Make a copy of machine_list[][] list found to append like list to search_result[] dict.
            # if no make a copy() that would produce a reference to a Dict
            search_result['info'].append(machine_list['info'][index].copy())

    if len(search_result['info']) == 0:
        console.print(f"Sorry, nothing was found with * {user_choice} * value!", style = 'error')
        return

    print_table(console, search_result, "Search results")


def search_by_maker(config, console):
    """
    search_by_maker: Search machines by maker or maker 2 in db file
    Similar to search_by_filter, but this has an special sub value for maker2
    """
    # Dict with machine list from file machine.txt
    machine_list = load_machine_list(config['default']['machine_list'])

    user_choice = console.input(f"[bold bright_cyan]Please insert the creator username: ")

    # Search result = Dict like machine_list to reuse print_table
    search_result = {"info": []}

    for index in range(len(machine_list['info'])):
        # Previous check if machine was made by 2 makers to apply doble filter
        # null = None, if we not apply this, an exception occur
        if machine_list['info'][index]['maker2'] != None:
            if machine_list['info'][index]['maker']['name'].lower() == user_choice.lower() or \
                machine_list['info'][index]['maker2']['name'].lower() == user_choice.lower():

                search_result['info'].append(machine_list['info'][index].copy())
        else:
            # if only has one creator
            if machine_list['info'][index]['maker']['name'].lower() == user_choice.lower():
                
                search_result['info'].append(machine_list['info'][index].copy())

    if len(search_result['info']) == 0:
        console.print(f"Sorry, nothing was found with * {user_choice} * value!", style = 'error')
        return

    print_table(console, search_result, f"Machines made by [bold bright_green]{user_choice}")

def show_spawned_machine(config, console):
    """
    show_spawned_machine: Get spawned machine if exists
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['spawned']
    headers = dict(config['htb_headers'])

    machine_list = api_get(url, endpoint, headers)

    if machine_list['info'] is None:
        console.print("Sorry, you don't have any machines currently started", style = 'info')
        return False
    
    console.print(f"[bold bright_red]{machine_list['info']['name']}[/] is currently active, do you want to turn it off? y/n: ", end = "", style = 'info')
    user_choice = console.input()

    if user_choice.lower() == 'y':
        stop_spawned_machine(config, console, machine_list['info']['id'])
    
    return True
    
def stop_spawned_machine(config, console, machine_id):
    """
    stop_spawned_machine: Shutdown assigned machine by id
    machine_id: Machine ID
    """

    url = config['htb']['vm_url']
    endpoint = config['htb_machine_api']['terminate']
    headers = dict(config['htb_headers'])

    data = {'machine_id' : int(machine_id)}

    with console.status("[bold bright_cyan]Turning off the machine...", spinner = "aesthetic") as status:
        stop_machine = api_post(url, endpoint, headers, data)

    if stop_machine.status_code != 200:
        console.print(f"The machine could not be turned off.", style = "warning")
        console.print(f"Status code: {stop_machine.status_code}.", style = "warning")
        console.print(f"Status msg: {stop_machine.text}.", style = "warning")
        return

    console.print("Machine shut down successfully!", style = 'info')

def spawn_machine(config, console):
    """
    spawn_machine: Start and assing a machine to user
    :param machine_id: Required to search and start machine
    """
    url = config['htb']['vm_url']
    endpoint = config['htb_machine_api']['spawn']
    headers = dict(config['htb_headers'])

    user_choice = console.input("[bright_cyan]Do you want to start a machine? y/n: ")

    if user_choice.lower() == 'n':
        return

    machine_id = console.input('[bright_cyan]Please enter the machine id to start: ')

    data = {'machine_id' : int(machine_id)}

    with console.status("[bold bright_cyan]Turning on the machine...", spinner = "aesthetic") as status:
        start_machine = api_post(url, endpoint, headers, data)

    if start_machine.status_code != 200:
        console.print(f"The machine could not be turned on.", style = "warning")
        console.print(f"Status code: {start_machine.status_code}.", style = "warning")
        console.print(f"Status msg: {start_machine.text}.", style = "warning")
        return

    console.print("Machine started successfully!", style = 'info')
