from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from operations import get_transactions_descriptions, make_transaction, encrypt, decrypt
import json

app = Flask(__name__)
CORS(app, support_credentials=True)

PROGRAM_WALLET = "BMJ2K4ACQAZM7Z6CLJSWLC545WIU6NGZDBATIMOZUXSK3KJJ7323JJYT2A"
PROGRAM_PRIVATE_KEY = "G3aUhQI65xSnaiyeqjSwH7bYzLS7rba1/lqR+EleJzcLE6VwAoAyz+fCWmVli7ztkU802RhBNDHZpeStqSn+9Q=="
DUMMY_USER_WALLET = "Y5ZRFBIVK4TMPLZXWZAHQSQEYEFWDXL6CFAQC4DXPYC35KB55V263DHFAA"
DUMMY_MASTER_PASSWORD = "123456789"

@app.route('/createData', methods=['POST'])
def createData():
    body = json.loads(request.data)
    
    data = get_transactions_descriptions(body["login"])
    _id = len(data)

    print("Creating data - information recieved:", body["login"], body["username"], body["user_password"], body["master_password"])

    description = encrypt(_id, body["username"], body["user_password"], body["master_password"])

    make_transaction(PROGRAM_PRIVATE_KEY, PROGRAM_WALLET, body["login"], description)

    return "OK", 200

@app.route('/deleteData', methods=['POST'])
def deleteData():
    # {login: "", password: ""}
    login = request.args.get("login")
    password = request.args.get("password")
    index = request.args.get("index")
    
    return "" #overwrite the transaction with this Index with an emtpy one  createTransaction with new (user, pass) data


@app.route('/updateData', methods=['POST'])
def updateData():
    # {login: "", password: ""}
    login = request.args.get("login")
    password = request.args.get("password")
    index = request.args.get("index")
    username = request.args.get("username")
    password = request.args.get("password")

    return "" # overwrite the transaction with this Index with an emtpy one  "answer" # [(user1, pass1), (user2, pass2)]




@app.route('/getData', methods=['POST'])
@cross_origin(supports_credentials=True)
def getData():
    data = json.loads(request.data)

    print(data["login"], data["password"])
    encrypted_transactions = get_transactions_descriptions(data["login"])

    print(encrypted_transactions)

    data = [decrypt(elem.encode(), data["password"]) for elem in encrypted_transactions]

    return_data = []

    for elem in data:
        _id, user, password = elem.split(',')
        return_data.append({"_id": _id, "login": user, "password": password})

    print("Return values:", return_data)
    res = jsonify({"data": return_data})
    return res    

if __name__ == "__main__":
    app.run()