import socket
import threading

# Konfigurasi Server
HOST = "localhost"
PORT = 9806

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message, sender_socket=None):
    """Mengirim pesan ke semua client kecuali pengirimnya"""
    for client in clients:
        if client != sender_socket:
            client.send(message)

def handle_client(client):
    """Menangani pesan dari setiap client"""
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            
            if message.lower() == "quit":
                index = clients.index(client)
                nickname = nicknames[index]
                
                # Menghapus client dari daftar
                clients.remove(client)
                nicknames.pop(index)
                
                print(f"❌ \033[92m{nickname}\033[0m keluar dari chat.")
                broadcast(f"🔴 \033[92m{nickname}\033[0m telah keluar dari chat.\n".encode("utf-8"))
                
                client.send("QUIT".encode("utf-8"))  # Kirim sinyal ke client untuk keluar
                client.close()
                break
            
            broadcast(message.encode("utf-8"), client)
        except:
            break

def receive():
    """Menerima koneksi baru dari client"""
    while True:
        client, address = server.accept()
        print(f"🔗 Koneksi baru dari {address}")

        client.send("NICK".encode("utf-8"))  # Meminta nickname dari client
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"🟢 \033[92m{nickname}\033[0m telah bergabung!")
        broadcast(f"🟢 \033[92m{nickname}\033[0m telah bergabung!\n".encode("utf-8"))

        client.send("✅ Anda terhubung ke chat server!".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print(f"🚀 Server berjalan di {HOST}:{PORT}")
receive()
