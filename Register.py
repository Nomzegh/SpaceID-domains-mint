from web3 import Web3, HTTPProvider
from eth_utils import to_bytes
import abi


HTTP_URL = 'url'
web3 = Web3(HTTPProvider(HTTP_URL))
print('Web3 connected:', web3.isConnected())
contract = web3.eth.contract(address='0x6D910eDFED06d7FA12Df252693622920fEf7eaA6', abi=contract_abi)
commits = []
registers = []


def register_tx(nametag, value, secret, acc, pkey):
    reg_tx = contract.functions.register(
        nametag,
        acc,
        31536000,
        to_bytes(secret)
    ).buildTransaction({
        'nonce': web3.eth.getTransactionCount(acc),
        'gas': 300000,
        'gasPrice': web3.toWei(30, 'gwei'),
        'from': acc,
        'value': value
    })
    signed_register = web3.eth.account.sign_transaction(reg_tx, pkey)
    registers.append(signed_register)
    print('Signed')


def send_register(signed):
    send_reg = web3.eth.sendRawTransaction(signed.rawTransaction)
    print(f'Register hash: {web3.toHex(send_reg)}')


# Sign and send register

register_tx('domain', web3.toWei(0.6, 'ether'),  'secret без скобок', 'address', 'private_key')
for reg in registers:
    send_register(reg)
