import socket
import threading

# Konfigurasi Client
HOST = "localhost"
PORT = 9806

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nickname = input("Masukkan nama Anda: ")
client.send(nickname.encode("utf-8"))

def receive_messages():
    """Menerima pesan dari server"""
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            
            if message == "QUIT":
                print("👋 Anda telah keluar dari chat.")
                client.close()
                break
            
            print(message)
        except:
            print("⚠️ Koneksi terputus dari server!")
            client.close()
            break

def send_messages():
    """Mengirim pesan ke server"""
    while True:
        message = input("")
        if message.lower() == "quit":
            client.send("quit".encode("utf-8"))
            break
        formatted_message = f"\033[92m{nickname}\033[0m: {message}"
        client.send(formatted_message.encode("utf-8"))

# Thread untuk menerima dan mengirim pesan
thread_receive = threading.Thread(target=receive_messages)
thread_receive.start()

thread_send = threading.Thread(target=send_messages)
thread_send.start()
