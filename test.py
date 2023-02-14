from tkinter import *
app = Tk()
def which_button(button_press):
    print(button_press)
b1 = Button(app, text="Apple",
            command=lambda m="It is an apple": which_button(m))
b1.grid(padx=10, pady=10)
b2 = Button(app, text="Banana",
            command=lambda m="It is a banana": which_button(m))
b2.grid(padx=10, pady=10)
app.mainloop()
# self.image_id = self.canvas.create_image(...)
# ...
# self.canvas.delete(self.image_id)