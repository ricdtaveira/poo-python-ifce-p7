from flask import Flask, url_for
from markupsafe import escape
from flask01.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Alô Mundo!'

@app.route('/login')
def login():
    return 'login'

@app.route('/todo')
def todo():
    return '<h1>Todo. Para fazer !</h1>'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Zé Mané'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
