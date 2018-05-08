import socket

# Reads each line of file and stores in a list called "content"
def read_file(filename):
    with open(filename) as file:
        content = file.readlines()

    content = [line.strip() for line in content]  # Strips \n from each line
    return content

# Read Ann-Chan file
file_content = read_file("../Text Files/Supplemental Text Files/Ann/Ann-_Chan.txt")
content_length = len(file_content)
line_index = 0

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port = 8090
server_address = ('localhost', port)
print("Connecton to localhost:{}".format(port))
sock.connect(server_address)

try:

    # Send data
    while line_index < content_length:
        message = file_content[line_index]
        line_index = line_index + 1
        bytes_message = bytes(message, "utf-8")
        print("Sending message: {}".format(message))
        sock.sendall(bytes_message)
        
        data = sock.recv(30)
        print("routerA received line: {}".format(data))
    # Look for the response
    # amount_received = 0
    # amount_expected = len(message)

    # while amount_received < amount_expected:
    #     data = sock.recv(30)
    #     amount_received += len(data)
    #     print("Received: {}".format(data))


finally:
    print("Closing socket.")
    sock.close()
