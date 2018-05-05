# Name: Kartik Gupta
# ID:   1001228675

# importing socket and threading libraries
import socket
import threading


# defining class ClientThread for multithreading and its functionality
class ClientThread(threading.Thread):
    # initialization function for the class ClientThread
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.clientAddress = clientAddress
        self.cSocket = clientSocket

    # function to run the new thread and execute the program
    def run(self):
        # try block for trying if the received file request is an actual file or not
        try:
            # receiving the message from the client
            message = (self.cSocket.recv(1024)).decode()
            # splitting the GET request to extract the requested file name
            filename = message.split()[1]
            # opening the file if it exists in the directory
            f = open(filename[1:])
            # printing connection success message
            print("Connection Accepted!")
            # assigning the data of the opened file
            outputdata = f.read()
            # header line for HTTP requests for finding the file to the client
            self.cSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            # sending the file to the client
            self.cSocket.send(outputdata.encode())
            # printing important information of the connection with the client to the server
            print("Client IP Address : ", self.clientAddress[0])
            print("Client Port no. : ", self.clientAddress[1])
            print("Client Host name: localhost")
            print("Peer name : ", self.cSocket.getpeername())
            print("Socket Family : ", self.cSocket.family)
            print("Type : ", self.cSocket.type)
        # except block for handling the file not found exception
        except IOError:
            # header line for HTTP requests for not finding the file to the client
            self.cSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        # closing the connection to this client once the requested file is received
        self.cSocket.close()


# defining the host and port the server is running on
host = "localhost"
port = 8090
# creating the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# letting the port number be reused for multiple executions
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# binding the host and port to form the server
server.bind((host, port))
# printing message for the server to show that it is waiting on clients
print("Waiting for connection")
# while loop for multiple connections from clients
while True:
    # queueing requests - 1
    server.listen(1)
    # server is accepting requests from clients now
    clientSock, clientAddress = server.accept()
    # creating a new thread of the new client and calling the initialization function
    newThread = ClientThread(clientAddress, clientSock)
    # starting the new thread for execution
    newThread.start()
