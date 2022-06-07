from tkinter import *
from time import strftime

def time():
    str=strftime("%I : %M : %S %p")
    label.config(text=str)
    label.after(1000,time)

gui=Tk()
gui.title("Digital Clock")
gui.resizable(0,0)
gui.configure(bg='#000000')

window_height = 300
window_width = 800

screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

gui.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

label=Label(gui,font=("ds-digital",70),background="#000000",foreground="#00ff66")
label.place(relx=0.5, rely=0.5, anchor=CENTER)

time()
mainloop()