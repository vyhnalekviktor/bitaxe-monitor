import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

miner_ip = os.getenv("BITAXE_IP")
miner_address = f"http://{miner_ip}"


# GET requests
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

# dont really useful... uses RAM. must allow  'statsFrequency': 1 !!
def get_custom_stats(cols):
    # call: get_custom_stats( cols=["hashrate", "asicTemp", "power", "fanRpm"] )
    try:
        # Převede list na string: hashrate,asicTemp...
        query = ",".join(cols)
        response = requests.get(f"{miner_address}/api/system/statistics?columns={query}", timeout=5)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# POST requests
def restart():
    try:
        response = requests.post(f"{miner_address}/api/system/restart", timeout=5)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return {"error": f"Could not restart {miner_address}, error: {e}"}

# say "Hi!" on the device
def identify():
    try:
        response = requests.post(f"{miner_address}/api/system/identify", timeout=5)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return {"error": f"Could not identify {miner_address}, error: {e}"}

# PATCH requests

# TODO not tested yet
def update_settings(settings_dict):
    # call: update_settings( {"fan_speed": 50, "frequency": 525} )
    try:
        response = requests.patch(f"{miner_address}/api/system", json=settings_dict, timeout=5)
        response.raise_for_status()
        return response.json() if response.text else {"status": "success"}
    except Exception as e:
        return {"error": f"Could not update settings {miner_address}, error: {e}"}


# tests:
'''
print("Asic Info")
pprint(get_asic_info())
print("\n\n")

print("System info:")
pprint(get_system_info())
print("\n\n")

print(get_custom_stats( cols=["hashrate", "asicTemp", "power", "fanRpm"] ))
print("\n\n")


print("\n\n")
print(identify())
print("\n\n")
print(restart())
'''
