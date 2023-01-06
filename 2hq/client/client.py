import socket
import threading
import time

class Client():
    def __init__(self,name,host='192.168.0.10',port=8888):
        self.host=host
        self.port=port
        self.name=name
        self.cli_soc=socket.socket()
        self.cli_soc.connect((self.host,self.port))
    def sendmes(self,mes:str):
        mes=f'{self.name}:{mes}'
        self.cli_soc.send(mes.encode())
    def getMes(self):
        rec_data=self.cli_soc.recv(1024).decode()
        return rec_data

if __name__ == '__main__':
    cli=Client('zjl')
    def sendmes():
        while True:
            cli.sendmes('hello')
            time.sleep(1)
    threading.Thread(target=sendmes).start()
    while True:
        mes=cli.getMes()
        print(mes)