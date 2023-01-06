import threading
import time

from client import Client
from configmodel import config as cfig
from tkinter import *
import socket
count_mes=0
class  chatPage(Frame):
    def __init__(self,master,name=None):
        super().__init__(master)
        self.username=name
        self.master=master
        self.createWidget()
        print('entrychat')
        self.client=Client(name)
        self.senduntoser()
        threading.Thread(target=self.loadmes).start()
    def createWidget(self):
        self.messbox=Listbox(self.master,bg=cfig.get_color(),selectmode=MULTIPLE)
        self.messbox.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.8)
        # input box
        self.input=Entry(self)
        self.input.place(relx=0.3,rely=0.84)
        # button
        Button(self,text='send',command=self.CliEventAbsend).place(relx=0.40,rely=0.90)
    # def launchCli(self):
    #     while True:
    def CliEventAbsend(self):
        mes_send=self.input.get()
        self.client.sendmes(mes_send)
    def loadmes(self):
        while True:
            global count_mes
            count_mes+=1
            mes=self.client.getMes()
            self.messbox.insert(END,mes)
            # scroll to tag end Every third message
            if count_mes>=5:
                count_mes=0
                cur_ind=self.messbox.index('end')
                self.messbox.see(cur_ind)
    def senduntoser(self):
        # send username
        time.sleep(0.1)
        self.client.sendmes(f'---{self.username}---')

if __name__ == '__main__':
    root=Tk(className='client')
    root.geometry('500x500+200+200')
    root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
    main_page=chatPage(root)
    main_page.place(x=0,y=0,relheight=1,relwidth=1)
    root.mainloop()

