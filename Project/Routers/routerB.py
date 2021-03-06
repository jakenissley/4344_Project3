from router_main import *
import socket

print_paths("B")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = ROUTER_DICT["B"]

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
                string_data = str(data, "utf-8")
                print("Received: {}".format(string_data))

                line_received = line_received + 1
                line_received_string = str(line_received)

                print("Received line {}. Sending acknowledgement back to client...\n".format(
                    line_received))
                bytes_line = bytes(str(line_received_string), "utf-8")
                connection.sendall(bytes_line)
            else:
                print("No more data from: {}".format(client_address))
                break

    finally:
        # Clean up the connection
        connection.close()
