from socket import *
import json
from utils import send_message, get_message

if __name__ == '__main__':

    client = socket()
    client.connect(('localhost', 9090))
    print('--------СОЕДИНЕНИЕ С СЕРВЕРОМ УСТАНОВЛЕНО--------')
    msg = {

    'user': 'gSom',
    'action': 'presence'

    }
    send_message(msg, client)
    responce = get_message(client)
    print(responce)

    while True:

        serv_message = get_message(client)
        print('{} написал: {}'.format(serv_message['user'], serv_message['message']))


    client.close()





