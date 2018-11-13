from flask import *
from persistence import *
import functools

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view

@app.route('/init')
def init():
    init_db()
    return 'db initialised'

@app.route('/')
def index():
    if 'id' in session:
        posts = get_blogs()
        return render_template('index.html', posts = posts)
    else:
        return render_template('login.html')


@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('index'))
        flash(error)
    return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html')

@app.route('/<string:id>/update', methods=('GET', 'POST'))
def update(id):
    post = get_blog(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            update_blog(post)
            return redirect(url_for('index'))

    return render_template('update.html', post=post)

@app.route('/<string:id>/delete', methods=('GET', 'POST'))
def delete(id):
    delete_blog(id)
    posts = get_blogs()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            create_blog(session['user_name'], title, body)
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()



