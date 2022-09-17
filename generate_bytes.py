from web3 import Web3, HTTPProvider
from abi import contract_abi

HTTP_URL = 'url'
web3 = Web3(HTTPProvider(HTTP_URL))
print('Web3 connected:', web3.isConnected())
router = web3.eth.contract(address='0x6D910eDFED06d7FA12Df252693622920fEf7eaA6', abi=contract_abi)

def makeComm(nametag, acc_address, random_secret):
    x = router.functions.makeCommitment(nametag, acc_address, random_secret).call()
    print(x)
