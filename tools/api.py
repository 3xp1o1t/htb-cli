from requests import post, get
"""
Related methods for submitting requests to the HTB V4 API
"""

def api_get(url: str, endpoint: str, headers: dict) -> list:
    """
    api_get: Make a get request to HTB API
    :param url: Target url to send request
    :param endpoint: API path to a specific resource
    :param headers: Headers http
    :return: Response result
    """

    return get(f"{url}{endpoint}", headers=headers, allow_redirects=False).json()

def api_post(url: str, endpoint: str, headers: dict, data: dict) -> list:
    """
    api_post: Send data through http POST to HTB API
    :param url: Target url to send request
    :param endpoint: API target path
    :param headers: Headers http
    :param data: Data to send
    :return: Response result
    """
    return post(f"{url}{endpoint}", headers=headers, data=data)