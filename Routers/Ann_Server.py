from router_main import *
import socket

# Read Ann-Chan file
file_content = read_file("../Text Files/Supplemental Text Files/Ann/Ann-_Chan.txt")
content_length = len(file_content)
line_index = 0

# Open Ann-Chan log file
file = open("../Text Files/Logs/Ann-Chan.txt", "w")

# JSON Packet
packet = """{
    "sID": "111",
    "dID": "001",
    "seq": "13510",
    "ack": "13513",
    "hdrLen": "10",
    "DRP": "0",
    "TER": "0",
    "URG" :"0",
    "ACK" :"0",
    "RST" :"0",
    "SYN" :"0",
    "FIN" :"0",
    "cksum" : "0",
    "data": ""
}"""

packet_json = json.loads(packet)

# Connect the socket to the port where the server is listening
sockA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portA = ROUTER_DICT["A"]
routerA_address = ('localhost', portA)
print("Connecton to localhost:{}".format(portA))
sockA.connect(routerA_address)

counter = 0
try:
    # Send data
    i = 0
    while line_index < content_length:
        if counter == 5:
            file.close()
            break
        if i >= 1:
            packet_json = json.loads(packet_json)
    
        packet_json["data"] = file_content[line_index]
        sent_string = "Sent: " + packet_json["data"] + "\n"
        packet_json = json.dumps(packet_json)
        i = i +1
        #packet_json["seq"] = str(int(packet["seq"]) + 1)

        packet_bytes = bytes(packet_json, "utf-8")

        line_index = line_index + 1
        #bytes_message = bytes(packet_bytes, "utf-8")
        print("Sending message: {}".format(packet_json))
        file.write(sent_string)
        sockA.sendall(packet_bytes)

        data = sockA.recv(1024)
        string_data = str(data, "utf-8")
        received_packet = json.loads(string_data)
        print("Received: {}\n".format(string_data))
        file.write("Received: " + received_packet["data"] + "\n\n")
        counter = counter + 1

finally:
    print("Closing socket.")
    sockA.close()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = ROUTER_DICT["Ann"]

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
                packet = json.loads(string_data)

                print("Received line {}. Sending acknowledgement back to client...\n".format(packet["data"]))
                # log packet["data"] to a log file
                connection.sendall(packet["data"]) # send ack

            else:
                print("No more data from: {}".format(client_address))
                break

    finally:
        # Clean up the connection
        connection.close()
