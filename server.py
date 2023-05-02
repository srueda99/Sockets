import socket

# Se crean los sockets del lado del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# El servidor estará activo localmente y por el puerto 8041
server_address = ('localhost', 8041)
server_socket.bind(server_address)
server_socket.listen(1)
print(f"Servidor activo: {server_address}")

# Establece la conexión con el cliente
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con: {client_address}")

while True:
    try:
        # Recibe el mensaje del cliente
        message = client_socket.recv(1024)

        # Imprime el mensaje recibido del cliente
        print(message.decode())

        # Envía los dos chulos de que el mensaje fue recibido
        response = "√√"
        client_socket.sendall(response.encode())

        # Si el cliente cierra la conexión entonces el servidor también se cierra
        if not message:
            print("El cliente cerró la conexión")
            break

    except socket.error as e:
        print(f"Hubo un error: {e}")
        break
    except KeyboardInterrupt:
        print('Servidor interrumpido...')
        break

# Cierra la conexión con el cliente
client_socket.close()