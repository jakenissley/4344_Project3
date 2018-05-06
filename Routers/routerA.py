from router_main import dijkstra, print_paths
import socket

print_paths("A")
print("\n")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8090

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

    try:
        print("Connection from: {}".format(client_address))
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(30)
            print("Received: {}".format(data))
            if data:
                print("Sending data back to client...")
                connection.sendall(data)
            else:
                print("No more data from: {}".format(client_address))
                break

    finally:
        # Clean up the connection
        connection.close()
