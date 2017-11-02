#!/usr/bin/env python3
# _*_ coding = utf-8 _*_

from tkinter import *
# 关于图形窗口
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello,World!')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='Quit',command = self.quit)
        self.quitButton.pack()

app = Application()
app.master.title('Hello World!')
app.mainloop()