import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port = 8090
server_address = ('localhost', port)
print("Connecton to localhost:{}".format(port))
sock.connect(server_address)

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    bytes_message = bytes(message, "utf-8")
    print("Sending message: {}".format(message))
    sock.sendall(bytes_message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(30)
        amount_received += len(data)
        print("Received: {}".format(data))

finally:
    print("Closing socket.")
    sock.close()
