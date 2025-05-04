import subprocess
import os
import time
import threading

# Definir colores para la terminal
BLUE = "\033[34m"
WHITE = "\033[37m"
RESET = "\033[0m"

# Leer los bots desde el archivo bots.txt
def load_bots():
    bots = {}
    with open('bots.txt', 'r') as file:
        for line in file:
            user, bot_count = line.strip().split(":")
            bots[user] = int(bot_count)
    return bots

# Leer los logins desde el archivo logins.txt
def load_logins():
    logins = {}
    with open('logins.txt', 'r') as file:
        for line in file:
            user, password = line.strip().split(":")
            logins[user] = password
    return logins

# Iniciar sesión
def login():
    logins = load_logins()
    print(f"{BLUE}Welcome to Osais C2!{RESET}")
    while True:
        username = input(f"{BLUE}Username: {RESET}")
        password = input(f"{BLUE}Password: {RESET}")
        if username in logins and logins[username] == password:
            print(f"{BLUE}Login successful!{RESET}")
            return username
        else:
            print(f"{WHITE}Invalid login. Please try again.{RESET}")

# Mostrar el estado de los bots
def show_status(bots, username):
    print(f"\n{BLUE}Osais C2 Status - User: {username}{RESET}")
    if username in bots:
        print(f"{WHITE}Bots Available: {bots[username]}{RESET}")
    else:
        print(f"{WHITE}No bots available for this account.{RESET}")
    
    print(f"\n{BLUE}Commands:{RESET}")
    print(f"{WHITE}.attack - Launch attack using bots{RESET}")
    print(f"{WHITE}.exit - Exit C2{RESET}")

# Comando para iniciar el ataque
def start_attack(bots, username):
    if username not in bots or bots[username] == 0:
        print(f"{WHITE}No bots available to attack. Please check your bot count.{RESET}")
        return
    
    # Simulamos la ejecución del ataque (llama al script attack.py)
    subprocess.run(["python3", "attack.py", "127.0.0.1", "80", "100"])
    bots[username] -= 1
    print(f"{BLUE}Attack sent successfully with 100 threads and 1024 bytes!{RESET}")
    print(f"{WHITE}Bots remaining: {bots[username]}{RESET}")
    
    # Guardar el estado actualizado de bots
    save_bots(bots)

# Guardar el estado actualizado de los bots
def save_bots(bots):
    with open('bots.txt', 'w') as file:
        for user, bot_count in bots.items():
            file.write(f"{user}:{bot_count}\n")

# Main loop
def main():
    bots = load_bots()
    username = login()
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la terminal
    while True:
        show_status(bots, username)
        
        command = input(f"{BLUE}osais:{RESET} ")
        
        if command == ".attack":
            start_attack(bots, username)
        elif command == ".exit":
            print(f"{BLUE}Exiting Osais C2...{RESET}")
            break
        else:
            print(f"{WHITE}Unknown command. Type .attack or .exit{RESET}")

if __name__ == "__main__":
    main()
