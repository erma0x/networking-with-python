import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '192.168.10.97'
server_port = 9101

client_socket.connect((server_address, server_port))

message = 'Hello World'
response = "Hello World"


while True:
	client_socket.send(message.encode())
	time.sleep(4)
	print("Test passed" if message == response else "Test failed")
