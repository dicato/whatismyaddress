from flask import Flask
from flask import request, Response


app = Flask(__name__)


@app.route('/')
def whatismyaddress():
    return Response(request.access_route[0].strip(),
                    mimetype='text/plain')

if __name__ == '__main__':
    app.run()
