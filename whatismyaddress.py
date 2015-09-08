from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def whatismyaddress():
    return request.access_route[0]

if __name__ == '__main__':
    app.run()
