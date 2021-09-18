from web3 import Web3

url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url))

print(web3.isConnected())
account_1 = "0xEaB919C8eF7abE79a5B3283cb16640653597baB2" 
account_2 = "0x24b4858110bB14f1d3510C65C2ec896C85606619"

private_key = "9ad0c028b907775b7f14dfe32a2c2257cd0713363a29cd55d5ec1f3b0c422c8f"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to' : account_2,
    'value' : web3.toWei(1, 'ether'),
    'gas' : 2000000,
    'gasPrice' : web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))