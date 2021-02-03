from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def home():
    return '<h1>Alô Mundo!</h1>'

@app.route('/todo')
def todo():
    return '<h1>Todo. Para fazer !</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')


