from socket import *
from utils import get_message, send_responce, bytes_to_dict, dict_to_bytes
from select import *

def new_listen_socket(address):
    sock = socket()
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)
    return sock

# def read_messages(client):
#     client_msg = get_message(client)
#     print(client_msg)

def mainloop():
    address = ('', 9090)
    clients = []
    server = new_listen_socket(address)

    while True:


        try:
            client, addr = server.accept()

            msg = get_message(client)

            responce_200 = {
                'responce': 200,
                'alert': 'Соединение с сервером установлено успешно. Привет, {}!'.format(msg['user'])
            }

            print(msg)
            send_responce(client, responce_200)
        except OSError as e:
            pass
        else:
            print('Получен запрос на соединение от {}'.format(addr))
            clients.append(client)
        finally:
            r = []
            w = []
            try:
                r, w, e = select(clients, clients, [], 0)
            except Exception as e:
                pass
            for some_client in r:
                try:
                    # resp = []
                    client_msg = get_message(some_client)
                    # resp.append(client_msg)
                    # message = resp[0]
                    print(client_msg)
                    for some_client in w:
                        send_responce(some_client, client_msg)

                except:
                    print('Клиент {} отключился'.format(client.getpeername()))
                    clients.remove(some_client)

print('----------------------------СЕРВЕР ЗАПУЩЕН------------------------------')
mainloop()

