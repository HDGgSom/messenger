from socket import *
import json
from utils import JIM

if __name__ == '__main__':

    client = socket()
    client.connect(('localhost', 9090))
    print('--------СОЕДИНЕНИЕ С СЕРВЕРОМ УСТАНОВЛЕНО--------')
    msg = {

    'user': 'gSom',
    'action': 'presence'

    }
    JIM.send_message(msg, client)
    responce = JIM.get_message(client)
    print(responce)

    while True:

        serv_message = JIM.get_message(client)
        print('{} написал: {}'.format(serv_message['user'], serv_message['message']))


    client.close()





