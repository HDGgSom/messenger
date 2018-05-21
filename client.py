from socket import *
# import json
from utils import send_message, get_message

if __name__ == '__main__':

    client = socket()
    client.connect(('localhost', 9090))
    print('--------СОЕДИНЕНИЕ С СЕРВЕРОМ УСТАНОВЛЕНО--------')

    message = {
        'username': 'gSom',
        'action': 'presence'
    }

    send_message(message, client)
    js_data = get_message(client)
    print('От сервера получено сообщение с кодом: {} \nТекст сообщения: {}'.format(js_data['responce'], js_data['alert']))