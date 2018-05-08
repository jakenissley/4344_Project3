from router_main import *
import socket

print_paths("A")
print("\n")

# Read Ann-Chan file
#file_content = read_file("../Text Files/Supplemental Text Files/Ann/Ann-_Chan.txt")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = ROUTER_DICT["A"]

# Bind the socket to the port
server_address = ('localhost', port)
print("Listening on port: {}".format(port))
sock.bind(server_address)

# Connection to routerB
sockB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portB = ROUTER_DICT["B"]
routerB_address = ('localhost', portB)
sockB.connect(routerB_address)

# Connection to routerE
sockE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portE = ROUTER_DICT["E"]
routerE_address = ('localhost', portE)
sockE.connect(routerE_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("Waiting for connection...")
    connection, client_address = sock.accept()
    print(connection)
    print(client_address)

    try:
        print("Connection from: {}".format(client_address))
        line_received = 0
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                string_data = str(data, "utf-8")
                #print("Received: {}".format(string_data))
                packet = json.loads(string_data)

                #connection.sendall(bytes_line)

                destination_ID = packet["dID"]
                if destination_ID == "001": # Send to Chan, so send to routerE
                    sockE.sendto(data, ("localhost", ROUTER_DICT["E"]))
                else: # connect to Jan, so send to routerB
                    sockB.sendto(data, ("localhost", ROUTER_DICT["B"]))

                received_data = sockE.recv(1024)
                connection.sendall(received_data)
            else:
                print("No more data from: {}".format(client_address))
                break

    finally:
        # Clean up the connection
        connection.close()
