import socket 

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = 'GET / HTTP/1.0\r\nHost: '+ HOST +'\r\n\r\n'

def main():

	addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
	address = addr_info[0]
	connect_socket(address)

def connect_socket(address):
	(family, socketype, proto, cannoname, socket_address) = address
	try:
		s = socket.socket(family, socketype, proto)
		s.connect(socket_address)
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

main()
