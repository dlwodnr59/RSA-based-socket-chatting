# RSA-based-socket-chat-program
RSA기반으로 암호화 복호화 되는 채팅 프로그램 입니다

이 프로그램은 서버(server.py, Server_RSA_key.py)와 클라이언트(client.py, Client_RSA_key.py)로 구성됩니다. 
서버에서 응답을 기다리며, 클라이언트가 연결하면 서버와 클라이언트 간에 공개키를 교환하고 RSA 암호화를 사용하여 통신합니다. 
이는 일반적인 소켓 통신과는 다른 방식으로 패킷을 암호화하므로 보안성이 높아집니다.
