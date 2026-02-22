import requests

BASE_URL = "https://api.taostats.io/api"

def _get(endpoint, api_key, params=None):
    headers = {"Authorization": api_key}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def get_stats(api_key):
    return _get("/stats/latest/v1", api_key)

def get_tao_price(api_key):
    return _get("/price/latest/v1", api_key, params={"asset": "tao"})

def get_subnets(api_key):
    return _get("/subnet/latest/v1", api_key)

def get_tao_flow(api_key):
    return _get("/dtao/tao_flow/v1", api_key)

def get_subnet_identity(api_key):
    return _get("/subnet_identity/latest/v1", api_key)