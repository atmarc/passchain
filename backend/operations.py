import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction
import requests as req
from hashlib import sha256
from cryptography.fernet import Fernet


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

def make_transaction(private_key, my_address, reciever_address, description):
    print("MAKING TRANSACTION:",private_key, my_address, reciever_address, description)

    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    print("My address: {}".format(my_address))
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    # build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = constants.MIN_TXN_FEE 
    params.fee = 1000
    amount = 100000

    unsigned_txn = transaction.PaymentTxn(my_address, params, reciever_address, amount, None, description)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Signed transaction with txID: {}".format(txid))

    # wait for confirmation 
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print("Something went wrong with the transaction!\n", err)
        return

    print(confirmed_txn)

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))

    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))

    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transfered: {} microAlgos".format(amount) )    
    print("Fee: {} microAlgos".format(params.fee) ) 


    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

    account_info = algod_client.account_info(reciever_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

def get_transactions_descriptions(user_address):
    print("get_transactions_descriptions of", user_address)
    base_url = "http://131.159.14.109:8980"
    url = f"{base_url}/v2/accounts/{user_address}/transactions"
    res = req.get(url)

    data = json.loads(res.text)
    if res.status_code != 200:
        raise "Coudn't retrieve transactions of the user."
    
    print("Number of transactions:", len(data['transactions']))

    descriptions = []
    for transaction in data['transactions']:
        note = transaction['note']
        unencrypted_data = base64.b64decode(note).decode()
        descriptions.append(unencrypted_data)

    return descriptions

def encrypt(_id, user, password, key):
    payload = f'{_id},{user},{password}'
    encryptionKey = sha256(key.encode())
    safe = base64.urlsafe_b64encode(encryptionKey.digest())
    fernet = Fernet(safe)
    encMessage = fernet.encrypt(payload.encode())
    return encMessage

def decrypt(payload, key):
    encryptionKey = sha256(key.encode())
    safe = base64.urlsafe_b64encode(encryptionKey.digest())
    fernet = Fernet(safe)
    decMessage = fernet.decrypt(payload).decode()
    return decMessage
    


PROGRAM_WALLET = "BMJ2K4ACQAZM7Z6CLJSWLC545WIU6NGZDBATIMOZUXSK3KJJ7323JJYT2A"
PROGRAM_PRIVATE_KEY = "G3aUhQI65xSnaiyeqjSwH7bYzLS7rba1/lqR+EleJzcLE6VwAoAyz+fCWmVli7ztkU802RhBNDHZpeStqSn+9Q=="
DUMMY_USER_WALLET = "Y5ZRFBIVK4TMPLZXWZAHQSQEYEFWDXL6CFAQC4DXPYC35KB55V263DHFAA"
DUMMY_MASTER_PASSWORD = "123456789"


# description = encrypt(1, "user3", "pass3", DUMMY_MASTER_PASSWORD)

# make_transaction(PROGRAM_PRIVATE_KEY, PROGRAM_WALLET, DUMMY_USER_WALLET, description)

# -----------------

# encrypted_transactions = get_transactions_descriptions(DUMMY_USER_WALLET)

# print(encrypted_transactions)

# data = [decrypt(elem.encode(), DUMMY_MASTER_PASSWORD) for elem in encrypted_transactions]

# print(data)