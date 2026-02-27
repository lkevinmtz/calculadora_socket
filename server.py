import socket
import threading

# Funcion vinculada al hilo cliente
def calcular_operacion(cliente, direccion):
    print(f"Conectado a {direccion}")

    # Bucle principal del cliente
    while True:

        # Recepcion del mensaje del cliente
        mensaje = cliente.recv(1024)
        print(f"{[direccion]} dice: {mensaje.decode()}")

        # Condicion para desconectar el cliente
        if not mensaje or mensaje.decode().lower().strip() == "salir":
            print(f"Cliente {direccion} desconectado")
            cliente.close()
            break

        # Decodiicacion y separacion del mensaje en variables individuales
        mensaje_pp = mensaje.decode().strip().split()

        try:
            try:
                # Declaracion de valores y operacion del mensaje
                n1 = float(mensaje_pp[0]) # valor 1
                operacion = mensaje_pp[1] # operacion (+ - * /)
                n2 = float(mensaje_pp[2]) # valor 2

                try:
                    # Logica de las operaciones
                    if operacion == '+':
                        resultado = n1 + n2
                        cliente.send(f"Resultado = {resultado}".encode())
                    elif operacion == '-':
                        resultado = n1 - n2
                        cliente.send(f"Resultado = {resultado}".encode())
                    elif operacion == '*':
                        resultado = n1 * n2
                        cliente.send(f"Resultado = {resultado}".encode())
                    elif operacion == '/':
                        resultado = n1 / n2
                        cliente.send(f"Resultado = {resultado}".encode())
                    else:
                        cliente.send("ERROR: Operador invalido.".encode()) # Condicion para detectar operadores erroneos
                        continue

                    print(f"Operacion realizada y resultado: {n1} {operacion} {n2} = {resultado}")
                    
                except ZeroDivisionError:
                    cliente.send("ERROR: No puedes dividir entre cero.".encode()) # Excepcion para controlar division entre 0
            except IndexError:
                cliente.send("ERROR: Debes ingresar al menos tres 3 valores/caracteres validos.".encode()) # Excepcion para errores de indice del .split() al intentar convertir datos que no existen
        except ValueError:
            cliente.send("ERROR: Uno o varios de los valores ingresados no es un numero".encode()) # Excepcion para controlar errores de tipo de valor

# Creacion y conexion del servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 5000))
servidor.listen()
print("Servidor esperando conexion")

# Bucle principal que detecta conexiones y las vincula a un hilo cliente
while True:
    cliente, direccion = servidor.accept()
    hilo = threading.Thread(target=calcular_operacion, args=(cliente, direccion))

    hilo.daemon = True
    hilo.start()