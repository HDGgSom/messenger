import json


def send_responce(client, responce):
    js_responce = json.dumps(responce)
    client.send(js_responce.encode('utf-8'))

def dict_to_bytes(data):
    jmessage = json.dumps(data)
    bytemessage = jmessage.encode('utf-8')
    return bytemessage

def bytes_to_dict(data):
    decoded_message = data.decode('utf-8')
    js = json.loads(decoded_message)
    return js

def get_message(sock):
    message = sock.recv(1024)
    dec_msg = bytes_to_dict(message)
    return dec_msg

def send_message(message, client):
    bytemessage = dict_to_bytes(message)
    client.send(bytemessage)

#