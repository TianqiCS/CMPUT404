import socket

HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 4096

payload = 'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("Connected")
        full_data = b''   
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        while True:			    
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data   
        print(full_data)
    except:
        print("failed to connect")

if __name__ == "__main__":
    main()

