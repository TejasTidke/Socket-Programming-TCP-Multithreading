import socket
import threading

#49152-65535
class ThreadedServer():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 49159
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))

    def listen(self):
        self.s.listen(5)
        while True:
            c, addr = self.s.accept()
            c.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (c,addr)).start()

    def listenToClient(self, c, addr):
        block_size = 1024
        print('Got connection from', addr)

        data = c.recv(1024)
    
        if (data.decode() == "download"):
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

        elif (data.decode() == "upload"):
            FileName = c.recv(1024)
            downfile = FileName.decode()
            Data = c.recv(1024)
            DownloadFile = open(downfile,"wb")
            i = 1
            while Data:
                print('Recieving...%d' %(i))
                DownloadFile.write(Data)
                Data = c.recv(1024)
                i = i + 1
            print("Done Recieving")
            DownloadFile.close()
            c.close()
        
                 
if __name__ == "__main__":
    ThreadedServer().listen()
