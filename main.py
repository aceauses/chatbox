import sys
import socket
import time

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080


new_socket.bind((host_name, port))
print("Binding succesfully")
print("Your hostname is : ", s_ip)

name = input("Name: ")
new_socket.listen(1)

con, add = new_socket.accept()
print("Receive connection from : ", add[0])
print('Connection established. Connection from: ', add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())

while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
