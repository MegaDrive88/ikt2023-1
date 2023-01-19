import tkinter
from commands import *
from PIL import Image, ImageTk
import classes
import events
# import customtkinter
enemies = []
allitems = []
inventory = []
save = []
ablak = tkinter.Tk()
ablak.configure(bg='#ffffff')
ablak.resizable(width=False, height=False)
ablak.title('Bob\'s trip in HELL')
focanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#ffffff', relief='flat') # 230259
def biztoshkilepszV2():
    focanvas.pack_forget()
    global subc
    subc = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#ffffff', relief='flat')
    ablak.title("Exit")
    cim3 = tkinter.Label(ablak, text = 'Are you sure?', font = ('Fette UNZ Fraktur', 40), foreground = '#850505', background='#ffffff')
    igengomb = tkinter.Button(ablak, height = 1, width= 5, text='Yes', font = ('Fette UNZ Fraktur', 25), relief='ridge' , background='#fcba03', foreground='#850505', activebackground="#850505", activeforeground="#fcba03", command=kilepigen)
    nemgomb = tkinter.Button(ablak, height = 1, width= 5, text='No', font = ('Fette UNZ Fraktur', 25), relief='ridge' , background='#fcba03', foreground='#850505', activebackground="#850505", activeforeground="#fcba03", command=kilepnem)

    subc.create_window(512, 110, window = cim3)
    subc.create_window(341, 250, window = igengomb)
    subc.create_window(683, 250, window = nemgomb)
    subc.pack()
def kilepnem():
    focanvas.pack()
    subc.pack_forget()
    ablak.title('Bob\'s trip in HELL')
gamecanvas = tkinter.Canvas(ablak, height = 780, width = 1024, background= '#ffffff', relief='flat')
cim = tkinter.Label(ablak, text = 'Bob\'s trip in', font = ('Fette UNZ Fraktur', 50), foreground = '#850505', background='#ffffff')
cim2 = tkinter.Label(ablak, text = 'hell', font = ('Fette UNZ Fraktur', 80), foreground = '#850505', background='#ffffff')
startgomb = tkinter.Button(height = 1, width= 12, text='Start game', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', activebackground="#850505", activeforeground="#fcba03", command = lambda: gamestart(focanvas, gamecanvas, enemies, allitems, inventory, save))
helpgomb = tkinter.Button(height = 1, width= 12, text='Help', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', activebackground="#850505", activeforeground="#fcba03", command = segitseg)
exitgomb = tkinter.Button(height = 1, width= 12, text='Exit', font = ('Fette UNZ Fraktur', 20), relief='ridge' , background='#fcba03', foreground='#850505', activebackground="#850505", activeforeground="#fcba03", command = biztoshkilepszV2)

tuzkep = Image.open('tuz2.png')
test = ImageTk.PhotoImage(tuzkep)
keplabel = tkinter.Label(image=test, background='#ffffff')
focanvas.create_window(512, 630, window = keplabel)

focanvas.create_window(400, 120, window = cim)
focanvas.create_window(700, 130, window = cim2)
focanvas.create_window(512, 290, window = startgomb)
focanvas.create_window(512, 360, window = helpgomb)
focanvas.create_window(512, 430, window = exitgomb)
#RAJZOLÁS
# def get_x_and_y(event):
#     global lasx, lasy
#     lasx, lasy = event.x, event.y

# def draw_smth(event):
#     global lasx, lasy
#     focanvas.create_line((lasx, lasy, event.x, event.y), 
#                       fill='red', 
#                       width=5)
#     lasx, lasy = event.x, event.y
# focanvas.bind("<Button-1>", get_x_and_y)
# focanvas.bind("<B1-Motion>", draw_smth)
# tag_lower()

focanvas.pack()

ablak.mainloop()

# pip install pillow
# pip install customtkinter
# startgame nagyobb ablak
