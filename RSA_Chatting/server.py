import Server_RSA_key
from socket import *
import threading
import time


port = 'server port'
ip = 'server ip'
Server_RSA_key.Generation_key()


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((ip, port))
serverSock.listen(1)

def send(sock):
    while True:
        sendData = input()
        sock.send(Server_RSA_key.encrypt_text(sendData))

def receive(sock):
    while True:
        recvData = sock.recv(9096)
        print('user :', Server_RSA_key.decrypt_text(recvData))


print('Waiting...')
connectionSock, addr = serverSock.accept()
print('Connect!')


# 서버의 공개키를 클라이언트로 전송
with open('Server_Public_Key.pem', 'rb') as f:
    filedata = f.read()
    connectionSock.sendall(filedata)

# 클라이언트의 공개키를 받음
with open('Client_Public_Key.pem', 'wb') as f:
    data = connectionSock.recv(1024)
    f.write(data)  # 받은 데이터를 파일에 쓰기


sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))


sender.start()
receiver.start()

while True:
    time.sleep(1)
