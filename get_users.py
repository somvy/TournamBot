from db import DB
from People_model import UserModel
import bs4, vk_api, random

USER_ID = '245280068'


def write_msg(user_id, message):
    vk.method('messages.send', message)


db = DB('users.db')
users_model = UserModel(db.get_connection())

with open('Token.txt', 'r') as file:
	token = file.read()

vk = vk_api.VkApi(token=token)
#longpoll = VkLongPoll(vk)


users_model.init_table()
res = []
j = 1

for i in users_model.get_all():
	prom = []
	prom.append(str(j))
	prom.append(f'https://vk.com/id{i[1]}')
	prom.append(i[2])
	prom.append('Solo' if i[5]=='5' else 'Team')
	j += 1
	res.append(prom)

message = '\n'.join([' '.join(i) for i in res])
print(message)

ANSWER_MAIN = {
            'user_id': USER_ID,
            'message': message,
            'random_id': random.randint(1, 1000000)
            }
write_msg('dont matter', ANSWER_MAIN)
