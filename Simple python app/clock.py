import time
from tkinter import *

def tick():
    time1 = time.strftime('%H:%M:%S')
    board.itemconfig(clock, text=time1)
    board.after(1000, tick)
    
root = Tk()
board = Canvas(root, width = 500, height = 500)
board.pack()
clock = board.create_text(250,250, font=("times", 40, "bold"))
tick()
exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.pack()
root.mainloop()

