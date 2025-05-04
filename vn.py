import subprocess
import time
import os

# Definir colores para la terminal
BLUE = "\033[34m"
WHITE = "\033[37m"
RESET = "\033[0m"

# Función para mostrar los logs
def show_logs():
    # Lee los logs desde un archivo (logs.txt)
    try:
        with open("logs.txt", "r") as file:
            logs = file.readlines()
            for log in logs:
                print(f"{WHITE}{log.strip()}{RESET}")
    except FileNotFoundError:
        print(f"{WHITE}Log file not found.{RESET}")

# Función para iniciar el c2.py
def start_c2():
    print(f"{BLUE}Starting Osais C2...{RESET}")
    subprocess.Popen(["python3", "c2.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Función principal que ejecuta la carga de logs y el C2
def main():
    # Asegurarse de que estamos en el directorio correcto (osais)
    os.chdir("osais")
    
    print(f"{BLUE}Loading logs and starting C2...{RESET}")
    show_logs()  # Muestra los logs al principio
    
    time.sleep(2)  # Espera para simular un retraso
    
    start_c2()  # Inicia el C2 en segundo plano

    print(f"{WHITE}Osais C2 started. You can now login from the terminal...{RESET}")
    print(f"{BLUE}Type 'python3 c2.py' in another terminal to access the C2 interface.{RESET}")

# Ejecutar el main cuando se ejecute vn.py
if __name__ == "__main__":
    main()
