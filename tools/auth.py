from rich.console import Console
from rich.live import Live
from re import fullmatch 
from tools.api import api_post
from tools.utils import update_config
from configparser import ConfigParser

def check(email):
    # Regex from geeksforgeeks.org
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return fullmatch(regex, email)
    

def login(config: ConfigParser):
    """
    login: Simple method to log-in into HTB Platform to get Bearer Token for API
    :param url: Url htb platform
    :param endpoint: Url login endpoint
    :return: True if successful, False otherwise or Bearer token if was enable
    """
    console = Console()

    url = config['htb']['api_url']
    endpoint = config['htb_auth']['login']
    headers = dict(config['htb_headers'])
    email = ''
    valid_email = None 

    while valid_email == None:
        email = console.input("[bold green]Please, enter your email: ")
        valid_email = check(email)

        if not valid_email: 
            console.print("[bold red]Invalid email, try again!")

    password = console.input("[bold green]Please, enter your password: ", password = True) 

    data = {
        "email": email,
        "password": password,
        "remember": "false"
        }
    
    response = ""
    access_token = ""
    update_bearer = False

    with console.status("[bold bright_cyan]Logging in...", spinner = "aesthetic") as status:
        response = api_post(url, endpoint, headers, data)
    
    if response.status_code != 200:
        return False

    console.print("[bold bright_green]Login successfully!")
    # Cast to json to access values
    response = response.json()
    access_token = response['message']['access_token']

    if not response['message']['is2FAEnabled']:
        return True

    # 2FA enabled
    if not verify_otp(config, access_token):
        return False

    console.print("[bold bright_green]Access token verified!")

    # Update Bearer token from config file
    access_token = "Bearer " + access_token
    update_bearer = update_config('config.cfg', 'htb_headers', 'authorization', access_token)    
    if not update_bearer:
        console.print("[bold bright_yellow]Everything is fine, we just couldn't update your access token in config file!")
    
    return True
    
def verify_otp(config: ConfigParser, access_token: str) -> bool:
    """
    verify_otp: Verify 2fa code in case was enabled
    :param config: Confi parser to get url, endpoint and headers.
    :param access_token: Bearer token from login successful
    :return: True if successful, False otherwise
    """
    console = Console()
    url = config['htb']['api_url']
    endpoint = config['htb_auth']['otp']
    headers = dict(config['htb_headers'])
    headers["Authorization"] = "Bearer " + access_token

    otp = console.input("[bold green]Please, enter your otp code: ")

    data = {"one_time_password" : otp}

    response = ""
    with console.status("[bold bright_cyan]Verifying 2FA code...", spinner = "aesthetic") as status:
        response = api_post(url, endpoint, headers, data)
    
    return response.status_code == 200
