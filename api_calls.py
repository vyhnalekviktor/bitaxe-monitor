import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

miner_ip = os.getenv("BITAXE_IP")
miner_address = f"http://{miner_ip}"

def get_system_info():
    try:
        response = requests.get(f"{miner_address}/api/system/info", timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Could not get sys info from {miner_address}, error: {e}"}


def get_asic_info():
    try:
        response = requests.get(f"{miner_address}/api/system/asic")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Could not get asic info from {miner_address}, error: {e}"}

print("Asic Info")
pprint(get_asic_info())

print("System info:")
pprint(get_system_info())