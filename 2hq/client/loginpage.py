from tkinter import *
from tkinter.messagebox import showinfo


class loginPage(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.loginSucc=False
        self.master=master
        self.name=None
        self.createWidget()
    def createWidget(self):
        self.input=Entry(self)
        self.input.pack()
        Button(self,text='entry',command=self.clickEveEntry).pack(pady=8)
    def clickEveEntry(self):
        self.name=self.input.get()
        if not self.name:
            showinfo(title='hint',message='input your name,please')
            return 0
        self.loginSucc=True
        self.destroy()
    def getloginSucc(self):
        return self.loginSucc
    def getname(self):
        return self.name
if __name__ == '__main__':
    root=Tk(className='loginPage')
    root.geometry('500x500+200+200')
    root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
    loginPage=loginPage(root)
    loginPage.place(x=0,y=0,relwidth=1,relheight=1)
    root.mainloop()
