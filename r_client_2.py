from socket import *
import json
from utils import send_message, get_message

if __name__ == '__main__':

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