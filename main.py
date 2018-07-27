<<<<<<< Updated upstream
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Andy!'


if __name__ == '__main__':
    app.run()
=======
from flask import Flaskimport requestsapp = Flask(__name__)@app.route('/')def hello_world():    requests.post(url='http://127.0.0.1:5000', data=None)    return 'Hello Tori!'if __name__ == '__main__':    app.run("0.0.0.0", port=22000)
>>>>>>> Stashed changes
