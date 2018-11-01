import sys
import socket 
 
skClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skClient.connect(("127.0.0.1",2525))
 
sFileName = input("Enter Filename to download from server : ")
sData = "Temp"
 
while True:
    skClient.send(sFileName.encode())
    sData = skClient.recv(1024)
    fDownloadFile = open(sFileName,"wb")
    while sData:
        print('Recieving...')
        fDownloadFile.write(sData)
        sData = skClient.recv(1024)
    print("Download Completed")
    fDownloadFile.close()
    break
 
skClient.close()
