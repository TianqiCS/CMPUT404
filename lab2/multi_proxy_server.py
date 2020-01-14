import socket
from multiprocessing import Process

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024

def main():
    host = 'www.google.com'
    port = 80 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen()

        while True:
            conn, addr = proxy_start.accept()
            print('Connected by: ', addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                try:
                    remote_IP = socket.gethostbyname(host)
                    proxy_end.connect((remote_IP, port))
                    p = Process(target=handle_request, args=(conn, addr, proxy_end))
                    p.daemon = True
                    p.start()
                    print("Started process: ", p)
                except socket.gaierror:
                    print('Host not found.')
            conn.close()

def handle_request(conn, address, proxy_end):
    send_full_data = conn.recv(BUFFER_SIZE)
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)

    data = proxy_end.recv(BUFFER_SIZE)
    conn.send(data)
if __name__ == "__main__":
    main()
