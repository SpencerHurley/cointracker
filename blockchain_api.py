import requests

def get_address_info_from_blockchain(address):
    r = requests.get(f"https://blockchain.info/rawaddr/{address}")
    return r.json()
