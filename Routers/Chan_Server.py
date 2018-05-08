from router_main import *
import socket

# Read Chan-Ann file
file_content = read_file(
    "../Text Files/Supplemental Text Files/Chan/Chan-_Ann.txt")
content_length = len(file_content)
line_index = 0

# Open Ann-Chan log file
file = open("../Text Files/Logs/Chan-Ann.txt", "w")

# JSON Packet
packet = """{
    "sID": "001",
    "dID": "111",
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

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = ROUTER_DICT["Chan"]

# Bind the socket to the port
server_address = ('localhost', port)
print("Listening on port: {}".format(port))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
counter = 0
while True:
    # Wait for a connection
    print("Waiting for connection...")
    connection, client_address = sock.accept()
    print(connection)
    print(client_address)

    # Maybe change value of "connection" to change what router to send to?
    i = 0
    try:
        print("Connection from: {}".format(client_address))
        line_received = 0
        # Receive the data in small chunks and retransmit it
        while counter != 5:

            data = connection.recv(1024)
            if data:
                string_data = str(data, "utf-8")
                received_packet = json.loads(string_data)
                print("Received: {}\n".format(received_packet["data"]))
                file.write("Received: " + received_packet["data"] + "\n")

                if line_index < content_length:
                    if i >= 1:
                        packet_json = json.loads(packet_json)
                    
                    packet_json["data"] = file_content[line_index]
                    packet_json = json.dumps(packet_json)
                    i = i + 1
                    #packet_json["seq"] = str(int(packet["seq"]) + 1)

                    packet_bytes = bytes(packet_json, "utf-8")

                    line_index = line_index + 1
                    #bytes_message = bytes(packet_bytes, "utf-8")
                    print("Sending message: {}".format(packet_json))
                    counter = counter + 1
                    file.write("Sending: " + file_content[line_index] + "\n\n")
                    connection.sendall(packet_bytes)

                #connection.sendall(packet["data"])  # send ack

            else:
                print("No more data from: {}".format(client_address))
                break

    finally:
        # Clean up the connection
        file.close()
        connection.close()
