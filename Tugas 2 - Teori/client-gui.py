import socket
import tkinter as tk
from tkinter import messagebox

def send_message():
    message = entry.get()
    if not message:
        messagebox.showwarning("Warning", "Pesan tidak boleh kosong!")
        return
    
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    data, _ = client_socket.recvfrom(1024)
    response_label.config(text=f"Response: {data.decode()}")

# Konfigurasi socket UDP
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# GUI menggunakan Tkinter
root = tk.Tk()
root.title("UDP Client")
root.geometry("400x200")

tk.Label(root, text="Masukkan Pesan:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Kirim", command=send_message).pack(pady=5)

response_label = tk.Label(root, text="Response:")
response_label.pack(pady=5)

root.mainloop()

# Jangan lupa untuk menjalankan server UDP agar client dapat berkomunikasi
