import socket

ip = "localhost"
port = 9806

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print("== SERVER SOCKET ==")
print(f"🚀 Server berjalan di {ip}:{port}")
conn, address = server.accept()
print(f"🔗 Koneksi diterima dari {address}")

while True:
    data = conn.recv(1024).decode("utf-8")
    if not data:
        break

    if data.lower() == "quit":
        print("🚪 Client mengakhiri koneksi.")
        break

    print("📥 Data diterima dari client:\n", data)

    # Ekstrak nama dari data
    try:
        pisah_data = data.split(",") 
        nama = pisah_data[0].split(":")[1].strip() 
        response = f"Halo {nama}, data Anda telah diterima!"
    except:
        response = "⚠️ Format data salah!"

    conn.send(response.encode("utf-8"))

conn.close()
server.close()
print("🛑 Server telah ditutup.")
