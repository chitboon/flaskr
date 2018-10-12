import shelve

user = shelve.open('user')


def create_user(id, name):
    user[id] = name

def get_user(id):
    return user[id]

def update_user(id, name):
    user[id] = name
    return user[id]
