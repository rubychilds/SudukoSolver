import Tkinter
from Tkconstants import *

tk = Tkinter.Tk()


class MyApp:

    def __init__(self,parent):

        self.frame = Tkinter.Frame(tk,relief=RIDGE,borderwidth=2,background = "#BEBEBE")
        self.frame.pack()

        self.message = Tkinter.Message(tk,text="Symbol Disolay")

        label = Tkinter.Label(self.frame,text="Badges")
        label.pack()

        self.button1 = ButtonClass( , BOTTOM)
        self.button1.bind("<Button-1>", self.button1Click)

        self.button2 = ButtonClass( , TOP)
        self.button1.bind("<Button-2>", self.button2Click)


    def button1Click(self, event):
        self.frame.clear()
        self.button2.clear()
        r = c.create_rectangle(50,50,91,67, background ='blue')
        t = Label(c, text="Hello John, Michael, Eric, ...", anchor='w').pack(side = BOTTOM)

        return "YES"

    def button2Click(self, event):
        self.button1.clear()
        r = c.create_rectangle(50,50,91,67, background ='blue')
        t = Label(c, text="Hello John, Michael, Eric, ...", anchor='w').pack(side = TOP)


class ButtonClass:
    """docstring for Button"""
    def __init__(self, file, sideChosen):

        self.b = Button(self.frame, justify = LEFT)
        self.photo = PhotoImage(file)
        self.b.config(image = self.photo, width="10",height="10")
        self.b.pack(side = sideChosen)

myapp = MyApp(tk)
tk.mainloop()