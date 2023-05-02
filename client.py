import socket

# Se crean los sockets para la conexión
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establece la conexión con el socket del servidor, activo en el puerto 8041
server_address = ('localhost', 8041)
client_socket.connect(server_address)
print(f"Conexión establecida con: {server_address}")
print("Para terminar la conexión escriba 'exit'")

# Se crea un bucle para que el usuario escriba los mensajes que desea hasta acabar con un "exit"
while True:
    message = input()
    if message == "exit":
        break
    try:
        # Envia el mensaje al servidor
        client_socket.sendall(message.encode())

        # Espera por una respuesta del servidor
        response = client_socket.recv(1024)

        # Imprime la respuesta del servidor
        print(response.decode())

    except socket.error as e:
        print(f"Ocurrió un error: {e}")
        break

# Cierra la conexión con el servidor
client_socket.close()
