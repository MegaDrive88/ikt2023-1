import webbrowser
import tkinter
import sys
from PIL import Image, ImageTk
from events import *
import random
def gamestart(bezar, enemies, items, inventory, save, ablak):
    enemyread(enemies)
    itemread(items)
    saveread(save, 'r')
    invread(inventory, 'a')
    bezar.pack_forget()
    global gamecanvas
    gamecanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#bbbbbb', relief='flat') # 230259
    gamecanvas.pack()
    item1 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item1')
    item2 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item2')
    item3 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item3')
    item4 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item4')
    backpackhossza = tkinter.Label(ablak, height=2, width=5, text=len(inventory))
    rk = Image.open('rerollkep.png').resize((60, 60))
    rerollkep = ImageTk.PhotoImage(rk)
    reroll = tkinter.Button(ablak, height=80, width=100, background='#ffffff', text="__", relief='flat', image=rerollkep)#, command=rerollbutton)
    passgomb = tkinter.Button(ablak, height=5, width=15, background='#ffffff', text="valamikep", relief='flat')#, command=valamibutton)    , highlightbackground = "#000000", highlightthickness=1, bd = 0
    trash = tkinter.Button(ablak, height=3, width=8, background='#ffffff', text="trashkep", relief='flat')#, command=trashbutton) 
    wavecounter = tkinter.Label(ablak, height=5, width=15, background='#ffffff', text="wavecounter", relief='flat')#, command=wavecounter)
    kilep = tkinter.Button(ablak, height=2, width=15, background='#ffffff', text="Exit", relief='flat')#, command=biztoshkilepszV2)
    enemy1 = tkinter.Button(ablak, background='#ff0000', height=10, width=8)
    enemy2 = tkinter.Button(ablak, background='#ff0000', height=10, width=8)
    enemy3 = tkinter.Button(ablak, background='#ff0000', height=10, width=8)
    enemy1neve = tkinter.Label(ablak, text='enemy1', height=2, width=6, background='#ff0000')
    enemy2neve = tkinter.Label(ablak, text='enemy2', height=2, width=6, background='#ff0000')
    enemy3neve = tkinter.Label(ablak, text='enemy3', height=2, width=6, background='#ff0000')# rakosgasd majd bele pls


    gamecanvas.create_window(512, 250, window=enemy1)
    gamecanvas.create_window(312, 150, window=enemy2)
    gamecanvas.create_window(712, 150, window=enemy3)
    gamecanvas.create_window(512, 352, window=enemy1neve)
    gamecanvas.create_window(312, 252, window=enemy2neve)
    gamecanvas.create_window(712, 252, window=enemy3neve)
    gamecanvas.create_window(130, 715, window=item1)
    gamecanvas.create_window(386, 715, window=item2)
    gamecanvas.create_window(642, 715, window=item3)
    gamecanvas.create_window(898, 715, window=item4)
    gamecanvas.create_window(20, 20, window=backpackhossza)
    gamecanvas.create_window(972, 607, window=reroll)
    gamecanvas.create_window(60, 607, window=passgomb)
    gamecanvas.create_window(36, 536, window=trash)
    gamecanvas.create_window(970, 42, window=wavecounter)
    gamecanvas.create_window(99, 17, window=kilep)
    enemyspawn(enemies, enemy1, enemy2, enemy3, enemy1neve, enemy2neve, enemy3neve, 1)
    ablak.mainloop()
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
def enemyspawn(ebbol, egyik, masik, harmadik, egyikneve, masikneve, harmadikneve, currentlvl):
    mostanra = []
    for i in ebbol:
        if str(currentlvl) in i.appearsAt:
            mostanra.append(i)
    #kéne rajzolni
def kilepigen():
    sys.exit()