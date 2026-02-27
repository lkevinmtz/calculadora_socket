import socket

# Creacion del cliente y conexion al servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 5000))

print("OPERACION DE 2 NUMEROS \nIngresa una operacion con la siguiente estructura: \nnum1 + num2 \nnum1 - num2 \nnum1 * num2 \nnum1 / num2 \n")

# Bucle de envio de mensajes al servidor
while True:
    
    # Input del mensaje del cliente
    mensaje = input(str("\nEscribe una operacion o 'salir' para terminar el programa: "))

    # Condicion para controlar inputs vacios
    if mensaje.strip() == "":
        print("ERROR: No puedes ingresar una entrada vacia")
        continue

    # Envio del mensaje del cliente
    cliente.send(mensaje.encode())

    # Recibir respuesta del servidor
    respuesta = cliente.recv(1024)
    print(respuesta.decode())

    # Cierre del bucle y del cliente
    if mensaje.lower().strip() == 'salir':
        print("Conexión cerrada")
        break

cliente.close()

# Kevin Alexis Martinez Cruz, 23220001
# 6to. Semestre, IINF