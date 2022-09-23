#!/usr/bin/env python3
import socket
from multiprocessing import Pool

#define address & buffer size
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

#create a tcp socket
def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s

def connect(addr):
    try:
        s = create_tcp_socket()
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as error:
        print(error)
    finally:
        s.close()

def main():
    address = [(HOST, PORT)]
    with Pool() as p:
        p.map(connect, address * 10)

if __name__ == "__main__":
    main()