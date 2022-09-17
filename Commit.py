from web3 import Web3, HTTPProvider
from eth_utils import to_bytes
from abi import contract_abi


HTTP_URL = 'url'
web3 = Web3(HTTPProvider(HTTP_URL))
print('Web3 connected:', web3.isConnected())
contract = web3.eth.contract(address='0x6D910eDFED06d7FA12Df252693622920fEf7eaA6', abi=contract_abi)
commits = []


def commit_tx(acc, pkey, byt32):
    com_tx = contract.functions.commit(
        byt32
    ).buildTransaction({
        'nonce': web3.eth.getTransactionCount(acc),
        'gas': 300000,
        'gasPrice': web3.toWei(30, 'gwei'),
        'from': acc
    })
    signed_tx = web3.eth.account.sign_transaction(com_tx, pkey)
    commits.append(signed_tx)
    print('Signed')


def send_commit(signed):
    send_tx = web3.eth.sendRawTransaction(signed.rawTransaction)
    print(f'Commit hash: {web3.toHex(send_tx)}')


# Sign and send
commit_tx('address', 'private_key', 'secret без скобок')
for comm in commits:
    send_commit(comm)
    
