from tools.utils import save_machine_list, load_machine_list
from tools.api import api_get, api_post
from tools.print_table import print_machine_table
from rich.style import Style

def list_ranking(config, console):
    """
    list_ranking: List ranking machines
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['active']
    headers = dict(config['htb_headers'])
    machine_list = api_get(url, endpoint, headers)

    print_machine_table(console, machine_list)
        
def list_vip(config, console):
    """
    list_vip: List retired machines
    """
    url = config['htb']['machine_url']
    endpoint = config['htb_machine_api']['retired']
    headers = dict(config['htb_headers'])
    machine_list = api_get(url, endpoint, headers)

    print_machine_table(console, machine_list)
