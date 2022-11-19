from flask import Flask, request

from operations import get_transactions_descriptions

app = Flask(__name__)

@app.route('/getData', methods=['POST'])
def index():
    # {login: "", password: ""}

    transactions = get_transactions_descriptions()

if __name__ == '__main__':
    app.run()