import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Bowling Score")
window.geometry("500x150")
window.resizable(False, False)

# frame 1
frame1 = ttk.Frame(window, relief="solid", borderwidth=1)
frame1.place(x=0, y=0, width=50, height=70)
frame1.columnconfigure((0,1), weight=1, uniform='a')
frame1.rowconfigure((0,1,2), weight=1)
label1 = ttk.Label(frame1, text="1")
label1.grid(row=0, column=0)
f1b1 = ttk.Entry(frame1, width=2)
f1b1.grid(row=1, column=0)
f1b2 = ttk.Entry(frame1, width=2)
f1b2.grid(row=1, column=1)
f1score = ttk.Label(frame1, text="0")
f1score.grid(row=2, column=1)

# # frame 2
# ttk.Label(window, text="2").grid(row=2, column=2, columnspan=2)
# f2b1 = ttk.Entry(window, width=2)
# f2b1.grid(row=3, column=2)
# f2b2 = ttk.Entry(window, width=2)
# f2b2.grid(row=3, column=3)

# # frame 3
# ttk.Label(window, text="3").grid(row=2, column=4, columnspan=2)
# f3b1 = ttk.Entry(window, width=2)
# f3b1.grid(row=3, column=4)
# f3b2 = ttk.Entry(window, width=2)
# f3b2.grid(row=3, column=5)

# # frame 4
# ttk.Label(window, text="4").grid(row=2, column=6, columnspan=2)
# f4b1 = ttk.Entry(window, width=2)
# f4b1.grid(row=3, column=6)
# f4b2 = ttk.Entry(window, width=2)
# f4b2.grid(row=3, column=7)

# # frame 5
# ttk.Label(window, text="5").grid(row=2, column=8, columnspan=2)
# f5b1 = ttk.Entry(window, width=2)
# f5b1.grid(row=3, column=8)
# f5b2 = ttk.Entry(window, width=2)
# f5b2.grid(row=3, column=9)

# # frame 6
# ttk.Label(window, text="6").grid(row=2, column=10, columnspan=2)
# f6b1 = ttk.Entry(window, width=2)
# f6b1.grid(row=3, column=10)
# f6b2 = ttk.Entry(window, width=2)
# f6b2.grid(row=3, column=11)

# # frame 7
# ttk.Label(window, text="7").grid(row=2, column=12, columnspan=2)
# f7b1 = ttk.Entry(window, width=2)
# f7b1.grid(row=3, column=12)
# f7b2 = ttk.Entry(window, width=2)
# f7b2.grid(row=3, column=13)

# # frame 8
# ttk.Label(window, text="8").grid(row=2, column=14, columnspan=2)
# f8b1 = ttk.Entry(window, width=2)
# f8b1.grid(row=3, column=14)
# f8b2 = ttk.Entry(window, width=2)
# f8b2.grid(row=3, column=15)

# # frame 9
# ttk.Label(window, text="9").grid(row=2, column=16, columnspan=2)
# f9b1 = ttk.Entry(window, width=2)
# f9b1.grid(row=3, column=16)
# f9b2 = ttk.Entry(window, width=2)
# f9b2.grid(row=3, column=17)

# # frame 10
# ttk.Label(window, text="10").grid(row=2, column=18, columnspan=3)
# f2b1 = ttk.Entry(window, width=2)
# f2b1.grid(row=3, column=18)
# f2b2 = ttk.Entry(window, width=2)
# f2b2.grid(row=3, column=19)
# f10b3 = ttk.Entry(window, width=2)
# f10b3.grid(row=3, column=20)

window.mainloop()