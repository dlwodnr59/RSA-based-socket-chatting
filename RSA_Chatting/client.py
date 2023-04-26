from socket import *
import threading
import time
import Client_RSA_key

ip = 'server ip'
port = 'server port'
Client_RSA_key.Generation_key()


connectionSock = socket(AF_INET, SOCK_STREAM)
connectionSock.connect((ip, port))
print('Connect!')
print('Start Chatting!')


def send(sock):
    while True:
        sendData = input()
        sock.send(Client_RSA_key.encrypt_text(sendData))

def receive(sock):
    while True:
        recvData = sock.recv(9096)
        print('user :', Client_RSA_key.decrypt_text(recvData))


# 클라이언트의 공개키를 서버로 전송
with open('Client_Public_Key.pem', 'rb') as f:
    pubkey_data = f.read()
    connectionSock.sendall(pubkey_data)


# 서버의 공개키를 받음
with open('Server_Public_Key.pem', 'wb') as f:
    key_data = connectionSock.recv(9096)
    f.write(key_data)


sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
