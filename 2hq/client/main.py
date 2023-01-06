import threading
import time
from tkinter import *
from  chatPage import chatPage
from loginpage import loginPage
root = Tk(className='client')
root.geometry('500x500+200+200')
root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
def showchatPage(loginPage:loginPage):
    # blocking until login successfully
    while True:
        loginSucc=loginPage.getloginSucc()
        name=loginPage.getname()
        print(name)
        if loginSucc:
            main_page = chatPage(root,name)
            main_page.place(x=0, y=0, relheight=1, relwidth=1)
            break
        time.sleep(0.2)

loginPage = loginPage(root)
loginPage.place(x=0, y=0, relheight=1, relwidth=1)
threading.Thread(target=showchatPage,args=(loginPage,)).start()
root.mainloop()