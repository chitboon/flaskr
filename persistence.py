import shelve
import uuid
from datetime import date
# today = str(date.today())

class User:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''

    def get_id(self):
        return self.__id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

class Blog:
    def __init__(self, id):
        self.id = id
        self.username = ''
        self.title = ''
        self.body = ''
        self.created = ''

users = shelve.open('user')
blogs = shelve.open('blog')

def create_blog(username, title, body):
    id = str(uuid.uuid4())
    blog = Blog(id)
    blog.title = title
    blog.username = username
    blog.body = body
    blog.created = str(date.today())
    blogs[id] = blog

def update_blog(blog):
    blogs[blog.id] = blog

def delete_blog(id):
    if id in blogs:
        del blogs[id]

def get_blogs():
    klist = list(blogs.keys())
    x = []
    for i in klist:
        x.append(blogs[i])
    return x

def get_blog(id):
    if id in blogs:
        return blogs[id]

def create_user(username, password):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_password(password)
    users[id] = user

def get_user(username, password):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), username, user.get_password(), password)
        if user.get_username() == username and user.get_password() == password:
            return user
    return None

def update_user(id, user):
    users[id] = user
    return users[id]

def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]

def clear_blog():
    klist = list(blogs.keys())
    for key in klist:
        del blogs[key]

def add_user(user):
    users[user.get_id()] = user

def init_db():
    clear_user()
    clear_blog()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))
        create_blog('user'+str(i), 'title'+str(i), 'body'+str(i))



