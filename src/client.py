import requests

NBI_URL = "http://localhost:7557"

def list_devices():
    response = requests.get(f"{NBI_URL}/devices")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    devices = list_devices()
    for device in devices:
        print(device["_id"])