import random
import time
import ctypes
import keyboard
from colorama import Fore, Style, init
import sys
import ctypes

# Establece el ícono del programa
if sys.platform == 'win32':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('myappid')
    ctypes.windll.kernel32.SetConsoleIcon(ctypes.windll.shell32.Shell_GetCachedImageIndexW('path\\to\\icon.ico', 0, 0x0000))

init()

# Variables iniciales
total_checks = 0
bitcoins_encontrados = 0
wallets = []

# Función para generar una dirección de wallet aleatoria y balance inicial
def generar_wallet():
    caracteres = "0123456789abcdef"
    direccion = "0x"
    for _ in range(40):
        direccion += random.choice(caracteres)
    balance = round(random.uniform(0, 3), 1)
    return {'direccion': direccion, 'balance': balance}

# Función para convertir bitcoins a dólares
def convertir_a_dolares(bitcoins):
    # Coloca aquí tu lógica de conversión de bitcoins a dólares
    # Puedes usar una API externa o un valor fijo
    return bitcoins * 50000

# Función para actualizar el título del CMD
def actualizar_titulo(total_checks, bitcoins_encontrados):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Total Checks: {total_checks} | Found (BITCOINS) = {convertir_a_dolares(bitcoins_encontrados)}")

# Función para intentar entrar a una wallet
def intentar_entrar_a_wallet(wallets):
    global total_checks, bitcoins_encontrados
    
    # Obtener una wallet aleatoria
    wallet = random.choice(wallets)
    
    # Verificar si la wallet tiene balance suficiente para recibir bitcoins
    if wallet['balance'] <= 0:
        return
    
    # Simulación de balance y bitcoins recibidos
    balance = round(random.uniform(0, wallet['balance']), 1)
    bitcoins_recibidos = min(round(random.uniform(0, 10), 1), wallet['balance'])
    
    # Actualizar el balance de la wallet
    wallet['balance'] -= bitcoins_recibidos
    
    # Actualizar estadísticas
    total_checks += 1
    bitcoins_encontrados += bitcoins_recibidos
    
    # Actualizar el título del CMD
    actualizar_titulo(total_checks, bitcoins_encontrados)
    
    # Mostrar los resultados en pantalla
    print(Fore.GREEN + f"Balance: {balance} | Received: {bitcoins_recibidos} | Address: {wallet['direccion']}" + Style.RESET_ALL)

# Función para iniciar la simulación
def iniciar_simulacion(wallets):
    print("Simulación iniciada...")
    print("Presiona ESC para detener la simulación.")
    
    while True:
        # Verificar si se ha presionado la tecla ESC
        if keyboard.is_pressed('esc'):
            break
        
        # Simulación de "entrar a wallets"
        intentar_entrar_a_wallet(wallets)
        
        # Esperar un segundo antes de intentar la siguiente wallet
        time.sleep(0.01)
    
    print("Simulación detenida.")


# Programa principal
def main():
    # Título y versión del programa
    print(Fore.RED + " ██▓███   ██▀███  ▓█████   ██████   ██████ ▓█████  ██▀███  ")
    print("▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒")
    print("▓██░ ██▓▒▓██ ░▄█ ▒▒███   ░ ▓██▄   ░ ▓██▄   ▒███   ▓██ ░▄█ ▒")
    print("▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ")
    print("▒██▒ ░  ░░██▓ ▒██▒░▒████▒▒██████▒▒▒██████▒▒░▒████▒░██▓ ▒██▒")
    print("▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░")
    print("░▒ ░       ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░")
    print("░░         ░░   ░    ░   ░  ░  ░  ░  ░  ░     ░     ░░   ░ ")
    print("            ░        ░  ░      ░        ░     ░  ░   ░     ")
    print("                                                            Beta" + Style.RESET_ALL)
    
    print("\nPresiona B para iniciar...")
    
    while True:
        if keyboard.is_pressed('b'):
            wallets = [generar_wallet() for _ in range(1000)]
            iniciar_simulacion(wallets)
            configurar_simulacion()
        
        # Esperar un segundo antes de verificar nuevamente las teclas presionadas
        time.sleep(0.1)

# Iniciar el programa
if __name__ == "__main__":
    main()
