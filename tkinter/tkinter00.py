"""Hello World application for Tkinter"""

from tkinter import *
tk = Tk()
frame = Frame(tk, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
label = Label(frame, text="Button Example")
label.pack(fill=X, expand=1)

button = Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
