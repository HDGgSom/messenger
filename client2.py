import threading
import time
from socket import *
import json
from utils import send_message, get_message

def update_chat():
    last_update = time.time()
    while True:
        if time.time() - last_update > 1:
            serv_message = get_message(client)
            if serv_message:
                print('{} написал: {}'.format(serv_message['user'], serv_message['message']))


if __name__ == '__main__':

    chat_update_thread = threading.Thread(target=update_chat, ).start()
    client = socket()
    client.connect(('localhost', 9090))
    client.settimeout(5)
    print('--------СОЕДИНЕНИЕ С СЕРВЕРОМ УСТАНОВЛЕНО--------')

    msg = {

        'user': 'Slark',
        'action': 'presence'

    }
    send_message(msg, client)
    responce = get_message(client)
    print(responce)

    while True:

        msg = input('Введите ваше сообщение: ')
        if msg == 'quit':
            break
        message = {

            'user': 'Slark',
            'message': msg
            }

        send_message(message, client)

    client.close()
