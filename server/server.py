import sys
import socket
import os
 
host = ''
skServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skServer.bind((host,2525))
skServer.listen(10)
print("Server Active")
bFileFound = 0
 
while True:
    Content,Address = skServer.accept()
    print(Address)
    sFileName = Content.recv(1024)
    for file in os.listdir("files/"):
        if file == sFileName.decode():
            bFileFound = 1
            break
 
    if bFileFound == 0:
        print(" Not Found On Server")
 
    else:
        print("File Found")
        upfile = sFileName.decode()
        fUploadFile = open("files/"+upfile,"rb")
        sRead = fUploadFile.read(1024)
        while sRead:
            print('Sending...')
            Content.send(sRead)
            sRead = fUploadFile.read(1024)
        print("Sending Completed")
        fUploadFile.close()
    break
 
Content.close()
skServer.close()
