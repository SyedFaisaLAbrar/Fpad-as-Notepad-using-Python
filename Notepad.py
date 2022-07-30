from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import tkinter.messagebox as tmsg
import os


def newFile():

    global file
    global new_Name
    def created():
        global new_Name
        global file
        root.title(f"{new_Name.get()}.txt - F Pad")
        file = f"{new_Name.get()}.txt"
        textArea.delete(1.0, END)
        newWindow.destroy()

    newWindow = Toplevel(root)
    newWindow.geometry("570x200")
    newWindow.title("Create File - F Pad")
    newWindow.resizable(0,0)
    Frame(newWindow, pady=10, bg="Sky Blue").grid(row=0,column=0,padx=20,pady=40)
    # f = Frame(newWindow, pady=10, bg="Sky Blue")
    # f.pack(fill=BOTH, pady=10)


    # Label(newWindow,bg="Light Grey").grid(row=0,column=0,padx=20,pady=20)
    Label(newWindow,text = "New File",font="Ubunda 10 bold",fg="Grey").grid(row=2,column=1)
    new_Name.set("untitled")
    Entry(newWindow,textvariable=new_Name,font="Ubunda 10").grid(row=2,column=2,padx=20)
    Label(newWindow,text = ".txt",font="Ubunda 10").grid(row=2,column=3)

    photo = ImageTk.PhotoImage(Image.open("10.png"))
    Button(newWindow, image=photo, borderwidth=0, command=created).grid(row=3,column=2,padx=20,pady=20)
    Button.configure()


def openFile():
    global file
    file= askopenfilename(defaultextension=".txt",filetypes=[("All Files ","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file + " - F Pad"))
        textArea.delete(1.0,END)
        f = open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()

pointer =0
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt",
                                 filetypes=[("All Files ","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file + " - F Pad"))
    elif file == f"{new_Name.get()}.txt":
        file = asksaveasfilename(initialfile=f"{new_Name.get()}.txt",
                                 filetypes=[("All Files ", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file + " - F Pad"))

    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def exitApp():
    root.destroy()
def copyFile():
    textArea.event_generate('<<Copy>>')
def cutFile():
    textArea.event_generate('<<Cut>>')
def pasteFile():
    textArea.event_generate('<<Paste>>')

def aboutFile():
    tmsg.showinfo("About", "You Using Notepad build using Python 3 for writting purpose."
                           "\n\n\nTitle            :      F Pade"
                           "\n\nCredited By    :     Syed Faisal Abrar\n\n"
                           "Published On :      28 July, 2022\n")
def audioFunc():
    tmsg.showinfo("Comin Soon !","Working On It.\nThis feature will be added shortly. Thanks! ")

root = Tk()
root.geometry("950x600")
root.wm_iconbitmap("icon.ico")
root.title("untitle.txt - F Pad")

f = Frame(root,pady=10,bg="Sky Blue")
f.pack(fill=BOTH)
f = Frame(root,pady=10,bg="Sky Blue")
f.pack(fill=BOTH,pady=10)
f = Frame(root,pady=10,bg="Light Grey")
f.pack(fill=BOTH,side=LEFT)
f = Frame(root,pady=10,bg="Light Grey")
f.pack(fill=BOTH,side=LEFT)

f1 = Frame(root)

Label(f1,text= "F Pad",font= "Ubundu 20 bold",fg="#22C1F5").pack(side=TOP)
Label(f1,text= "Write From World Of Your Thoughts",font= "Ubundu 10",fg="Grey").pack()


photo1 = ImageTk.PhotoImage(Image.open("1.png"))
Button(f1,image=photo1,borderwidth=0,command=newFile).pack(side=LEFT,pady=10,anchor= SW)
photo2 = ImageTk.PhotoImage(Image.open("2.png"))
Button(f1,image=photo2,borderwidth=0,command=openFile).pack(side=LEFT)
photo3 = ImageTk.PhotoImage(Image.open("3.png"))
Button(f1,image=photo3,borderwidth=0,command=saveFile).pack(side=LEFT)
photo4 = ImageTk.PhotoImage(Image.open("4.png"))
Button(f1,image=photo4,borderwidth=0,command=copyFile).pack(side=LEFT)
photo5 = ImageTk.PhotoImage(Image.open("5.png"))
Button(f1,image=photo5,borderwidth=0,command=cutFile).pack(side=LEFT)
photo6 = ImageTk.PhotoImage(Image.open("6.png"))
Button(f1,image=photo6,borderwidth=0,command=pasteFile).pack(side=LEFT)
photo7 = ImageTk.PhotoImage(Image.open("7.png"))
Button(f1,image=photo7,borderwidth=0,command=exitApp).pack(side=RIGHT,padx=10,pady=10)
photo8 = ImageTk.PhotoImage(Image.open("8.png"))
Button(f1,image=photo8,borderwidth=0,command=aboutFile).pack(side=LEFT,pady=10)
photo9 = ImageTk.PhotoImage(Image.open("9.png"))
Button(f1,image=photo9,borderwidth=0,command=audioFunc).pack(side=LEFT,pady=10)

f1.pack(fill=BOTH)

file=None
new_Name = StringVar()

textArea = Text(root,font="Ubundu 11 italic",fg="grey")
textArea.pack(fill=BOTH,expand=True,pady=10)
scroll = Scrollbar(textArea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command= textArea.yview())
textArea.config(yscrollcommand= scroll.set)

root.mainloop()