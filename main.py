from vk_bot import VkBot
import vk_api, random, json
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', answer)

with open('Token.txt', 'r') as file:
	token = file.read()

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')
            bot = VkBot(event.user_id)
            answer = bot.new_message(event.text)
            write_msg(event.user_id, answer)
            print('Text: ', event.text)
