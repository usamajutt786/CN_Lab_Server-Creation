import socket
host='127.0.0.1'
port=5001
obj=socket.socket()
obj.connect((host,port))
message=input("Please enter the message: ")
while message !="Bye":
    obj.send(message.encode())
    data=obj.recv(1024).decode()
    print("Receive from server ",data)
    message=input("Type message")
    obj.send(message.encode())
    obj.close()