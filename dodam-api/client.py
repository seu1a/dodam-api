import requests
from utils import Utils

class Client() :
    def __init__(self) :
        self.utils = Utils()
    
    def request(self, url, method, **kwargs) :
        return requests.request(
            method,
            url,
            headers=kwargs.get("headers", {}),
            json=kwargs.get("body", {})).json()["data"]
        