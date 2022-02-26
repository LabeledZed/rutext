from tkinter import *
from tkinter.filedialog import *
import pyautogui

win = Tk()
win.title("RUText Editor")


def darkmode():
    if darkmodee.get() == 0:
        txt.config(bg="#000000", fg="#ffffff")
    elif darkmodee.get() == 1:
        txt.config(bg="#ffffff", fg="#000000")

def open_file():
    filepath = askopenfilename(filetypes = [("RUText Data File",".ak47")])
    if not filepath:
        return
    txt.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text = input_file.read()
        txt.insert(END,text)
        win.title(f"RUText Editor - {filepath}")

def save_file():
    filepath2 = asksaveasfilename(defaultextension="ak47",filetype=[("RUText Data File",".ak47")])
    if not filepath2:
        return
    with open(filepath2,"w") as read_file:
        text = txt.get(1.0,END)
        read_file.write(text)
        win.title(f"RUText Editor - {filepath2}")

def txt_delete():
    txt.delete(1.0, END)

def pag_cut():
    pyautogui.keyDown('ctrl')
    pyautogui.press('x')
    pyautogui.keyUp('ctrl')

def pag_copy():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def pag_paste():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=None)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save as...", command=save_file)
filemenu.add_command(label="Close", command=None)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=None)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=pag_cut)
editmenu.add_command(label="Copy", command=pag_copy)
editmenu.add_command(label="Paste", command=pag_paste)
editmenu.add_command(label="Delete", command=txt_delete)
menubar.add_cascade(label="Edit", menu=editmenu)
viewmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="View",menu=viewmenu)

darkmodee = IntVar()
viewmenu.add_checkbutton(label="Darkmode",onvalue = 0, offvalue = 1, variable = darkmodee, command=darkmode)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=None)
helpmenu.add_command(label="About...", command=None)
menubar.add_cascade(label="Help", menu=helpmenu)


win.config(menu=menubar)
txt = Text(win, bg="#000000", fg="#ffffff")
txt.pack()



win.mainloop()