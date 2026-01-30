import time
from prometheus_client import start_http_server, Gauge
import api_calls

#metrics
BITAXE_HASHRATE = Gauge('btx_hashrate', 'bitaxe hashrate in GH/s')
BITAXE_TEMP = Gauge('btx_temperature', 'bitaxe temperature in Celsius')
BITAXE_FANSPD = Gauge('btx_fan_speed', 'bitaxe fan speed in %')
BITAXE_VOL = Gauge('btx_voltage', 'bitaxe voltage in V')
BITAXE_FRQ = Gauge('btx_frequency', 'bitaxe frequency in MHz')

INTERVAL = 60 # seconds

def start_prometheus():
    start_http_server(9090)
    while True:
        data = api_calls.get_system_info()
        if "error" in data:
            print(f"Error reading system info: {data['error']}")
            time.sleep(INTERVAL)
            continue

        BITAXE_HASHRATE.set(data["hashrate"], 0)
        BITAXE_TEMP.set(data["temperature"], 0)
        BITAXE_FANSPD.set(data["fan_speed"], 0)
        BITAXE_VOL.set(data["voltage"], 0)
        BITAXE_FRQ.set(data["frequency"], 0)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    start_prometheus()