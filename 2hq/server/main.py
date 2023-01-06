import threading
import server
from configmodel import config as cfig
from tkinter import *
import socket
count_mes=0
from server import Server
class  mainPage(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.createWidget()
        self.server=Server()
        threading.Thread(target=self.launchSer).start()
        threading.Thread(target=self.loadAndSendmes).start()
    def createWidget(self):
        self.messbox=Listbox(self.master,bg=cfig.get_color(),selectmode=MULTIPLE)
        self.messbox.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.8)
    def launchSer(self):
        while True:
            self.server.lis_cli_con()
    def loadAndSendmes(self):
        while True:
            global count_mes
            count_mes+=1
            mes=self.server.getmes()
            self.messbox.insert(END,mes)
            # scroll to tag end Every third message
            if count_mes>=5:
                count_mes=0
                cur_ind=self.messbox.index('end')
                self.messbox.see(cur_ind)
if __name__ == '__main__':
    root=Tk(className='server')
    root.geometry('500x500+200+200')
    root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
    main_page=mainPage(root)
    main_page.place(x=0,y=0,relheight=1,relwidth=1)
    root.mainloop()

