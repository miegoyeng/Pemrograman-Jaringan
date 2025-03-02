import socket
from datetime import datetime

# Fungsi operasi hitung umur
def hitung_umur(tahun_lahir):
    return datetime.now().year - tahun_lahir

ip = "localhost"
port = 9806

# mengatur server dengan socket IPv4 dan protokol TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))
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
    
    print("\n📥 Data diterima dari client:\n", data)
          
     # Ekstrak nama dari data
    try:
        pisah_data = data.split(",")  
        nama = pisah_data[0].split(":")[1].strip()  

        # Operasi hitung umur
        tahun_lahir = int(pisah_data[1].split(":")[1].strip())
        umur = hitung_umur(tahun_lahir)

        response = f"Halo {nama}, kamu lahir pada tahun {tahun_lahir} dan sekarang berumur {umur} tahun."
    except:
        response = "⚠️ Format data salah!"

    conn.send(response.encode("utf-8"))

conn.close()
server.close()
print("🛑 Server telah ditutup.")   