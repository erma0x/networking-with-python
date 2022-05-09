import socket

def get_response(my_socket):
    while len(risposta) > 0: 
        risposta = my_socket.recv(2048)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    s.send(b'Systematik')
