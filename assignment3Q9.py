# Web server programming: develop a web server that handles one HTTP request at a time.
# Your web server should accept and parse the HTTP request, get the requested file from the
# server’s file system, create an HTTP response message consisting of the requested file
# preceded by header lines, and then send the response directly to the client. If the requested
# file is not present in the server, the server should send an HTTP “404 Not Found” message
# back to the client.


from socket import *
import sys

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverPort = 6789
    serverIP = "127.0.0.1"
    serverSocket.bind((serverIP, serverPort))
    serverSocket.listen(1)
    print(f"Checking the web server up on port number: {serverPort}")

    while True:
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            print(f"outputdata: {outputdata}")
            # send one HTTP header line into socket
            connectionSocket.send("\nHTTP/1.1 200 OK\n\n".encode())
            # send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            # send response message for file not found
            connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
            # close client socket
            connectionSocket.close()
        serverSocket.close()
        sys.exit() # Terminate the program after sending the corresponding data

if __name__=="__main__":
    main()
