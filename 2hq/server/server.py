import threading
import socket
import re as reg
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
        print(self.conWiCliInf[1])
        # when we get a connection object ,we will create a thread to manage the connection
        threading.Thread(target=self.recmsg,args=(conWiCli,)).start()
        threading.Thread(target=self.sendmsg,args=(conWiCli,)).start()

    def sendmsg(self,conWiCli:socket.socket):
        global data_rec
        while True:
            if cond.acquire():
                # wait(),blocking,the thread will release the resource (release the global variable )until be notified
                cond.wait()
                try:
                    conWiCli.send(data_rec.encode())
                    cond.release()
                except Exception:
                    # print(data_rec)
                    cond.release()
                    print(Exception)
                    break
    def getmes(self):
        global data_rec
        if cond.acquire():
            # wait(),blocking,the thread will release the resource (release the global variable )until be notified
            cond.wait()
            cond.release()
            return data_rec

    def wakeupSen(self,data):
        global data_rec
        if cond.acquire():
            data_rec=data
            # notify_all:release the resource and wake up the thread that call the wait
            cond.notify_all()
            cond.release()
    def recmsg(self,conWiCli:socket.socket):
        while True:
                rev_data = conWiCli.recv(1024).decode('utf-8')
                # judge if mes is username that was sent by client
                re1 = '---([\S\s]*)---$'
                res = reg.findall(re1, rev_data)
                if len(res) != 0:
                    username = res[0].split('---')[0]
                    self.wakeupSen(f'welcome {username} to chatroom')
                    continue
                self.wakeupSen(rev_data)

if __name__ == '__main__':
    server=Server()
    while True:
        server.lis_cli_con()