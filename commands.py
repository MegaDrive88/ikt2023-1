import webbrowser
import tkinter
import sys
from PIL import Image, ImageTk
from events import *
import random
import time
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
    level = 0
    global turn
    turn = 0
    item1 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item1', name='1')
    item2 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item2', name='2')
    item3 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item3', name='3')
    item4 = tkinter.Button(ablak, height=8, width=35, relief='ridge', background= '#ffffff', text='item4', name='4')
    rerollkep = ImageTk.PhotoImage(Image.open('rerollkep.png').resize((60, 60)))
    trashkep = None # ide majd a trashképet
    reroll = tkinter.Button(ablak, height=80, width=100, background='#ffffff', text="__", relief='flat', image=rerollkep, command= lambda: rerollbutton(items, level, item1, item2, item3, item4, potilabel, reroll))
    passgomb = tkinter.Button(ablak, height=5, width=15, background='#ffffff', text="valamikep", relief='flat')#, command=valamibutton)    , highlightbackground = "#000000", highlightthickness=1, bd = 0
    trash = tkinter.Button(ablak, height=3, width=8, background='#ffffff', text="trashkep", relief='flat', command= lambda: trashbutton(potilabel, item1, item2, item3, item4, trash)) 
    wavecounter = tkinter.Label(ablak, height=2, width=6, background='#ff7500', text=level, relief='flat', font=('Fette UNZ Fraktur', 25))
    kilep = tkinter.Button(ablak, height=2, width=5, background='#ffffff', text="Exit", relief='flat', command = sys.exit)#, command=biztoshkilepszV2)
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
    enemy1 = gamecanvas.create_image(512, 230, image = None)
    enemy2 = gamecanvas.create_image(312, 130, image = None)
    enemy3 = gamecanvas.create_image(712, 130, image = None)
    gamecanvas.tag_bind(enemy1, "<Button-1>", lambda event: itemuse(turn, enemy1neve, potilabel))
    gamecanvas.tag_bind(enemy2, "<Button-1>", lambda event: itemuse(turn, enemy2neve, potilabel))
    gamecanvas.tag_bind(enemy3, "<Button-1>", lambda event: itemuse(turn, enemy3neve, potilabel))
    bobhp = tkinter.Label(ablak, text = 'Health-████████████-120', foreground='#06b82f')
    bobenergy = tkinter.Label(ablak, text='Energy-██████████-100', foreground='#03b7f5')
    gamecanvas.create_window(512, 618, window=bobhp)
    gamecanvas.create_window(512, 638, window=bobenergy)
    gamecanvas.create_window(512, 530, window=boblabel)
    gamecanvas.create_window(512, 352, window=enemy1neve)
    gamecanvas.create_window(312, 252, window=enemy2neve)
    gamecanvas.create_window(712, 252, window=enemy3neve)
    gamecanvas.create_window(130, 715, window=item1)
    gamecanvas.create_window(386, 715, window=item2)
    gamecanvas.create_window(642, 715, window=item3)
    gamecanvas.create_window(898, 715, window=item4)
    gamecanvas.create_window(972, 607, window=reroll)
    gamecanvas.create_window(60, 607, window=passgomb)
    gamecanvas.create_window(36, 536, window=trash)
    gamecanvas.create_window(974, 45, window=wavecounter)
    gamecanvas.create_window(970, 127, window=bosslabel)
    gamecanvas.create_window(512, 400, window=potilabel)
    gamecanvas.create_window(20, 17, window=kilep)
    # while level < 15:
    reroll["state"] = "normal"
    level += 1
    wavecounter.config(text=level)
    itemgenerate(items, item1, item2, item3, item4, level)
    enemyspawn(gamecanvas, enemies, enemy1, enemy2, enemy3, enemy1neve, enemy2neve, enemy3neve, level)
        # if level % 5 == 0:
        #     bosslabel.config(text='Boss')
        #     gamecanvas.itemconfig(enemy2, image = None)
        #     gamecanvas.itemconfig(enemy3, image = None)
        # elif level % 5 != 0:
        #     bosslabel.config(text='')
        # gamecanvas.update()
        # time.sleep(2)
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
    potilabel.config(text = 'You have no rerolls this round')
    gomb["state"] = "disabled"
def valamibutton(turn):
    turn += 1
def trashbutton(selected, item1, item2, item3, item4, gomb):
    pass

def itemuse(turn, clicked, selected):
    if turn % 2 == 0:
        enemy = clicked.cget("text").split(', ')
        try:
            mikettud = selected.cget('text').split(', ')[1].split(' ')
        except:
            selected.config(text = 'No item selected')
            return None
        if mikettud[0] ==  'Damage:':
            clicked.config(text = f'{enemy[0]}, {int((enemy[1]))-int(mikettud[1])}')
            try:
                if mikettud[2] == '\nPerk:':
                    match mikettud[5]:
                        case 'Health:':
                            print('hp')
                        case 'Energy:':
                            print('energy')
                        case 'DMG:':
                            print('dmg')
                        case 'Shield:':
                            print('shield')
                        case _:
                            print('something ain\'t right')
            except:
                pass
                #ilyenkor fix nincs perk
            #van perk? ha van, akkor x, else y
            #kéne egy olyan függvény ami csak egy itemet generál, de azt megoldom
        else:
            pass
            #defenzív item, emiatt lehet kellenek még argumentek

def generateone(ebbol, item1, lvl): # , item2, item3, item4,
    ei = random.choice(ebbol)
    if ei.rese*5 - lvl*3 <= 7:
        ei = random.choice(ebbol)
        if ei.rese*5 - lvl*3 <= 12:
            ei = random.choice(ebbol)
            while ei.rese < lvl/3:
                ei = random.choice(ebbol)
    item1.config(text = ei.name)
def enemyturn(turn, e1n, e2n, e3n, hp):
    if turn % 2 != 0:
        pass
def kilepigen():
    sys.exit()
def enemyspawn(ablak, ebbol, egyik, masik, harmadik, egyikneve, masikneve, harmadikneve, currentlvl):
    mostanra = []
    for i in ebbol:
        if str(currentlvl) in i.appearsAt:
            mostanra.append(i)
    if currentlvl % 5 != 0:
        ec = random.choice(mostanra)
        egyikneve.config(text = f'{ec.name}, {ec.hp}')
        global ekk
        ekk = ImageTk.PhotoImage(Image.open(f'enemies/{ec.name}.png').resize((100, 200))) 
        ablak.itemconfig(egyik, image = ekk)
        ec = random.choice(mostanra)
        masikneve.config(text = f'{ec.name}, {ec.hp}')
        global mkk
        mkk = ImageTk.PhotoImage(Image.open(f'enemies/{ec.name}.png').resize((100, 200))) 
        ablak.itemconfig(masik, image = mkk)
        harmadikneve.config(text = f'{ec.name}, {ec.hp}')
        global hkk
        hkk = ImageTk.PhotoImage(Image.open(f'enemies/{ec.name}.png').resize((100, 200))) 
        ablak.itemconfig(harmadik, image = hkk)
    else:
        ec = random.choice(mostanra)
        egyikneve.config(text = f'{ec.name}, {ec.hp}')
        masikneve.config(text = '')
        harmadikneve.config(text = '')
        global bkk
        bkk = ImageTk.PhotoImage(Image.open(f'enemies/{ec.name}.png').resize((100, 200)))
        ablak.itemconfig(egyik, image = bkk)
        ures = ImageTk.PhotoImage(Image.open(f'enemies/ures.png').resize((100, 200)))
        ablak.itemconfig(masik, image = ures)
        ablak.itemconfig(harmadik, image = ures)
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
                mittud = f'{valasztott}\nMana cost: {i.energy}, Damage: {i.damage} \nPerk: {i.perk}: {i.perkValue}'
    potilabel.config(text = mittud)
    return valasztott, neve
#after