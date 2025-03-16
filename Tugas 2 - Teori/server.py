import socket

# Konfigurasi socket UDP
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server UDP berjalan di {SERVER_IP}:{SERVER_PORT}")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Pesan diterima dari {addr}: {data.decode()}")
    response = data.decode().upper()
    server_socket.sendto(response.encode(), addr)
