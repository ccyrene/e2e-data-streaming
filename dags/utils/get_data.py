import requests

from typing import Dict

def get_data(url: str) -> Dict:
    
    response = requests.get(url).json()
    
    return response["results"][0]