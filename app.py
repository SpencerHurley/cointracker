from flask import Flask, Blueprint
from blockchain_api import get_address_info_from_blockchain 

addresses = Blueprint('addresses', __name__)

ADDRESS_DATA = {}

@addresses.post("/<address>")
def add_address(address):
    address_info = get_address_info_from_blockchain(address)
    ADDRESS_DATA[address] = {"address": address, "balance": address_info["final_balance"], "txs": address_info["txs"]}
    return ADDRESS_DATA[address]

@addresses.delete("/<address>")
def delete_address(address):
    if address in ADDRESS_DATA:
        del ADDRESS_DATA[address] 
    return {}

@addresses.post("/<address>/synchronize")
def synchronize(address):
    address_info = get_address_info_from_blockchain(address)
    ADDRESS_DATA[address] = {"address": address, "balance": address_info["final_balance"], "txs": address_info["txs"]}
    return ADDRESS_DATA[address]

@addresses.get("/<address>")
def get_address_data(address):
    return ADDRESS_DATA.get(address, {})

def create_app():
    app = Flask(__name__)
    app.register_blueprint(addresses, url_prefix='/addresses')
    return app

app = create_app()
