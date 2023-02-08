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
    #invread(inventory, 'a')
    bezar.pack_forget()
    global gamecanvas
    bg = Image.open('hatter.jpg').resize((1050, 790))
    bbg = ImageTk.PhotoImage(bg)
    gamecanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#ff7500', relief='flat') # 230259
    gamecanvas.create_image(512, 395, image = bbg)
    gamecanvas.pack()
    level = 1
    turn = 0
    item1 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item1', name='1')
    item2 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item2', name='2')
    item3 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item3', name='3')
    item4 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item4', name='4')
    # backpackhossza = tkinter.Label(ablak, height=2, width=5, text=len(inventory), background='#ffffff')
    rk = Image.open('rerollkep.png').resize((60, 60))
    rerollkep = ImageTk.PhotoImage(rk)
    reroll = tkinter.Button(ablak, height=80, width=100, background='#ffffff', text="__", relief='flat', image=rerollkep, command= lambda: rerollbutton(items, level, item1, item2, item3, item4, potilabel, reroll))
    passgomb = tkinter.Button(ablak, height=5, width=15, background='#ffffff', text="valamikep", relief='flat')#, command=valamibutton)    , highlightbackground = "#000000", highlightthickness=1, bd = 0
    trash = tkinter.Button(ablak, height=3, width=8, background='#ffffff', text="trashkep", relief='flat')#, command=trashbutton) 
    wavecounter = tkinter.Label(ablak, height=2, width=6, background='#ff7500', text=level, relief='flat', font=('Fette UNZ Fraktur', 25))
    kilep = tkinter.Button(ablak, height=2, width=5, background='#ffffff', text="Exit", relief='flat')#, command=biztoshkilepszV2)
    enemy1 = tkinter.Button(ablak, background='#ff7500', height=200, width=120, relief='flat', activebackground="#ff7500")
    enemy2 = tkinter.Button(ablak, background='#ff7500', height=200, width=120, relief='flat', activebackground="#ff7500")
    enemy3 = tkinter.Button(ablak, background='#ff7500', height=200, width=120, relief='flat', activebackground="#ff7500")
    enemy1neve = tkinter.Label(ablak, text='', height=2, background= '#ff7500')
    enemy2neve = tkinter.Label(ablak, text='', height=2, background= '#ff7500')
    enemy3neve = tkinter.Label(ablak, text='', height=2, background= '#ff7500')
    potilabel = tkinter.Label(ablak, text='', padx=0)
    bosslabel = tkinter.Label(ablak, text='', height=5, width = 17, background='#ffffff')
    boblabel = tkinter.Label(ablak, background='#ffffff', height=10, width=8, relief='flat')
    item1.bind("<Button-1>", lambda event: item1press(event, potilabel, items))
    item2.bind("<Button-1>", lambda event: item1press(event, potilabel, items))
    item3.bind("<Button-1>", lambda event: item1press(event, potilabel, items))
    item4.bind("<Button-1>", lambda event: item1press(event, potilabel, items))

    gamecanvas.create_window(512, 230, window=enemy1)
    gamecanvas.create_window(312, 130, window=enemy2)
    gamecanvas.create_window(712, 130, window=enemy3)
    gamecanvas.create_window(512, 535, window=boblabel)
    gamecanvas.create_window(512, 352, window=enemy1neve)
    gamecanvas.create_window(312, 252, window=enemy2neve)
    gamecanvas.create_window(712, 252, window=enemy3neve)
    gamecanvas.create_window(130, 715, window=item1)
    gamecanvas.create_window(386, 715, window=item2)
    gamecanvas.create_window(642, 715, window=item3)
    gamecanvas.create_window(898, 715, window=item4)
    #gamecanvas.create_window(20, 20, window=backpackhossza)
    gamecanvas.create_window(972, 607, window=reroll)
    gamecanvas.create_window(60, 607, window=passgomb)
    gamecanvas.create_window(36, 536, window=trash)
    gamecanvas.create_window(974, 45, window=wavecounter)
    gamecanvas.create_window(970, 127, window=bosslabel)
    if level % 5 == 0:
        bosslabel.config(text='Boss')
    else:
        bosslabel.config(text='')
    gamecanvas.create_window(512, 390, window=potilabel)
    gamecanvas.create_window(20, 17, window=kilep)
    enemyspawn(enemies, enemy1, enemy2, enemy3, enemy1neve, enemy2neve, enemy3neve, level)
    itemgenerate(items, item1, item2, item3, item4, level)
    # while level < 16:
    
    ablak.mainloop()
def segitseg():
    webbrowser.open_new(r"help.html")

def rerollbutton(ebbol, lvl, item1, item2, item3, item4, potilabel, gomb):
    listaa = []
    listaa.append(item1)
    listaa.append(item2)
    listaa.append(item3)
    listaa.append(item4)
    for i in range(0, 4):
        ei = random.choice(ebbol)
        if ei.rese*5 - lvl*3 <= 7:
            ei = random.choice(ebbol)
            if ei.rese*5 - lvl*3 <= 12:
                ei = random.choice(ebbol) 
                while ei.rese < lvl/3:
                    ei = random.choice(ebbol) 
        listaa[i].config(text = ei.name)
    potilabel.config(text = 'You have n rerolls in this round')
    gomb["state"] = "disabled"


#def valamibutton():


#def trashbutton():


#def wavecounter():

# def enemyTakingDamage():
#     enemyHealth = Enemy.hp
#     activeItem = 
#     if Item.type == 'mag':
#         enemyHealth -= Item.damage




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
def enemyspawn(ebbol, egyik, masik, harmadik, egyikneve, masikneve, harmadikneve, currentlvl):
    mostanra = []
    for i in ebbol:
        if str(currentlvl) in i.appearsAt:
            mostanra.append(i)
    if currentlvl % 5 != 0:
        gamecanvas.create_window(312, 130, window=masik)
        gamecanvas.create_window(712, 130, window=harmadik)
        ec = random.choice(mostanra)
        egyikneve.config(text = f'{ec.name}, {ec.hp}')
        ek = Image.open(f'enemies/{ec.name}.png').resize((100, 200))
        global ekk
        ekk = ImageTk.PhotoImage(ek) 
        egyik.config(image = ekk)
        ec = random.choice(mostanra)
        masikneve.config(text = f'{ec.name}, {ec.hp}')
        mk = Image.open(f'enemies/{ec.name}.png').resize((100, 200))
        global mkk
        mkk = ImageTk.PhotoImage(mk) 
        masik.config(image = mkk)
        ec = random.choice(mostanra)
        harmadikneve.config(text = f'{ec.name}, {ec.hp}')
        hk = Image.open(f'enemies/{ec.name}.png').resize((100, 200))
        global hkk
        hkk = ImageTk.PhotoImage(hk) 
        harmadik.config(image = hkk)
        masik.config(width = 120, height = 200)
        harmadik.config(width = 120, height = 200)
    else:
        ec = random.choice(mostanra)
        egyikneve.config(text = f'{ec.name}, {ec.hp}')
        bk = Image.open(f'enemies/{ec.name}.png')
        global bkk
        bkk = ImageTk.PhotoImage(bk) 
        egyik.config(image = bkk)
        masik.pack_forget()
        harmadik.pack_forget()
        masik.config(width = 0, height = 0)
        harmadik.config(width = 0, height = 0)
    # egyik. ---kép
def itemgenerate(ebbol, item1, item2, item3, item4, lvl):
    listaa = []
    listaa.append(item1)
    listaa.append(item2)
    listaa.append(item3)
    listaa.append(item4)
    # var_holder = {}
    # for i in range(5):
    #     var_holder['item' + str(i)] = "iterationNumber=="+str(i)
    # locals().update(var_holder) 
    for i in range(0, 4):
        ei = random.choice(ebbol)
        if ei.rese*5 - lvl*3 <= 7:
            ei = random.choice(ebbol)
            if ei.rese*5 - lvl*3 <= 12:
                ei = random.choice(ebbol)
                while ei.rese < lvl/3:
                    ei = random.choice(ebbol)
        listaa[i].config(text = ei.name)
    pass
# commandok egyesével
# global valasztott
# valasztott = 'a'
def item1press(event, potilabel, ebbol):
    valasztott = event.widget.cget("text")
    neve = str(event.widget).split(".")[-1]
    mittud = ''
    for i in ebbol:
        if i.name == valasztott:
            if i.type == ' atk':
                mittud = f'{valasztott}\nMana cost: {i.energy}, Damage: {i.damage}'
            elif i.type == ' def':
                mittud = f'{valasztott}\nMana cost: {i.energy}, Defense: {i.defense}'
            elif i.type == ' mag':
                mittud = f'{valasztott}\nMana cost: {i.energy}, Damage: {i.damage}\nPerk: {i.perk}, {i.perkValue}'
    potilabel.config(text = mittud)
    return valasztott, neve

# def flipper(event):
#     print("label text:", event.widget.cget("text"))
# def flipper(event):
#     print("widget name:", str(event.widget).split(".")[-1])
def selectitem(potilabel): #ebbol, item1, item2, item3, item4, 
    pass