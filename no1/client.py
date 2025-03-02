import socket

ip = "localhost"
port = 9806

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

while True:
    print("== CLIENT - INPUT DATA ==")
    nama = input("> Nama (atau ketik 'quit' untuk keluar): ")
    if nama.lower() == "quit":
        client.send("quit".encode("utf-8"))
        print("👋 Keluar dari program.")
        break

    nim = input("> NIM: ")
    tahun_lahir = input("> Tahun Lahir: ")

    # Format dengan pemisah koma agar server bisa membacanya dengan benar
    data = f"Nama: {nama}, NIM: {nim}, Tahun Lahir: {tahun_lahir}"
    print(f"📤 Mengirim data: {data}")

    client.send(data.encode("utf-8")) 

    response = client.recv(1024).decode("utf-8")
    print("📥 Server:", response)

client.close()
