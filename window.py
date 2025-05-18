import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("Bowling Score")
window.geometry("800x400")
window.resizable(False, False)

frame1_var=tk.IntVar()

# frame 1
Label(window, text="1").grid(row=0, columnspan=2)
f1b1 = Entry(window, width=2)
f1b1.grid(row=1, column=0)
f1b2 = Entry(window, width=2)
f1b2.grid(row=1, column=1)


# frame 2
Label(window, text="2").grid(row=0, column=2, columnspan=2)
f2b1 = Entry(window, width=2)
f2b1.grid(row=1, column=2)
f2b2 = Entry(window, width=2)
f2b2.grid(row=1, column=3)

mainloop()