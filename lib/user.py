class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, new_user):
        return self.__dict__ == new_user.__dict__

    def __repr__(self):
        return f"User(id: {self.id}, username: {self.username}, password: {self.password})"