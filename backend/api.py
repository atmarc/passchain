from flask import Flask, request, jsonify
from operations import get_transactions_descriptions, make_transaction, encrypt, decrypt

app = Flask(__name__)

PROGRAM_WALLET = "ECLEFRP6UN52NJSY6XVXVGANU6KSATTPYQJE6R3UMUOKRBWMTQ4DUCZ6RY"
PROGRAM_PRIVATE_KEY = "qTUS9bltxHlxWCN+fmLSOqluyL9Nu7uO3tSq5IumOpQglkLF/qN7pqZY9et6mA2nlSBOb8QST0d0ZRyohsycOA=="
# DUMMY_USER_WALLET = "YGWPQACTX7GL34Z7ZLMCTIFD7CP425L25GUOUHVCQ7F6JAWRYWLBKPIOCU"
DUMMY_USER_WALLET = "A7NMWS3NT3IUDMLVO26ULGXGIIOUQ3ND2TXSER6EBGRZNOBOUIQXHIBGDE"

@app.route('/createData', methods=['POST'])
def createData():
    body = request.get_json()
    
    data = get_transactions_descriptions(body["login"])
    _id = len(data)

    description = encrypt(_id, body["username"], body["user_password"], body["master_password"])

    make_transaction(PROGRAM_PRIVATE_KEY, PROGRAM_WALLET, DUMMY_USER_WALLET, description)

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
def getData():
    body = request.get_json()

    print(body["login"], body["password"])
    encrypted_transactions = get_transactions_descriptions(body["login"])

    print(encrypted_transactions)

    data = [decrypt(elem.encode(), body["password"]) for elem in encrypted_transactions]

    return jsonify(data)
    

if __name__ == "__main__":
    app.run()