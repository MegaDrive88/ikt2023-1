import tkinter
import sys
from commands import *
from PIL import Image, ImageTk
# import customtkinter
ablak = tkinter.Tk()
ablak.configure(bg='#ffffff')
ablak.resizable(width=False, height=False)
ablak.title('Bob\'s trip in HELL')
focanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#ffffff', relief='flat') # 230259
cim = tkinter.Label(ablak, text = 'Bob\'s trip in', font = ('Fette UNZ Fraktur', 50), foreground = '#850505', background='#ffffff')
cim2 = tkinter.Label(ablak, text = 'hell', font = ('Fette UNZ Fraktur', 80), foreground = '#850505', background='#ffffff')
startgomb = tkinter.Button(height = 1, width= 12, text='Start game', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', command = gamestart)
helpgomb = tkinter.Button(height = 1, width= 12, text='Help', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', command = segitseg)
exitgomb = tkinter.Button(height = 1, width= 12, text='Exit', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', command = biztoshkilepsz)# command = u sure?
tuzkep = Image.open('tuz2.png')
test = ImageTk.PhotoImage(tuzkep)
keplabel = tkinter.Label(image=test, background='#ffffff')

# teszt = tkinter.Button(text='anyád', relief='raise').pack()

cimcanvas = focanvas.create_window(400, 120, window = cim)
cimcanvas2 = focanvas.create_window(700, 130, window = cim2)
startcanv = focanvas.create_window(512, 280, window = startgomb)
helpcanv = focanvas.create_window(512, 350, window = helpgomb)
exitcanv = focanvas.create_window(512, 420, window = exitgomb)
kepcanv = focanvas.create_window(512, 630, window = keplabel)
# focanvas.tag_lower(kepcanv, exitcanv)


focanvas.pack()

ablak.mainloop()

# pip install pillow
# pip install customtkinter
# startgame nagyobb ablak