import socket

HOST = '127.0.0.1'                   # Symbolic name meaning all available interfaces
PORT = 9999              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by'), addr
i=0;


while 1:
    data = conn.recv(1024).decode('utf-8')
    #i=i+1
    conn.send(data.encode('utf-8'))
    print(i)
    print("번째 데이터 송수신")
    if not data: break

conn.sendall(data)
conn.close()