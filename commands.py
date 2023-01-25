import webbrowser
import tkinter
import sys
from PIL import Image, ImageTk
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
    item1 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item1')
    item2 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item2')
    item3 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item3')
    item4 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item4')
    backpackhossza = tkinter.Label(ablak, height=2, width=5, text=len(inventory))
    reroll = tkinter.Button(ablak, height=5, width=10, background='#ffffff', text="rerollkep")#, command=rerollbutton)
    #elfelejtettem ez a gomb mit akarˇ passol. Kihagy egy kört
    passgomb = tkinter.Button(ablak, height=5, width=10, background='#ffffff', text="valamikep")#, command=valamibutton)
    trash = tkinter.Button(ablak, height=3, width=8, background='#ffffff', text="trashkep")#, command=trashbutton) 
    wavecounter = tkinter.Label(ablak, height=6, width=15, background='#ffffff', text="wavecounter")#, command=wavecounter)
    kilep = tkinter.Button(ablak, height=2, width=15, background='#ffffff', text="Exit")#, command=biztoshkilepszV2)

    gamecanvas.create_window(130, 715, window=item1)
    gamecanvas.create_window(386, 715, window=item2)
    gamecanvas.create_window(642, 715, window=item3)
    gamecanvas.create_window(898, 715, window=item4)
    gamecanvas.create_window(20, 20, window=backpackhossza)
    gamecanvas.create_window(970, 560, window=reroll)
    gamecanvas.create_window(54, 560, window=passgomb)
    gamecanvas.create_window(54, 480, window=trash)
    gamecanvas.create_window(965, 70, window=wavecounter)
    gamecanvas.create_window(100, 20, window=kilep)
    
    # test_label = tkinter.Label(text='anyád')
    # gamecanvas.create_window(200, 200, window=test_label)
def segitseg():
    webbrowser.open_new(r"help.html")

#def rerollbutton():


#def valamibutton():


#def trashbutton():


#def wavecounter():


# def biztoshkilepsz():
#     ablak = tkinter.Tk()
#     ablak.configure(bg='#ffffff')
#     # ablak.resizable(width=False, height=False)
#     ablak.title("Exit")
#     focanvas = tkinter.Canvas(ablak, height = 500, width = 500, background= '#ffffff', relief='flat')
#     cim = tkinter.Label(ablak, text = 'Are you sure?', font = ('Fette UNZ Fraktur', 25), foreground = '#850505', background='#ffffff')
#     igengomb = tkinter.Button(ablak, height = 1, width= 5, text='Yes', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', command=kilepigen)
#     nemgomb = tkinter.Button(ablak, height = 1, width= 5, text='No', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505')

#     focanvas.create_window(250, 100, window = cim)
#     focanvas.create_window(166, 200, window = igengomb)
#     focanvas.create_window(333, 200, window = nemgomb)

#     focanvas.pack()

#     ablak.mainloop()
def kilepigen():
    sys.exit()