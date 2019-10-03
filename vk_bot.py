import bs4, vk_api
import json
import random
import requests
from People_model import UserModel
from db import DB
#from keyboard import keyboard_dict_main, keyboard_dict_first_dialog_1, keyboard_dict_first_dialog_not, \
 #   keyboard_dict_first_dialog_ok, keyboard_dict_thanks, keyboard_dict_ok
from keyboard import *

# Авторизуемся как сообщество
with open('Token.txt', 'r') as file:
    token = file.read()

vk = vk_api.VkApi(token=token)

db = DB('users.db')


class VkBot:

    def __init__(self, user_id):
        print("\n!!!Создан объект бота!!!")
        self.USER_ID = user_id
        self.USERNAME = self.get_user_name_from_vk_id(user_id)
        self.pm = UserModel(db.get_connection())
        self.is_user_in()
        self.register_steps = self.pm.get_step(self.USER_ID)


    def is_user_in(self):
        if not self.pm.exists(self.USER_ID):
            self.pm.insert(self.USER_ID, self.USERNAME, 'None', 0)
        else:
            pass

    def get_user_name_from_vk_id(self, user_id):
        if user_id == 0:
            user_id = self.USER_ID
        params = {'user_id': user_id,
                  'v': '5.52',
                  'access_token': token,
                  'fields': 'first_name,last_name'}
        request = requests.get('https://api.vk.com/method/users.get?', params=params)
        request = request.json()['response'][0]
        return request['first_name'] + request['last_name']

    def get_user_photo_from_vk_id(self, user_id):
        if user_id == 0:
            user_id = self.USER_ID
        params = {'user_id': user_id,
                  'v': '5.52',
                  'access_token': token,
                  'fields': 'photo_id'}
        request = requests.get('https://api.vk.com/method/users.get?', params=params)
        return 'photo' + request.json()['response'][0]['photo_id']

    def answer(self, number):
        if number == 1:
            self.pm.add_ratio(self.user_to_choose_1[1])
        elif number == 2:
            self.pm.add_ratio(self.user_to_choose_2[1])
        return self.show_new_people()

    def get_users(self):
        res = []
        j = 1

        for i in self.pm.get_all():
            print(i)
            prom = []
            prom.append(str(j))
            prom.append(f'https://vk.com/id{i[1]}')
            prom.append(i[2])
            if i[5] == '5':
                prom.append('Solo')
            elif i[5] == '4':
                prom.append('Team')
            else:
                prom.append('Not participating')
            #prom.append('Solo' if i[5]=='5' else 'Team')
            j += 1
            res.append(prom)


        message = '\n'.join([' '.join(i) for i in res])
        return message

    def greetings(self, message):
        answer_main = {
            'user_id': self.USER_ID,
            'message': 'Привет!\nХочешь поучаствовать в нашем турнире по CS:GO?',
            'random_id': random.randint(1, 1000000)
            }

        if message == 'get_users':
            answer = answer_main.copy()
            answer['message'] = self.get_users()
            return answer


        if self.register_steps == 0:
            self.pm.set_step(self.USER_ID, '1')
            self.register_steps = 1
            answer_main['keyboard'] = json.dumps(keyboard_dict_first_dialog_1, ensure_ascii=False)
            return answer_main

        elif self.register_steps == 1:

            if message == 'Да!':
                answer = answer_main.copy()
                answer['message'] = 'Отлично! Тебя добавили в список участников.\nКогда начнется распределение по командам, тебе напишут.\nЕсли у тебя уже есть команда(team player), отправь 1, если нет(solo player), то 2.'
                answer['keyboard'] = json.dumps(keyboard_dict_first_dialog_ok, ensure_ascii=False)
                self.register_steps = 3
                self.pm.set_step(self.USER_ID, 3)
                return answer

            elif message == 'Нет(':
                self.register_steps = 2
                self.pm.set_step(self.USER_ID,2)
                answer = answer_main.copy()
                answer['message'] = 'Ты вот сейчас серьёзно?'
                answer['keyboard'] = json.dumps(keyboard_dict_first_dialog_not, ensure_ascii=False)
                return answer

            else:
                answer = answer_main.copy()
                answer['message'] = 'Используй кнопки!!'
                answer['keyboard'] = json.dumps(keyboard_dict_first_dialog_1, ensure_ascii=False)
                return answer

        elif self.register_steps == 2:

            if message == 'Ладно, уговорили!' or message == '&quot;Ладно,уговорили&quot; только другого цвета':
                answer = answer_main.copy()
                answer['message'] = 'Отлично! Тебя добавили в список участников.\nКогда начнется распределение по командам, тебе напишут.\nЕсли у тебя уже есть команда(team player), отправь 1, если нет(solo player), то 2.'
                answer['keyboard'] = json.dumps(keyboard_dict_first_dialog_ok, ensure_ascii=False)
                self.register_steps = 3
                self.pm.set_step(self.USER_ID, 3)
                return answer

            else:
                answer = answer_main.copy()
                answer['message'] = 'Используй кнопки!!!'
                answer['keyboard'] = json.dumps(keyboard_dict_first_dialog_not, ensure_ascii=False)
                return answer

        elif self.register_steps == 3:

            if message == '1':
                #if user has a team
                answer = answer_main.copy()
                answer['message'] = 'С тобой свяжутся когда начнется распределение и вы будете играть командой'
                answer['keyboard'] = json.dumps(keyboard_dict_thanks, ensure_ascii=False)
                self.register_steps = 4
                self.pm.set_step(self.USER_ID, 4)
                return answer
                

            elif message == '2':
                #and if he doesn't
                answer = answer_main.copy()
                answer['message'] = 'Когда начнется распределение по командам, тебе напишут.\nБудешь играть командой, составленной из участников турнира.\nУдачи!!'
                answer['keyboard'] = json.dumps(keyboard_dict_thanks, ensure_ascii=False)
                self.register_steps = 5
                self.pm.set_step(self.USER_ID, 5)
                return answer
            
            elif message == 'Спасибо!' or message == 'Спасибо!':
                answer = answer_main.copy()
                answer['message'] = '))'
                answer['keyboard'] = json.dumps(keyboard_dict_thanks, ensure_ascii=False)
                return answer

            else:
                answer = answer_main.copy()
                answer['message'] = 'Используй кнопки!'
                answer['keyboard'] = json.dumps(keyboard_dict_ok, ensure_ascii=False)
                return answer


        elif self.register_steps == 4:
            if message =='Изменить статус участника':
                answer = answer_main.copy()
                self.pm.set_step(self.USER_ID, 5)
                answer['message'] = 'Статус участника был успешно сменен с team на solo'
                answer['keyboard'] = json.dumps(keyboard_dict_last_solo, ensure_ascii=False)
                return answer

            elif message == 'Отменить регистрацию в турнире':
                answer = answer_main.copy()
                self.pm.set_step(self.USER_ID, 6)
                answer['message'] = 'Ты уверен, что хочешь покинуть турнир?'
                answer['keyboard'] = json.dumps(keyboard_dict_ausure, ensure_ascii=False)
                return answer

            elif message == 'Спасибо!' or message == 'Спасибо!':
                answer = answer_main.copy()
                answer['message'] = '))'
                answer['keyboard'] = json.dumps(keyboard_dict_last_team, ensure_ascii=False)
                return answer

            else:
                answer = answer_main.copy()
                answer['message'] = 'Используй кнопки!'
                answer['keyboard'] = json.dumps(keyboard_dict_last_team, ensure_ascii=False)
                return answer



        elif self.register_steps == 5:
            if message =='Изменить статус участника':
                answer = answer_main.copy()
                self.pm.set_step(self.USER_ID, 4)
                answer['message'] = 'Статус участника был успешно сменен с solo на team'
                answer['keyboard'] = json.dumps(keyboard_dict_last_team, ensure_ascii=False)
                return answer

            elif message == 'Отменить регистрацию в турнире':
                answer = answer_main.copy()
                self.pm.set_step(self.USER_ID, 6)
                answer['message'] = 'Ты уверен, что хочешь покинуть турнир?'
                answer['keyboard'] = json.dumps(keyboard_dict_ausure, ensure_ascii=False)
                return answer
            
            elif message == 'Беседа для solo игроков':
                answer = answer_main.copy()
                self.pm.set_step(self.USER_ID, 6)
                answer['message'] = 'Вступай в беседу, чтобы найти команду:\n https://vk.me/join/AJQ1dzHhIRXGUMUNyHXAMK2J'
                answer['keyboard'] = json.dumps(keyboard_dict_last_solo, ensure_ascii=False)
                return answer

            elif message == 'Спасибо!' or message == 'Спасибо!':
                answer = answer_main.copy()
                answer['message'] = '))'
                answer['keyboard'] = json.dumps(keyboard_dict_last_solo, ensure_ascii=False)
                return answer


            else:
                answer = answer_main.copy()
                answer['message'] = 'Используй кнопки!'
                answer['keyboard'] = json.dumps(keyboard_dict_last_solo, ensure_ascii=False)
                return answer

        elif self.register_steps == 6:
            if message == 'Да':
                answer = answer_main.copy()
                self.pm.delete_user(self.USER_ID)
                answer['message'] = 'Ну что ж, прощай.'
                #answer['keyboard'] = json.dumps({}, ensure_ascii=False)
                return answer

            elif message == 'Нет':
                answer = answer_main.copy()
                self.pm.set_step(self.USER_ID,3)
                answer['message'] = 'Отлично! Ты еще в деле! \n Участвуешь в команде(1) или в составе команды, составленной из других участников турнира(2)?'
                answer['keyboard'] = json.dumps(keyboard_dict_first_dialog_ok, ensure_ascii=False)
                return answer

            else:
                answer = answer_main.copy()
                answer['message'] = 'Используй кнопки!'
                answer['keyboard'] = json.dumps(keyboard_dict_ausure, ensure_ascii=False)
                return answer



   
    def new_message(self, message):
        return self.greetings(message)

