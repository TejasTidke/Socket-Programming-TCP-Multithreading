import socket               # Import socket module
import os
import sys

#49152-65535
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 49159                # Reserve a port for your service.

s.bind((host, port))       # Bind to the port

s.listen(5)                 # Now wait for connection.
bFileFound = 0

while True:
    c, addr = s.accept()     # Establish connection with other party
    print('Got connection from', addr)

    print(os.listdir("files/")) #Shows all the files at server side
    
    FileName = c.recv(1024)
    for file in os.listdir("files/"):
        if file == FileName.decode():
            FileFound = 1
            break

    if FileFound == 0:
        print(" Not Found On Server")

    else:
        print("File Found")
        upfile = FileName.decode()
        UploadFile = open("files/"+upfile,"rb")
        Read = UploadFile.read(1024)
        i = 1
        while Read:
            print("Sending...%d" %(i))
            c.send(Read) #sends 1KB 
            Read = UploadFile.read(1024)
        print("Done Sending")
        UploadFile.close()
        #s.shutdown(socket.SHUT_WR)
    break

#c.close()
#s.close()

       
'''
    res = input('do you want to send file??(y/n)')
    if(res == 'y'):
        
        ##### Code To Send File ####
        
        f = open('paris.png','rb')
        i = 1
        l = f.read(block_size)
        while (l):
            print('Sending...%d' % (i))
            c.send(l)
            l = f.read(block_size)
            i = i + 1
        f.close()
        print("Done Sending")
        mssg = "Thank You!"
        byt = mssg.encode()
        c.send(byt)
        c.close()
        
        ################################
        
    res = input('do you want to continue??(yes/no)')
    if(res == 'yes'):
        continue
    else:
        c.close()
        break
'''    
    

