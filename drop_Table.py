from db import DB
from People_model import UserModel

#db = DB('users.db')
users_model = UserModel(db.get_connection())
users_model.clear_db()
print(users_model.get_all())
