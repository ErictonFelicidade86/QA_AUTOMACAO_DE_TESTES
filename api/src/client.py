import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT_SECONDS", 10))

def get_headers():
    return {
        "Content-Type": "application/json",
    }

def get(path, params=None):
    """
    Realiza uma requisição GET para a BASE_URL + path
    """
    url = f"{BASE_URL}{path}"
    response = requests.get(url, headers=get_headers(), params=params, timeout=TIMEOUT)
    return response

def post(path, json=None):
    """
    Realiza uma requisição POST para a BASE_URL + path
    """
    url = f"{BASE_URL}{path}"
    response = requests.post(url, headers=get_headers(), json=json, timeout=TIMEOUT)
    return response

def _join(path: str) -> str:
    return f"{BASE_URL}{path if path.startswith('/') else '/' + path}"

def get(path, params=None):
    return requests.get(_join(path), headers=get_headers(), params=params, timeout=TIMEOUT)

def post(path, json=None):
    return requests.post(_join(path), headers=get_headers(), json=json, timeout=TIMEOUT)
