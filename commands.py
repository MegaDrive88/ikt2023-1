import webbrowser
import tkinter

def gamestart():
    pass
def segitseg():
    webbrowser.open_new(r"help.html")
def biztoshkilepsz():
    ablak = tkinter.Tk()
    ablak.configure(bg='#ffffff')
    # ablak.resizable(width=False, height=False)
    ablak.title("Exit")
    focanvas = tkinter.Canvas(ablak, height = 1000, width = 1000, background= '#ffffff', relief='flat')
    cim = tkinter.Label(ablak, text = 'Are you sure?', font = ('Fette UNZ Fraktur', 15), foreground = '#850505', background='#ffffff')
    igengomb = tkinter.Button(height = 1, width= 3, text='Yes', font = ('Fette UNZ Fraktur', 5), relief='ridge' , background='#fcba03', foreground='#850505')
    nemgomb = tkinter.Button(height = 1, width= 3, text='No', font = ('Fette UNZ Fraktur', 5), relief='ridge' , background='#fcba03', foreground='#850505')

    cimcanvas = focanvas.create_window(250, 100, window = cim)
    igencanv = focanvas.create_window(50, 200, window = igengomb)
    nemcanv = focanvas.create_window(200, 200, window = nemgomb)

    focanvas.pack()

    ablak.mainloop()