from Users import User, get_data


def register():
    name = input("enter your name: ")
    lastname = input("enter your lastname: ")
    email = input("enter your email address: ")
    username = input("enter username: ")
    password = input("enter password: ")
    user_obj = User(name, lastname, email, username, password)
    user_obj.set_into_json()
    return True


def login():
    username = input("enter your username: ")
    password = input("enter your password: ")
    all_users = get_data()
    k = 0
    for user in all_users:
        if user['username'] == username and user['password'] == password:
            return user['id']
        else:
            k += 1
    if k == len(all_users):
        return 0

def login_as_admin():
    username = input("enter your username: ")
    password = input("enter your password: ")
    all_users = get_data()
    k = 0
    for user in all_users:
        if user['username'] == username and user['password'] == password and user['role'] == 'admin':
            return user['id']
        else:
            k += 1
    if k == len(all_users):
        return 0
