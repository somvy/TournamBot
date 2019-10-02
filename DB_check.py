from People_model import UserModel
from db import DB

db = DB('users.db')
pm = UserModel(db.get_connection())
print(pm.get_all())