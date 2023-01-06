import threading
import socket
# the server can be connected by mutil client
data_rec:str=''
# condition:include function release(),wait(),acquire()
cond=threading.Condition()
class Server():
    def __init__(self):
        self.init()
    def init(self):
        self.server=socket.socket()
        self.server.bind(('192.168.0.10',8888))
        self.server.listen(5)

    def lis_cli_con(self):
        self.conWiCliInf: tuple = self.server.accept()
        print('a client')
        conWiCli: socket.socket = self.conWiCliInf[0]
        # when we get a connection object ,we will create a thread to manage the connection
        threading.Thread(target=self.recmsg,args=(conWiCli,)).start()
        threading.Thread(target=self.sendmsg,args=(conWiCli,)).start()

    def sendmsg(self,conWiCli:socket.socket):
        global data_rec
        while True:
            if cond.acquire():
                # wait(),blocking,the thread will release the resource (release the global variable )until be notified
                cond.wait()
                conWiCli.send(data_rec.encode())
                cond.release()

    def wakeupSen(self,data):
        global data_rec
        if cond.acquire():
            data_rec=data
            # notify_all:wake up the thread that call the wait
            cond.notify_all()
            cond.release()
    def recmsg(self,conWiCli:socket.socket):
        while True:
                rev_data = conWiCli.recv(1024).decode('utf-8')
                print(rev_data)
                self.wakeupSen(rev_data)

if __name__ == '__main__':
    server=Server()
    while True:
        server.lis_cli_con()