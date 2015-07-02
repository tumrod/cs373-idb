from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, welcome to THE INTERGALACTIC DATABASE!'


if __name__ == '__main__':
    app.run()
