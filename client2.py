from socket import *
import json
from utils import send_message, get_message

if __name__ == '__main__':

    client = socket()
    client.connect(('localhost', 9090))
    print('--------СОЕДИНЕНИЕ С СЕРВЕРОМ УСТАНОВЛЕНО--------')

    while True:
        msg = input('Введите ваше сообщение: ')
        if msg == 'quit':
            break
        message = {
            'user': 'slark',
            'message': msg
        }
        send_message(message, client)
        # serv_message = get_message(client)
        # print('Ответ от сервера: ', serv_message)

    client.close()