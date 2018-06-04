from socket import *
import json
from utils import JIM

if __name__ == '__main__':

    client = socket()
    client.connect(('localhost', 9090))
    client.settimeout(5)
    print('--------СОЕДИНЕНИЕ С СЕРВЕРОМ УСТАНОВЛЕНО--------')
    msg = {

    'user': 'Slark',
    'action': 'presence'

    }

    JIM.send_message(msg, client)
    responce = JIM.get_message(client)
    print(responce)
    while True:
        msg = input('Введите ваше сообщение: ')
        if msg == 'quit':
            break
        message = {
            'user': 'Slark',
            'message': msg
        }
        JIM.send_message(message, client)

    client.close()