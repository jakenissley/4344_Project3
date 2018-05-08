from router_main import *
import socket

print_paths("E")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = ROUTER_DICT["E"]

# Connection to Chan
sockChan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portChan = ROUTER_DICT["Chan"]
chan_address = ('localhost', portChan)
sockChan.connect(chan_address)

# Bind the socket to the port
server_address = ('localhost', port)
print("Listening on port: {}".format(port))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("Waiting for connection...")
    connection, client_address = sock.accept()
    print(connection)
    print(client_address)

 # Maybe change value of "connection" to change what router to send to?

    try:
        print("Connection from: {}".format(client_address))
        line_received = 0
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                sockChan.sendall(data)
                received_data = sockChan.recv(1024)
                connection.sendall(received_data)
            else:
                print("No more data from: {}".format(client_address))
                break

    finally:
        # Clean up the connection
        connection.close()
