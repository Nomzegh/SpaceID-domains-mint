import time
import asyncio
import json
import os

from web3 import Web3, HTTPProvider
from websockets import connect

# Connect to localhost node
HTTP_URL = 'http://127.0.0.1:8545'
WS_URL = 'ws://127.0.0.1:8546'
web3 = Web3(HTTPProvider(HTTP_URL))
print('Web3 connected:', web3.isConnected())
