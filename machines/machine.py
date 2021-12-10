from tools.utils import save_machine_list, load_machine_list, log, read
from tools.api import api_get, api_post
from machines.print_machine_table import print_table

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
    spawn_machine(config, console)
        
def list_vip(config, console):
    """
    list_vip: List retired machines
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['retired']
    headers = dict(config['htb_headers'])

    with console.status("[bold bright_cyan]Requesting vip machines", spinner = "aesthetic") as status:
        machine_list = api_get(url, endpoint, headers)

    print_table(console, machine_list, "HTB VIP Machines")
    spawn_machine(config, console)

def list_all(config, console):
    """
    list_all: Get and store all machines ranking/vip ones.
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['all']
    endpoint_active = config['htb_machine_api']['active']
    headers = dict(config['htb_headers'])

    with console.status("[bold bright_cyan]Updating machine list db", spinner = "aesthetic") as status:
        # First all available vip/no ranking free machines
        all_machine_list = api_get(url, endpoint, headers)
        # All ranking machines, for some reason /list/all don't return ranking machines.

        ranking_list = api_get(url, endpoint_active, headers)

        # Merge list 
        all_machine_list['info'].extend(ranking_list['info'])

        # Store list on file to use for search.
        save_machine_list(config['default']['machine_list'], all_machine_list)

    log(f"Total machines: {len(all_machine_list['info'])}", message_style = 'info')

    user_choice = read("Machine DB successfully updated!, Do you want to print the output?", '', is_confirm = True)
    if not user_choice:
        console.clear()
        return
    
    print_table(console, all_machine_list, "HTB All Machines")

def search_by_filter(config, console, filter):
    """
    search_by_filter: Search machines by filter in db file
    """
    # Dict with machine list from file machine.txt
    machine_list = load_machine_list(config['default']['machine_list'])

    user_choice = read(f"Please insert the {filter.capitalize()}", 'htb')

    if len(user_choice) < 1:
        log(f"Please, next time put something to search", message_style = 'warning')
        return

    # Search result = Dict like machine_list to reuse print_table
    search_result = {"info": []}

    for index in range(len(machine_list['info'])):
        if machine_list['info'][index][filter].lower() == user_choice.lower():
            # Make a copy of machine_list[][] list found to append like list to search_result[] dict.
            # if no make a copy() that would produce a reference to a Dict
            search_result['info'].append(machine_list['info'][index].copy())

    if len(search_result['info']) == 0:
        log(f"Sorry, nothing was found with * [bright_yellow]{user_choice}[/bright_yellow] * value!", message_style= 'error')
        return

    print_table(console, search_result, "Search results")
    spawn_machine(config, console)

def search_by_maker(config, console):
    """
    search_by_maker: Search machines by maker or maker 2 in db file
    Similar to search_by_filter, but this has an special sub value for maker2
    """
    # Dict with machine list from file machine.txt
    machine_list = load_machine_list(config['default']['machine_list'])

    user_choice = read(f"Please insert the creator username", '0xdf')
    if len(user_choice) < 1:
        log(f"Please, next time put something to search", message_style = 'warning')
        return

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
        log(f"Sorry, nothing was found with * [bright_yellow]{user_choice}[/bright_yellow] * value!", message_style= 'error')
        return

    print_table(console, search_result, f"Machines made by [bold bright_green]{user_choice}")
    spawn_machine(config, console)

def show_spawned_machine(config, console):
    """
    show_spawned_machine: Get spawned machine if exists
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['spawned']
    headers = dict(config['htb_headers'])

    machine_list = api_get(url, endpoint, headers)

    if machine_list['info'] is None:
        return False

    user_choice = read(f"[bright_yellow]* {machine_list['info']['name']} *[/bright_yellow] is currently active, do you want to send the flag?", '', True)

    if user_choice:
        send_flag(config, console, machine_list['info']['id'])

    user_choice = read(f"Would you like to turning off the [bright_yellow] * {machine_list['info']['name']} *[/bright_yellow] machine?", '', True)

    # Return true, if user send or not send a flag.
    if user_choice:
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

    with console.status("[bold bright_cyan]Turning off the machine", spinner = "aesthetic") as status:
        stop_machine = api_post(url, endpoint, headers, data)

    if stop_machine.status_code != 200:
        log("The machine could not be turned off. \n" + \
            f"Status code: {stop_machine.status_code}. \n" + \
                f"Status msg: {stop_machine.text}.", 
        message_style = 'warning')
        
        return

    log("Machine shut down successfully!", 'info')

def spawn_machine(config, console):
    """
    spawn_machine: Start and assing a machine to user
    :param machine_id: Required to search and start machine
    """
    url = config['htb']['vm_url']
    endpoint = config['htb_machine_api']['spawn']
    headers = dict(config['htb_headers'])

        #log("Sorry, you don't have any machine currently started!", message_style = 'warning')
    is_a_machine_running = show_spawned_machine(config, console)
    if is_a_machine_running:
        return

    user_choice = read('Do you want to start a machine?', '', True)

    if not user_choice:
        return

    machine_id = read('Please enter the machine id to start', 1)

    try:
        data = {'machine_id' : int(machine_id)}
    except ValueError:
        log('Invalid id, please verify the ID machine and use only numbers!', 'error')
        return

    with console.status("[bold bright_cyan]Turning on the machine", spinner = "aesthetic") as status:
        start_machine = api_post(url, endpoint, headers, data)

    if start_machine.status_code != 200:
        log(f"The machine could not be turned on.\n" + \
            f"Status code: {start_machine.status_code}.\n" + \
                f"Status msg: {start_machine.text}.",
                message_style = 'warning')
        return

    log("Machine started successfully!", message_style = 'info')

def send_flag(config, console, machine_id):
    """
    send_flag: Send User/Root flag
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['owned']
    headers = dict(config['htb_headers'])

    #my worst solution agains a re-input data problem :v 
    is_value_invalid = True
    while is_value_invalid:
        # User rating
        user_rating = read('Please rate the machine difficult between 10 and 100 using multiple of 10', '10')
        try:
            user_rating = int(user_rating)
        except ValueError:
            log('Invalid rating value, please verify your value and use only numbers (10, 20, ... 90, 100)!', 'error')
        else:
            if user_rating < 10 or user_rating > 100 or user_rating % 10 != 0:
                log(f"{user_rating} is invalid, please use an integer and multiple of 10 value. (10, 20, ... 90, 100)", 'error')
            else:
                is_value_invalid = False 
        
    # TODO -> code a way to verify a flag or something else.
    flag = read('Please enter the flag', '3x4mp13_f14g_5crypt_k1D_v')

    #if has a valid rating number
    data = {
        'id' : int(machine_id),
        'flag': flag.strip(),
        'difficulty': user_rating
    }

    with console.status('[bold bright_cyan]Sending flag', spinner = "aesthetic") as status:
        post_flag = api_post(url, endpoint, headers, data)
    
    if post_flag.status_code == 200:
        log("Flag sended successfully!", message_style = 'info')
        return
    
    if post_flag.status_code == 400:
        log("Incorrect Flag!", message_style = 'warning')
        return   

    log('An unknown error has occurred!\n' + \
        f'Status code: {post_flag.status_code}.\n' + \
            f'Status msg: {post_flag.text}.',
        message_style = 'error')
    return
