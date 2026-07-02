from .user import User

class UserRepository:
    def __init__(self, conn):
        self._connection = conn

    def all(self):
        users = self._connection.execute("SELECT * FROM users")

        list_of_users = []

        for user in users:
            list_of_users.append(User
                                (
                                    user.get("id"), 
                                    user.get("username"), 
                                    user.get("password")
                                    )
                                )

        return list_of_users

    def create_user(self, new_user):
        username = new_user.get("username")
        password = new_user.get("password")

        # print(username)
        # print(password)

        self._connection.execute("INSERT INTO users (username, password) VALUES (%s, %s)", [username, password])

    def find(self, username):
        return self._connection.execute("SELECT * FROM users WHERE username = %s", [username])

    def does_user_exist(self, username):
        return True if self.find(username) else False

    def check_password(self, username, password):
        user = self.find(username)

        database_password = user[0].get("password")

        if database_password == password:
            return True
        else:
            return False