from tkinter import *
#import tkinter as tk
#from PIL import ImageTk,Image

root = Tk()
canvas = Canvas(root, bg="black", width = 1000, height = 800)
canvas.pack()
#img = PIL.ImageTK.PhotoImage(Image.open("lightning.jpeg"))
#img = tkinter.PhotoImage(file="lightning.jpeg")
img = PhotoImage(file="squirrel.gif")
canvas.create_image(500,400, image=img)
exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.pack()
root.mainloop()

