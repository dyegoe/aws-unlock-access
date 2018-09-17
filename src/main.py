from flask import Flask
import random
import string

app = Flask(__name__)

s = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(256))


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/unlock/<code>')
def app_unlock(code):
    if code == s:
        return "Unlock successful"
    else:
        return "Wrong code"


if __name__ == '__main__':
    print(s)
    app.run(debug=True)
