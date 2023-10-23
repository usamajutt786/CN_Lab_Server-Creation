import socket
host='127.0.0.1'
port=5001
server=socket.socket()
server.bind((host,port))
server.listen()
conn, addr = server.accept()
print("Connect from: ",str(addr))
while True:
    data=conn.recv(1024).decode()
    if str(data)=="Bye":
        print("Receeive from client: ",str(data))
        print("connection termination ")
        conn.close()
        break
    print("Receive from client :",str(data))
    data=input("Type message :")
    conn.send((data.encode())) 