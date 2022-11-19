from flask import Flask, request

from operations import get_transactions_descriptions

app = Flask(__name__)

@app.route('/getData', methods=['POST'])
def index():
    # {login: "", password: ""}

    # return get_transactions_descriptions("YGWPQACTX7GL34Z7ZLMCTIFD7CP425L25GUOUHVCQ7F6JAWRYWLBKPIOCU")
    return "{}"


if __name__ == '__main__':
    app.run()