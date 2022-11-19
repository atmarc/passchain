import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction
import requests as req
from hashlib import sha256

PROGRAM_WALLET = "ECLEFRP6UN52NJSY6XVXVGANU6KSATTPYQJE6R3UMUOKRBWMTQ4DUCZ6RY"
PROGRAM_PRIVATE_KEY = "qTUS9bltxHlxWCN+fmLSOqluyL9Nu7uO3tSq5IumOpQglkLF/qN7pqZY9et6mA2nlSBOb8QST0d0ZRyohsycOA=="
DUMMY_USER_WALLET = "YGWPQACTX7GL34Z7ZLMCTIFD7CP425L25GUOUHVCQ7F6JAWRYWLBKPIOCU"


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

def make_transaction(private_key, my_address, reciever_address, description):
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
    note = description.encode()

    unsigned_txn = transaction.PaymentTxn(my_address, params, reciever_address, amount, None, note)

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

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))

    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))

    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transfered: {} microAlgos".format(amount) )    
    print("Fee: {} microAlgos".format(params.fee) ) 


    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

def get_transactions_descriptions(user_address):
    base_url = "http://localhost:8980"
    url = f"{base_url}/v2/accounts/{user_address}/transactions"
    res = req.get(url)
    data = json.loads(res.text)
    if res.status_code != 200:
        raise "Coudn't retrieve transactions of the user."
    
    descriptions = []
    for transaction in data['transactions']:
        note = transaction['note']
        unencrypted_data = base64.b64decode(note).decode()
        descriptions.append(unencrypted_data)

    return descriptions

def encrypt(_id, user, password, key):
    payload = f'{_id},{user},{password}'
    encryptionKey = sha256(sha256(key))

    

    return payload



def decrypt(payload, key):
    hashlib.decode()
    



# description = "(user, pass)"
# make_transaction(PROGRAM_PRIVATE_KEY, PROGRAM_WALLET, DUMMY_USER_WALLET, description)

# print(get_transactions_descriptions(DUMMY_USER_WALLET))