import requests
import json

# Try fetching subnet info from GitHub
r = requests.get("https://raw.githubusercontent.com/taostat/subnets-infos/main/subnets.json")
print(f"Status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    # Show first 3 entries
    for key in list(data.keys())[:3]:
        print(f"NetUID {key}: {json.dumps(data[key], indent=2)}")