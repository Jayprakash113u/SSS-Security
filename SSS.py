from tkinter import *
from PIL import ImageTk, Image
import os
import subprocess

def batfile1():
    subprocess.call([r'batch1.bat'])



def write_File (text_File):
    file = open("hosts.txt", "a")

    user_Input = text_File.get()

    file.write(user_Input+"\n")
    file.close()
    subprocess.call([r'batch.bat'])



def batfile():
    subprocess.call([r'batch.bat'])



def close_window ():
    top.destroy()





def new_winF():
    top = Toplevel()

    def close_window2():
        top.destroy()
    top.title('Hello, Tkinter!')
    top.geometry("500x540")

    frame = Frame(top, relief=RAISED, borderwidth=1)
    frame.pack(fill=BOTH, expand=True)
    img = ImageTk.PhotoImage(Image.open("win2.png"))
    panel = Label(frame, image = img)
    panel.pack(side = TOP, fill = BOTH, expand = YES)
    closeButton = Button(top, text="Close", bg="black", fg="white", width=10, command=close_window2)
    closeButton.pack(side=RIGHT, padx=5, pady=5)
    okButton = Button(top, text="OK", bg="black", fg="white", width=20, command=batfile)
    okButton.pack(side=RIGHT)
    top.mainloop()




def new_winF2():
    top1 = Toplevel()
    def close_window ():
        top1.destroy()
    top1.geometry("500x540")
    frame = Frame(top1, relief=RAISED, borderwidth=1)
    frame.pack(fill=BOTH, expand=True)
    img = ImageTk.PhotoImage(Image.open("Add Website.png"))
    panel = Label(frame, image = img)
    panel.pack(side = TOP, fill = BOTH, expand = YES)
    the_input = Entry(top1,bg="grey",width=40)
    the_input.pack(side=LEFT)
    button_Write = Button(top1, text = "Close", bg="black", fg="white",width=15,command=close_window).pack(side=RIGHT)
    button_Write = Button(top1, text = "ADD", bg="black", fg="white",width=20, command = lambda: write_File(the_input)).pack(side=RIGHT)
    top1.mainloop()

def new_winF3():
    top2 = Toplevel()

    filename = "notes.txt"

    top2.geometry("1000x550")

    img = ImageTk.PhotoImage(Image.open("final notes(1).png"))
    panel = Label(top2, image = img)
    panel.pack(side = TOP, fill = BOTH, expand = YES)
    top = Frame(top2)
    top.pack(side='bottom')
    text =Text(panel


           )
    text.pack(side=RIGHT)

    text.insert('end', open(filename,'r').read())
    Button(top2, text='QUIT', command=top2.destroy, bg="black", fg="white", width="20").pack(side="right", pady=10)
    top2.mainloop()


def new_winF4():

    top4 = Toplevel()
    def close_window ():
        top4.destroy()
    top4.title('Hello, Tkinter!')
    top4.geometry("500x540")

    frame = Frame(top4, relief=RAISED, borderwidth=1)
    frame.pack(fill=BOTH, expand=True)
    img = ImageTk.PhotoImage(Image.open("win3.png"))
    panel = Label(frame, image = img)
    panel.pack(side = TOP, fill = BOTH, expand = YES)
    closeButton = Button(top4,text="Close", bg="black", fg="white", width=10, command=close_window)
    closeButton.pack(side=RIGHT, padx=5, pady=5)
    okButton = Button(top4,text="OK", bg="black", fg="white", width=20, command=batfile1)
    okButton.pack(side=RIGHT)
    top4.mainloop()









root = Tk()
root.title('MAIN')
root.geometry("1199x680")


img = ImageTk.PhotoImage(Image.open("back.png"))
panel = Label(root, image = img)
panel.pack(side = TOP, fill = BOTH, expand = YES)
w = Frame(panel, height=628, width=200)
w.grid(column=0)
label = Label(w, bg="black", height="9", width="20")
label.pack(side=TOP)
button=Button(w, text="SSS SECURITY", bg="black", fg="white", command=new_winF, pady=10)
button.pack(side=TOP, fill=BOTH, expand=YES)
label = Label(w, bg="black", height="5", width="20")
label.pack(side=TOP)
button=Button(w, text="ADD WEBSITE", bg="black", fg="white", command=new_winF2, pady=10)
button.pack(side=TOP, fill=BOTH, expand=YES)
label = Label(w, bg="black", height="5", width="20")
label.pack(side=TOP)
button=Button(w, text="REMOVE", bg="black", fg="white", command=new_winF4, pady=10)
button.pack(side=TOP, fill=BOTH, expand=YES)
label = Label(w, bg="black", height="5", width="20")
label.pack(side=TOP)
button=Button(w, text="NOTES", bg="black", fg="white", command=new_winF3, pady=10)
button.pack(side=TOP, fill=BOTH, expand=YES)
label = Label(w, bg="black", height="9", width="20")
label.pack(side=TOP)



root.mainloop()
