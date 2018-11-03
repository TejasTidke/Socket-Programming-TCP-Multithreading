# Socket-Programming-TCP-Multithreading
### Problem Statement For Above Code
Implement a Multithreaded File Server Using Tcp Sockets.
## File Server (Upload/Download) Using TCP Sockets using python language
- Multiple Clients Can Connect to the Server.
  - There are 3 files named temp.py, temp2.py and temp3.py
  - First run the multiserver.py(in server folder), then run all the above(files in client folder)
  - With the help of Multithreading, You can download from a server and upload on the server through different clients.
- Server create one thread for each client.
  - The line below will create thread for every client connection
    - `threading.Thread(target = self.listenToClient,args = (c,addr)).start()`
- File is divided into 1KB blocks and File is transferred block by block.
  - code ensures that file is recieved at the other end in 1024bytes only at a time, but you can make changes as you want.

