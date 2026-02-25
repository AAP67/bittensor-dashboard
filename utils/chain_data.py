import requests
import time

BASE_URL = "https://api.taostats.io/api"

def _get(endpoint, api_key, params=None, retries=2):
    headers = {"Authorization": api_key}
    for i in range(retries + 1):
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 429 and i < retries:
            print(f"Rate limited on {endpoint} — waiting 30 seconds...")
            time.sleep(30)
            continue
        break
    return None

def get_stats(api_key):
    return _get("/stats/latest/v1", api_key)

def get_tao_price(api_key):
    return _get("/price/latest/v1", api_key, params={"asset": "tao"})

def get_subnets(api_key):
    return _get("/subnet/latest/v1", api_key)

def get_tao_flow(api_key):
    return _get("/dtao/tao_flow/v1", api_key)

def get_subnet_names():
    try:
        r = requests.get("https://raw.githubusercontent.com/taostat/subnets-infos/main/subnets.json")
        if r.status_code == 200:
            data = r.json()
            return {int(k): v.get("name", f"Subnet {k}") for k, v in data.items()}
    except:
        pass
    return {}