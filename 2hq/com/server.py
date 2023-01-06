import threading

from configmodel import config as cfig
from tkinter import *
from threading import *
import socket
class Server():
    def __init__(self):
        self.init()
    def init(self):
        self.server=socket.socket()
        self.server.bind(('192.168.0.10',8888))
        self.server.listen(3)

    def lis_cli_con(self):
        self.conWiCliInf: tuple = self.server.accept()
        self.conWiCli: socket.socket = self.conWiCliInf[0]
        return self.conWiCli
    def getmes(self):
        rev_data = self.conWiCli.recv(1024).decode('utf-8')
        return rev_data
class mainPage(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.createWidget()
        self.server=Server()
        thr_list=threading.Thread(target=self.lis_con_cli)
        thr_list.start()
    def createWidget(self):
        self.messbox=Listbox(self.master,bg=cfig.get_color(),selectmode=MULTIPLE)
        self.messbox.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.8)
    def deal(self,con:socket.socket):
        while True:
            res=con.recv(1024).decode('utf-8')
            self.messbox.insert(END,f'client{res}')
    def lis_con_cli(self):
        while True:
            con=self.server.lis_cli_con()
            print('a client')
            thr_con=threading.Thread(target=self.deal(con))
            thr_con.start()
if __name__ == '__main__':
    root=Tk(className='server')
    root.geometry('500x500+200+200')
    root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
    main_page=mainPage(root)
    main_page.place(x=0,y=0,relheight=1,relwidth=1)
    main_page.pack()
    root.mainloop()

