import socket 

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = 'GET / HTTP/1.0\r\nHost: '+ HOST +'\r\n\r\n'

def main():
    address = (HOST, PORT)
    connect(address)

def connect(address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        print("Connected")
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

if __name__ == "__main__":
    main()
