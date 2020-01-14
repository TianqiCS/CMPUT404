import socket
HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1) 
        conn, addr = s.accept() 
        with conn:
            print('Connected by: ', addr)
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                print(data)
                conn.sendall(data)


if __name__ == "__main__":
    main()
