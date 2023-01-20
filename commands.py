import webbrowser
import tkinter
import sys
from events import *
def gamestart(bezar, enemies, items, inventory, save, ablak):
    enemyread(enemies)
    itemread(items)
    saveread(save, 'r')
    invread(inventory, 'a')
    bezar.pack_forget()
    global gamecanvas
    gamecanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#230259', relief='flat')
    gamecanvas.pack()
    # test_label = tkinter.Label(text='anyád')
    # gamecanvas.create_window(200, 200, window=test_label)
def segitseg():
    webbrowser.open_new(r"help.html")
def biztoshkilepsz():
    ablak = tkinter.Tk()
    ablak.configure(bg='#ffffff')
    # ablak.resizable(width=False, height=False)
    ablak.title("Exit")
    focanvas = tkinter.Canvas(ablak, height = 500, width = 500, background= '#ffffff', relief='flat')
    cim = tkinter.Label(ablak, text = 'Are you sure?', font = ('Fette UNZ Fraktur', 25), foreground = '#850505', background='#ffffff')
    igengomb = tkinter.Button(ablak, height = 1, width= 5, text='Yes', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', command=kilepigen)
    nemgomb = tkinter.Button(ablak, height = 1, width= 5, text='No', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505')

    focanvas.create_window(250, 100, window = cim)
    focanvas.create_window(166, 200, window = igengomb)
    focanvas.create_window(333, 200, window = nemgomb)

    focanvas.pack()

    ablak.mainloop()
def kilepigen():
    sys.exit()