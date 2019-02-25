from tkinter import *
import picture

root = Tk()
board = Canvas(root, width = 500, height = 500)
board.pack()
button1 = Button(root, width = 10, text="Picture", command = picture)
button1.pack()
#button1_window = board.create_window(10, 10, window = button1)
root.mainloop()
