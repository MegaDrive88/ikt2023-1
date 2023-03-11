import webbrowser
import tkinter
import sys
from PIL import Image, ImageTk
from events import *
import random
import time

def gamestart(bezar, enemies, items, save, ablak):
    time.sleep(1)
    enemyread(enemies)
    itemread(items)
    bezar.pack_forget()
    global gamecanvas
    bg = Image.open('hatter.jpg').resize((1050, 790))
    bbg = ImageTk.PhotoImage(bg)
    gamecanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#ff7500', relief='flat')
    gamecanvas.create_image(512, 395, image = bbg)
    gamecanvas.pack()
    level = 0
    global turn
    turn = 0
    item1 = tkinter.Button(ablak, height=5, width=22, font = ('Fette UNZ Fraktur', 13), relief='ridge' , background='#850505', foreground='#fcba03', activebackground="#fcba03", activeforeground="#850505", text='item1', name='1')
    item2 = tkinter.Button(ablak, height=5, width=22, font = ('Fette UNZ Fraktur', 13), relief='ridge' , background='#850505', foreground='#fcba03', activebackground="#fcba03", activeforeground="#850505", text='item2', name='2')
    item3 = tkinter.Button(ablak, height=5, width=22, font = ('Fette UNZ Fraktur', 13), relief='ridge' , background='#850505', foreground='#fcba03', activebackground="#fcba03", activeforeground="#850505", text='item3', name='3')
    item4 = tkinter.Button(ablak, height=5, width=22, font = ('Fette UNZ Fraktur', 13), relief='ridge' , background='#850505', foreground='#fcba03', activebackground="#fcba03", activeforeground="#850505", text='item4', name='4')
    rerollkep = ImageTk.PhotoImage(Image.open('rerollkep.png').resize((60, 60)))
    trashkep = ImageTk.PhotoImage(Image.open('trashcan.png').resize((60, 60)))
    reroll = tkinter.Button(ablak, height=80, width=100, background='#ffffff', text="", relief='flat', image=rerollkep, command= lambda: rerollbutton(items, level, item1, item2, item3, item4, potilabel, reroll))
    trash = tkinter.Button(ablak, height=80, width=100, background='#ffffff', text="", relief='flat', image=trashkep, command= lambda: trashbutton(potilabel, item1, item2, item3, item4, level, items)) 
    wavecounter = tkinter.Label(ablak, height=2, width=6, background='#ff7500', text=level, relief='flat', font=('Fette UNZ Fraktur', 25))
    kilep = tkinter.Button(ablak, height=2, width=5, background='#ff7500', text="Exit", relief='flat', command = lambda: backtotitlescreen(bezar, gamecanvas))
    enemy1neve = tkinter.Label(ablak, text='', height=2, background= '#ff7500')
    enemy2neve = tkinter.Label(ablak, text='', height=2, background= '#ff7500')
    enemy3neve = tkinter.Label(ablak, text='', height=2, background= '#ff7500')
    potilabel = tkinter.Label(ablak, text='', padx=0)
    bosslabel = tkinter.Label(ablak, text='', height=3, width = 17, background='#ffffff', foreground='#850505')
    bob = ImageTk.PhotoImage(Image.open('bob.png').resize((125, 225)))
    bobkep = enemy1 = gamecanvas.create_image(512, 505, image = bob)
    item1.bind("<Button-1>", lambda event: item1press(event, potilabel, items))
    item2.bind("<Button-1>", lambda event: item1press(event, potilabel, items))
    item3.bind("<Button-1>", lambda event: item1press(event, potilabel, items))
    item4.bind("<Button-1>", lambda event: item1press(event, potilabel, items))
    enemy1 = gamecanvas.create_image(512, 230, image = None)
    enemy2 = gamecanvas.create_image(312, 130, image = None)
    enemy3 = gamecanvas.create_image(712, 130, image = None)
    gamecanvas.tag_bind(enemy1, "<Button-1>", lambda event: itemuse(turn, enemy1neve, potilabel, bobhp, bobenergy, save, level, item1, item2, item3, item4, items))
    gamecanvas.tag_bind(enemy2, "<Button-1>", lambda event: itemuse(turn, enemy2neve, potilabel, bobhp, bobenergy, save, level, item1, item2, item3, item4, items))
    gamecanvas.tag_bind(enemy3, "<Button-1>", lambda event: itemuse(turn, enemy3neve, potilabel, bobhp, bobenergy, save, level, item1, item2, item3, item4, items))
    bobhp = tkinter.Label(ablak, text = 'Health-███████████████-150', foreground='#06b82f')
    bobenergy = tkinter.Label(ablak, text='Energy-████████████-120', foreground='#03b7f5')
    gamecanvas.create_window(512, 620, window=bobhp)
    gamecanvas.create_window(512, 640, window=bobenergy)
    gamecanvas.create_window(512, 352, window=enemy1neve)
    gamecanvas.create_window(312, 252, window=enemy2neve)
    gamecanvas.create_window(712, 252, window=enemy3neve)
    gamecanvas.create_window(130, 718, window=item1)
    gamecanvas.create_window(386, 718, window=item2)
    gamecanvas.create_window(642, 718, window=item3)
    gamecanvas.create_window(898, 718, window=item4)
    gamecanvas.create_window(972, 607, window=reroll)
    # gamecanvas.create_window(60, 607, window=passgomb)
    gamecanvas.create_window(55, 607, window=trash)
    gamecanvas.create_window(974, 45, window=wavecounter)
    gamecanvas.create_window(970, 120, window=bosslabel)
    gamecanvas.create_window(512, 400, window=potilabel)
    gamecanvas.create_window(20, 17, window=kilep)
    while level < 15:
        reroll["state"] = "normal"
        level += 1
        if int(bobenergy.cget('text').split('-')[2]) + 20>= 120:
            bobenergy.config(text = 'Energy-████████████-120')
        else:
            enbar = ''
            elozoen = int(bobenergy.cget('text').split('-')[2])
            for i in range(0, int(round((int(elozoen) + 20)/12, 0))):
                enbar += '█'
            bobenergy.config(text = f'Energy-{enbar}-{elozoen + 20}')
        wavecounter.config(text=level)
        itemgenerate(items, item1, item2, item3, item4, level)
        enemyspawn(gamecanvas, enemies, enemy1, enemy2, enemy3, enemy1neve, enemy2neve, enemy3neve, level)
        if level % 5 == 0:
            bosslabel.config(text='Boss')
            gamecanvas.itemconfig(enemy2, image = None)
            gamecanvas.itemconfig(enemy3, image = None)
        else:
            bosslabel.config(text='Weeklings')
        saveread(save, 'r')
        gamecanvas.update()
        while enemy1neve.cget('text') != 'Dead' or enemy2neve.cget('text') != 'Dead' or enemy3neve.cget('text') != 'Dead':
            if level % 5 == 0 and enemy1neve.cget('text') == 'Dead':
                break
            saveread(save, 'r')
            turn = int(save[-1].split(';')[2])
            if turn % 2 == 0:
                if str(level) == save[-1].split(';')[1]:
                    rest = f'{level};{turn};{"True" if save[-1].split(";")[2] == "True" else "False"};{save[-1].split(";")[4]}'
                    fajl = open('save.txt', 'w', encoding='utf-8')
                    fajl.write(f'{0};{rest}')
                    fajl.close()
                if bobenergy.cget('text').split('-')[2] == '0' or bobhp.cget('text').split('-')[2] == '0':
                    break
                vár(gamecanvas, 0.6)
            else:
                enemyturn(save, turn, enemy1neve, enemy2neve, enemy3neve, bobhp, enemies, level)
                pass
        if bobenergy.cget('text').split('-')[2] == '0' or bobhp.cget('text').split('-')[2] == '0' or (enemy1neve.cget('text') == 'Dead' and level >= 15):
            print('end')
            fajl = open('save.txt', 'w', encoding='utf-8')
            fajl.write(f'0;0;0;{"True" if enemy1neve.cget("text") == "Dead" and level >= 15 else "False"};{level if level >= int(save[-1].split(";")[-1]) else save[-1].split(";")[-1]}')
            fajl.close()
            gamecanvas.pack_forget()
            endcanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#230259', relief='flat')
            endcanvas.pack()
            endlabel = tkinter.Label(ablak, background='#230259', foreground='#850505', text = "You win!" if enemy1neve.cget("text") == "Dead" and level >= 15 else "Game over", font = ('Fette UNZ Fraktur', 50))
            kilepgomb = tkinter.Button(height = 1, width= 17, text='Back to title screen', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', activebackground="#850505", activeforeground="#fcba03", command = lambda: backtotitlescreen(bezar, endcanvas))
            endcanvas.create_window(512, 160, window = endlabel)
            endcanvas.create_window(512, 350, window = kilepgomb)
            break
    ablak.mainloop()

def backtotitlescreen(megnyit, bezar):
    megnyit.pack()
    bezar.pack_forget()

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
    potilabel.config(text = 'You have no more rerolls this round')
    gomb["state"] = "disabled"

def trashbutton(selected, item1, item2, item3, item4, lvl, osszes):
    lista = [item1, item2, item3, item4]
    melyiket = selected.cget('text').split('\n')[0]
    for c, i in enumerate(lista, 0):
        if i.cget('text') == melyiket:
            generateone(osszes, lista[c], lvl)
            break
    selected.config(text = '')
def itemuse(turn, clicked, selected, bhp, ben, save, lvl, item1, item2, item3, item4, osszes):
    items = [item1, item2, item3, item4]
    saveread(save, 'r')
    global mult
    mult = int(save[-1].split(';')[0])
    if turn % 2 == 0:
        enemy = clicked.cget("text").split(', ')
        try:
            mikettud = selected.cget('text').split(', ')[1].split(' ')
        except:
            selected.config(text = 'No item selected')
            return None
        if mikettud[0] ==  'Damage:':
            if clicked.cget('text') != 'Dead':
                clicked.config(text = f'{enemy[0]}, {round(int(float(enemy[-1]))-int(mikettud[1])*float(f"1.{mult}"), 0):.0f}')
                if int(float(clicked.cget("text").split(', ')[1])) <= 0:
                    clicked.config(text = 'Dead')
            enbar = ''
            minusz = int(selected.cget('text').split(', ')[0].split(':')[1])
            elozoen = ben.cget('text').split('-')[2]
            if elozoen != '-':
                for i in range(0, int(round((int(elozoen) - int(minusz))/10, 0))):
                    enbar += '█'
            if int(elozoen) - int(minusz) <= 0:
                ben.config(text = f'Energy-{enbar}-0')
            else:
                ben.config(text = f'Energy-{enbar}-{int(elozoen) - int(minusz)}')
            try:
                if mikettud[2] == '\nPerk:':
                    match mikettud[5]:
                        case 'Health:':
                            if int(bhp.cget('text').split('-')[2]) + int(mikettud[6]) >= 150:
                                bhp.config(text = 'Health-███████████████-150')
                            else:
                                hpbar = ''
                                elozohp = int(bhp.cget('text').split('-')[2])
                                for i in range(0, int(round((int(elozohp) + int(mikettud[6]))/15, 0))):
                                    hpbar += '█'
                                bhp.config(text = f'Health-{hpbar}-{elozohp + int(mikettud[6])}')
                        case 'Energy:':
                            if int(ben.cget('text').split('-')[2]) + int(mikettud[6]) >= 120:
                                ben.config(text = 'Energy-████████████-120')
                            else:
                                enbar = ''
                                elozoen = int(ben.cget('text').split('-')[2])
                                for i in range(0, int(round((int(elozoen) + int(mikettud[6]))/12, 0))):
                                    enbar += '█'
                                ben.config(text = f'Energy-{enbar}-{elozoen + int(mikettud[6])}')
                        case 'DMG:':
                            mult = int(mikettud[6])
                            rest = f'{turn};{"True" if save[-1].split(";")[2] == "True" else "False"};{save[-1].split(";")[4]}'
                            fajl = open('save.txt', 'w', encoding='utf-8')
                            fajl.write(f'{mult};{lvl+1};{rest}')
                            fajl.close()
                        case _:
                            print('something ain\'t right')
            except:
                pass
        for i in range(0, len(items)):
            if items[i].cget('text') == selected.cget('text').split('\n')[0]:
                generateone(osszes, items[i], lvl)
        selected.config(text = '')
        turn += 1
        saveread(save, 'r')
        fajl = open('save.txt', 'w', encoding='utf-8')
        rest =  [f'{save[-1].split(";")[0]};{save[-1].split(";")[1]}', f'{"True" if save[-1].split(";")[2] == "True" else "False"};{save[-1].split(";")[4]}']
        fajl.write(f'{rest[0]};{turn};{rest[1]}')
        fajl.close()

def generateone(ebbol, item1, lvl):
    ei = random.choice(ebbol)
    if ei.rese*5 - lvl*3 <= 7:
        ei = random.choice(ebbol)
        if ei.rese*5 - lvl*3 <= 12:
            ei = random.choice(ebbol)
            while ei.rese < lvl/3:
                ei = random.choice(ebbol)
    item1.config(text = ei.name)

def enemyturn(save, turn, e1n, e2n, e3n, bhp, osszes, lvl):
    if lvl % 5 != 0:
        enemyk = [e1n, e2n, e3n]
        ez = 10
        if turn % 2 != 0:
            melyik = random.randint(0, 2)
            for i in osszes:
                if enemyk[melyik].cget('text').split(', ')[0] == i.name:
                    ez = i.dam
                    break
            hpbar = ''
            time.sleep(1)
            elozohp = int(bhp.cget('text').split('-')[2])
            for i in range(0, int(round((int(elozohp) - int(ez))/15, 0))):
                hpbar += '█'
            bhp.config(text = f'Health-{hpbar}-{int(elozohp)-int(ez)}')
            turn = int(save[-1].split(";")[2])
            turn += 1
            fajl = open('save.txt', 'w', encoding='utf-8')
            rest =  [f'{save[-1].split(";")[0]};{save[-1].split(";")[1]}', f'{"True" if save[-1].split(";")[2] == "True" else "False"};{save[-1].split(";")[4]}']
            fajl.write(f'{rest[0]};{turn};{rest[1]}')
            fajl.close()
    else:
        ez = 15
        for i in osszes:
            if e1n.cget('text').split(', ')[0] == i.name:
                ez = i.dam
                break
        hpbar = ''
        time.sleep(1)
        elozohp = int(bhp.cget('text').split('-')[2])
        for i in range(0, int(round((int(elozohp) - int(ez))/15, 0))):
            hpbar += '█'
        bhp.config(text = f'Health-{hpbar}-{int(elozohp)-int(ez)}')
        turn = int(save[-1].split(";")[2])
        turn += 1
        fajl = open('save.txt', 'w', encoding='utf-8')
        rest =  [f'{save[-1].split(";")[0]};{save[-1].split(";")[1]}', f'{"True" if save[-1].split(";")[2] == "True" else "False"};{save[-1].split(";")[4]}']
        fajl.write(f'{rest[0]};{turn};{rest[1]}')
        fajl.close()
            
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
    listaa = [item1, item2, item3, item4]
    for i in range(0, 4):
        ei = random.choice(ebbol)
        if ei.rese*5 - lvl*3 <= 7:
            ei = random.choice(ebbol)
            if ei.rese*5 - lvl*3 <= 12:
                ei = random.choice(ebbol)
                while ei.rese < lvl/3:
                    ei = random.choice(ebbol)
        listaa[i].config(text = ei.name)
    x = []
    for i in listaa:
        if 'Potion' in i.cget('text'):
            x.append(i)
    if len(x) == 4:
        while 'Potion' in i.cget('text'):
            generateone(ebbol, x[0], lvl)

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
def vár(root, time):
        root.after(int(time*1000), root.quit)
        root.mainloop()

# Basic shield, def, 2, 5, 1
# Hardened round shield, def, 5, 10, 2
# Blessed shield, def, 5, 20, 2
# Thicc af shield, def, 8, 35, 4
# Basic armor, def, 2, 6, 1
# Blessed armor, def, 5, 40, 4
# Cursed armor, def, 10, 45, 6
# Basic helmet, def, 2, 5, 1