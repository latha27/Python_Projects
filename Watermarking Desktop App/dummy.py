import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

image = Image.open('hero-bg1.jpg')
tk_image = ImageTk.PhotoImage(image)

label = tk.Label(root, text='Some Plain Text', image=tk_image, compound='center')
label.pack()

root.mainloop()