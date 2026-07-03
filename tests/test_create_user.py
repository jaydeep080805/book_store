from lib.user_repository import UserRepository
from lib.user import User

# importing the db func makes sure it is seeded
def test_create_user(db, bcrypt):
    user_repo = UserRepository(db, bcrypt)

    test_data = {"username": "test_user", "password": "test_password"}
    user_repo.create_user(test_data)

    all_users = user_repo.all()

    # print(f">>> ALL USERS: {all_users[0]}")

    # new_user = User(1, "test_user", "test_password")
    # print(f">>> NEW USER: {new_user}")

    # print(type(new_user))
    # print(type(all_users[0]))

    # print(new_user == all_users[0])

    assert len(all_users) == 1

    # for this to pass you need __eq__ in the class
    # otherwise it'll never compare the contents and will always return false
    # ^ this no longer matters since its broken with bcrypt (:
    assert all_users[-1].username == "test_user"
    assert bcrypt.check_password_hash(all_users[-1].password, "test_password")