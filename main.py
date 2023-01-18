import tkinter
import sys
from commands import *
# import customtkinter
ablak = tkinter.Tk()
ablak.title('Bob\'s trip in HELL')
focanvas = tkinter.Canvas(ablak, height = 800, width = 1024, background= '#ffffff')
cim = tkinter.Label(ablak, text = 'Bob\'s trip in', font = ('Fette UNZ Fraktur', 50), foreground = '#850505').pack()
ci2 = tkinter.Label(ablak, text = 'hell', font = ('Fette UNZ Fraktur', 80), foreground = '#850505').pack()
startgomb = tkinter.Button(text='Start game', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#f0ab0a', foreground='#850505', command = gamestart).pack()

exitgomb = tkinter.Button(text='Exit', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#f0ab0a', foreground='#850505').pack() # command = u sure?

# teszt = tkinter.Button(text='anyád', relief='raise').pack()

cimcanvas = focanvas.create_window(480, 120)
cimcanvas = focanvas.create_window(520, 120)
focanvas.pack()


ablak.mainloop()

# pip install pillow
# pip install customtkinter
# startgame nagyobb ablak