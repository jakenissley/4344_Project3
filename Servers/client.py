# Name: Kartik Gupta
# ID:   1001228675

# importing socket, sys and time libraries
import socket
import sys
import time

# creating client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# taking in the parameters from the command line and assigning them to variables
host = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

# connecting the socket to the entered host and port and printing the success message to the client
sock.connect((host, int(port)))
print("Connection Accepted!")

# making a GET HTTP request from the provided information
message = "GET /"+filename+" HTTP/1.1"

# storing the start time
start_time = time.time()

# sending the GET request to the server
sock.send(message.encode())

# receiving the file from the server and printing it out to the client
file = sock.recv(1024)
print(file.decode())

# printing important information about the connection to the client
print("Client IP Address : ", sock.getpeername()[0])
print("Client Port no. : ", sock.getpeername()[1])
print("Client Host name: localhost")
print("Peer name : ", sock.getpeername())
print("Socket Family : ", sock.family)
print("Type : ", sock.type)
print("Protocol: ", socket.getservbyport(int(port)))

# printing the total time for the file and data to be retrieved from the server
print("RTT: "+str(time.time() - start_time)+" seconds")

# closing the client socket to the server once all the tasks are performed
sock.close()
