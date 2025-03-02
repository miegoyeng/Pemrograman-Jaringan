import socket

ip = "localhost"
port = 9806

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

print("== CLIENT - HITUNG UMUR ==")
while True:
    nama = input("> Nama (atau ketik 'quit' untuk keluar): ")
    if nama.lower() == "quit":
        client.send("quit".encode("utf-8"))
        print("👋 Keluar dari program.")
        break
    
    tahun_lahir = input("> Tahun Lahir: ")
    
    data = f"Nama: {nama}, Tahun Lahir: {tahun_lahir}"
    print(f"📤 Mengirim data: {data}")
    client.send(data.encode("utf-8"))

    response = client.recv(1024).decode("utf-8")
    print("📥 Server:", response)

client.close()