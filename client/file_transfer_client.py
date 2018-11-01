import socket               # Import socket module
import sys

#49152-65535
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 49157                # Reserve a port for your service.

s.bind((host, port))   # Bind to the port

try:
    s.connect((host, 49159))
    print("Connected Successfully!")
except Exception as e: 
    print("something's wrong with %s:%d. Exception is %s" % (host, 49159, e))

FileName = input("Enter Filename to Download from server : ")
Data = "Temp"

while True:
    s.send(FileName.encode())
    Data = s.recv(1024)
    DownloadFile = open(FileName,"wb")
    i = 1
    while Data:
        print('Recieving...%d' %(i))
        DownloadFile.write(Data)
        Data = s.recv(1024)
        i = i + 1
    print("Done Recieving")
    DownloadFile.close()
    break

    
s.close


'''
    else:
        print("Enter the option carefully Next time!")
        break

    ##### Code To Recieve File ####
        
    i = 1
    l = s.recv(block_size)
    while (l):
        print("Receiving...%d" % (i))
        l = s.recv(block_size)
        i = i + 1
    print("Done Receiving")
    print(s.recv(1024))
    s.shutdown(socket.SHUT_WR)
    s.close
    
    res = input('do you want to continue??(yes/no)')
    if(res == 'yes'):
        continue
    else:
        break
    ################################
    '''     
