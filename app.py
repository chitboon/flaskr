from flask import *
from persistence import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello %s' % 'xx'

@app.route('/create/<name>')
def create(name):
    create_user('1', name)
    return 'created %s' % name

@app.route('/get/<id>')
def get(id):
    name = get_user(id)
    return 'retrieved %s' % name

@app.route('/update/<name>')
def update(name):
    user = update_user('1', name)
    return 'updated %s' % user



if __name__ == '__main__':
    app.run()
