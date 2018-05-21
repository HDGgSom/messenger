from socket import *
# import json
from utils import get_message, send_responce, bytes_to_dict, dict_to_bytes

if __name__ == '__main__':

    server = socket()
    server.bind(('', 9090))
    server.listen(5)
    print('\n----------СЕРВЕР ЗАПУЩЕН--------\n')

    while True:
        client, addr = server.accept()
        print('Получен запрос на соединение от {}\n'.format(addr))
        js_message = get_message(client)

        responce_200 = {
            'responce': 200,
            'alert': 'Соединение с сервером установлено успешно. Привет, {}!'.format(js_message['username'])
        }

        responce_400 = {
            'responce': 400,
            'alert': 'ОШИБКА: неизвестное действие со стороны клиента'
        }

        if js_message['action'] == 'presence':
            send_responce(client, responce_200)
        else:
            send_responce(client, responce_400)
