from .user import User

class UserRepository:
    def __init__(self, conn, bcrypt):
        self._connection = conn
        self.bcrypt = bcrypt

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

        hashed_password = self.bcrypt.generate_password_hash(password).decode("utf-8")

        # print(username)
        # print(password)

        self._connection.execute("INSERT INTO users (username, password) VALUES (%s, %s)", [username, hashed_password])

    def find(self, username):
        return self._connection.execute("SELECT * FROM users WHERE username = %s", [username])

    def does_user_exist(self, username):
        return True if self.find(username) else False

    def check_password(self, username, password):
        user = self.find(username)

        database_password = user[0].get("password")

        print()

        if self.bcrypt.check_password_hash(database_password, password) == True:
            return True
        else:
            return False