import socket
from router_main import *


# Read Ann-Chan file
file_content = read_file("../Text Files/Supplemental Text Files/Ann/Ann-_Chan.txt")
content_length = len(file_content)
line_index = 0

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

# Create a TCP/IP socket
sockA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port = ROUTER_DICT["A"]
server_address = ('localhost', port)
print("Connecton to localhost:{}".format(port))
sockA.connect(server_address)

try:

    # Send data
    while line_index < content_length:
        packet_json["data"] = file_content[line_index]
        packet_json = json.dumps(packet_json)
        #packet_json["seq"] = str(int(packet["seq"]) + 1)

        packet_bytes = bytes(packet_json, "utf-8")

        line_index = line_index + 1
        #bytes_message = bytes(packet_bytes, "utf-8")
        print("Sending message: {}".format(packet_json))
        sockA.sendall(packet_bytes)

        data = sockA.recv(30)
        string_data = str(data, "utf-8")
        print("routerA received line: {}\n".format(string_data))

finally:
    print("Closing socket.")
    sockA.close()
