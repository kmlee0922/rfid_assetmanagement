import socket

rule = {
    "30":'0', '31':'1','32':'2','33':'3','34':'4','35':'5','36':'6','37':'7','38':'8','39':'9',
    '41':'A','42':'B','43':'C','44':'D','45':'E','46':'F','47':'G','48':'H','49':'I','4A':'J','4B':'K','4C':'L','4D':'M','4E':'N','4F':'O',
    '50':'P','51':'Q','52':'R','53':'S','54':'T','55':'U','56':'V','57':'W','58':'X','59':'Y','5A':'Z'
}


def deleted(data):
    del_data = data[7:len(data)-1]
    
    return del_data

def decoding(data):
    
    data=deleted(data)

    decoding = ["",""]
    temp=""
    for i, value in enumerate(data):
        if i<8:
            if i%2==0:
                temp+=value
            else:
                temp+=value
                decoding[0]+=rule[str(temp)]
                temp=""
        elif value.isdigit():
            decoding[0]+=value
        else:
            decoding[1]=value
    return decoding


# 접속할 서버 주소입니다. 여기'에서는 루프백(loopback) 인터페이스 주소 즉 localhost를 사용합니다. 
HOST = '127.0.0.1'

# 클라이언트 접속을 대기하는 포트 번호입니다.   

PORT = 5001      

print('11')


# 소켓 객체를 생성합니다. 
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중이라 연결할 수 없다는 
# WinError 10048 에러 해결를 위해 필요합니다. 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
# HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
# 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다. 
# PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.  
server_socket.bind((HOST, PORT))

# 서버가 클라이언트의 접속을 허용하도록 합니다. 
server_socket.listen()

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다. 
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소입니다.
print('Connected by', addr)


# 무한루프를 돌면서 
while True:

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다. 
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 루프를 중지합니다. 
    if not data:
        break

    # 수신받은 문자열을 출력합니다.
    print('Received from', addr, data.decode())
    print(decoding(data.decode()))

    # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코) 
    client_socket.sendall(data)


# 소켓을 닫습니다.
client_socket.close()
server_socket.close()