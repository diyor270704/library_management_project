import json
from json import JSONDecodeError


def get_data():
    try:
        with open("users.json") as f:
            all_users: list = json.load(f)
            f.close()
        return all_users
    except (JSONDecodeError, FileNotFoundError):
        with open("users.json", 'w') as f:
            json.dump([], f, indent=4)
            f.close()
        with open("users.json") as f:
            all_users: list = json.load(f)
            f.close()
        return all_users


class User:
    def __init__(self, name, lastname, email, username, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password

    def set_into_json(self):
        user: dict = {
            'id': 1 if len(get_data()) < 1 else len(get_data()) + 1,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'role': 'user'
        }
        if not self.isavailable():
            try:
                with open("users.json") as f:
                    all_users: list = json.load(f)
                    f.close()
                all_users.append(user)
                with open("users.json", "w") as f:
                    json.dump(all_users, f, indent=4)
                    f.close()
                print('registered successfully :)')
            except (JSONDecodeError, FileNotFoundError):
                with open("users.json", "w") as f:
                    json.dump([], f, indent=4)
                    f.close()
                with open("users.json") as f:
                    all_users: list = json.load(f)
                    f.close()
                all_users.append(user)
                with open("users.json", "w") as f:
                    json.dump(all_users, f, indent=4)
                    f.close()
                print('registered successfully :)')
        else:
            print("password or username registered")

    def isavailable(self):
        all_data = get_data()
        k = 0
        for user in all_data:
            if user['username'] == self.username and user['password'] == self.password:
                return True
            else:
                k += 1
        if k == len(all_data):
            return False
