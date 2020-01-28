import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import threading
import requests
import os


class Bot:
    def __init__(self):
        token = os.environ.get('token')
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk, 187766801)
        self.vk_api = self.vk.get_api()

    def main(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.obj.text.lower() == '/создать':
                    if self.check_room(event.obj.from_id) == 0:
                        text = self.create_room(event.obj.from_id)
                        self.send_msg(event.obj.from_id, 'Ваша номер чата: ' + str(text))
                    else:
                        self.send_msg(event.obj.from_id, 'Вы уже находитесь в чате')
                elif '/подключиться' in event.obj.text.lower():
                    try:
                        if self.check_room(event.obj.from_id) == 0 and self.check_value(event.obj.text.split()[1]) < 2:
                            text = event.obj.text.split()[1]
                            self.join_in_room(event.obj.from_id, int(text))
                        else:
                            self.send_msg(event.obj.from_id, 'Вы уже находитесь в чате либо чат занят')
                    except:
                        self.send_msg(event.obj.from_id, 'Неправильный ввод')
                elif event.obj.text.lower() == '/выйти':
                    try:
                        if self.check_room(event.obj.from_id) != 0:
                            self.send_msg(event.obj.from_id, 'Вы покинули чат')
                            self.exit_from_room(event.obj.from_id)
                        else:
                            self.send_msg(event.obj.from_id, 'Вы не в чате!')
                    except:
                        self.send_msg(event.obj.from_id, 'Неправильный ввод')
                elif self.check_room(event.obj.from_id) != 0 and self.check_value_by_id(event.obj.from_id) == 2:
                    try:
                        self.write_message(event.obj.from_id, 'Сообщение: ' + event.obj.text.replace('/написать ', ''))
                        self.send_msg(event.obj.from_id, 'Отправлено!')
                    except:
                        self.send_msg(event.obj.from_id, 'Неправильный ввод')

    def log(self, msg):
        self.vk_api.messages.send(peer_id=159951767,
                                  message=msg,
                                  random_id=get_random_id())


    def send_msg(self, send_id, message):
        try:
            self.vk_api.messages.send(peer_id=send_id,
                                    message=message,
                                    random_id=get_random_id())
        except Exception as a:
            self.log("Error in function 'send_msg'\n\n" + str(a))


    def create_room(self, uid):
        try:
            response = requests.get('http://clrn1w.xyz/chat/create.php?id=' + str(uid))
            return response.json()
        except Exception as a:
            self.log("Error in function 'create_room'\n\n" + str(a))


    def check_room(self, uid):
        try:
            response = requests.get('http://clrn1w.xyz/chat/check.php?id=' + str(uid))
            return response.json()
        except Exception as a:
            self.log("Error in function 'check_room'\n\n" + str(a))


    def join_in_room(self, uid, room):
        try:
            self.send_msg(uid, 'Вы подключились к чату номер ' + str(room))
            requests.get('http://clrn1w.xyz/chat/join.php?user=' + str(uid) + '&rm=' + str(room))
            self.write_message(uid, 'Собеседник подключился в чат')
        except Exception as a:
            self.log("Error in function 'join_in_room'\n\n" + str(a))

        
    def write_message(self, uid, text):
        try:
            response = requests.get('http://clrn1w.xyz/chat/getid.php?id=' + str(uid))
            self.send_msg(response.json(), str(text))
        except Exception as a:
            self.log("Error in function 'write_message'\n\n" + str(a))


    def exit_from_room(self, uid):
        try:
            if self.check_value_by_id(uid) == 2:
                self.write_message(uid, 'Собеседник покинул чат')
                requests.get('http://clrn1w.xyz/chat/exit.php?id=' + str(uid))
            else:
                requests.get('http://clrn1w.xyz/chat/exit.php?id=' + str(uid))
        except Exception as a:
            self.log("Error in function 'exit_from_room'\n\n" + str(a))


    def check_value(self, room):
        try:
            response = requests.get('http://clrn1w.xyz/chat/value.php?id=' + str(room))
            return response.json()
        except Exception as a:
            self.log("Error in function 'check_value'\n\n" + str(a))


    def check_value_by_id(self, uid):
        try:
            response = requests.get('http://clrn1w.xyz/chat/valueid.php?id=' + str(uid))
            return response.json()
        except Exception as a:
            self.log("Error in function 'check_value_by_id'\n\n" + str(a))

t1 = threading.Thread(target=Bot().main)
t1.start()
t1.join()
