import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from score import score

window = tk.Tk()

window.title("Bowling Score")
window.geometry("525x150")
window.resizable(False, False)

frame_count = 1
                
f1score_var = tk.IntVar()
f2score_var = tk.IntVar()
f3score_var = tk.IntVar()
f4score_var = tk.IntVar()
f5score_var = tk.IntVar()
f6score_var = tk.IntVar()
f7score_var = tk.IntVar()
f8score_var = tk.IntVar()
f9score_var = tk.IntVar()
f10score_var = tk.IntVar()

f2disable = tk.DISABLED
f3disable = tk.DISABLED
f4disable = tk.DISABLED
f5disable = tk.DISABLED
f6disable = tk.DISABLED
f7disable = tk.DISABLED
f8disable = tk.DISABLED
f9disable = tk.DISABLED
f10disable = tk.DISABLED

def submit_frame():
    match frame_count:
        case 1:
            ball1 = f1b1.get()
            ball2 = f1b2.get()
            if not ball1.isdigit() or not ball2.isdigit():
                messagebox.showerror("Error", "Please enter valid numbers for balls 1 and 2.")
                return
            frame1_score = score(int(ball1), int(ball2), frame_count)
            f1score_var.set(frame1_score)
            f1b1['state'] = tk.DISABLED
            f1b2['state'] = tk.DISABLED
            f2disable = tk.NORMAL

score_button = tk.Button(window, 
                         text="Submit Frame", 
                         command=submit_frame,
                         bd=1, 
                         bg="blue",
                         fg="white",
                         font=("Arial", 12),
                         height=2,
                         justify="center",
                         overrelief="raised")
score_button.pack(side="bottom")

# frame 1
frame1 = ttk.Frame(window, relief="solid", borderwidth=1)
frame1.place(x=0, y=0, width=50, height=70)
frame1.columnconfigure((0,1), weight=1, uniform='a')
frame1.rowconfigure((0,1,2), weight=1)
label1 = ttk.Label(frame1, text="1", border=1, borderwidth=1).grid(row=0, column=0)
f1b1 = ttk.Entry(frame1, width=2)
f1b1.grid(row=1, column=0)
f1b2 = ttk.Entry(frame1, width=2)
f1b2.grid(row=1, column=1)
f1score = ttk.Label(frame1, textvariable=f1score_var).grid(row=2, column=1)

# frame 2
frame2 = ttk.Frame(window, relief="solid", borderwidth=1)
frame2.place(x=50, y=0, width=50, height=70)
frame2.columnconfigure((0,1), weight=1, uniform='a')
frame2.rowconfigure((0,1,2), weight=1)
label2 = ttk.Label(frame2, text="2").grid(row=0, column=0)
f2b1 = ttk.Entry(frame2, width=2)
f2b1.grid(row=1, column=0)
f2b2 = ttk.Entry(frame2, width=2)
f2b2.grid(row=1, column=1)
f2score = ttk.Label(frame2, textvariable=f2score_var).grid(row=2, column=1)

# frame 3
frame3 = ttk.Frame(window, relief="solid", borderwidth=1)
frame3.place(x=100, y=0, width=50, height=70)
frame3.columnconfigure((0,1), weight=1, uniform='a')
frame3.rowconfigure((0,1,2), weight=1)
label3 = ttk.Label(frame3, text="3").grid(row=0, column=0)
f3b1 = ttk.Entry(frame3, width=2)
f3b1.grid(row=1, column=0)
f3b2 = ttk.Entry(frame3, width=2)
f3b2.grid(row=1, column=1)
f3score = ttk.Label(frame3, textvariable=f3score_var).grid(row=2, column=1)

# frame 4
frame4 = ttk.Frame(window, relief="solid", borderwidth=1)
frame4.place(x=150, y=0, width=50, height=70)
frame4.columnconfigure((0,1), weight=1, uniform='a')
frame4.rowconfigure((0,1,2), weight=1)
label4 = ttk.Label(frame4, text="4").grid(row=0, column=0)
f4b1 = ttk.Entry(frame4, width=2)
f4b1.grid(row=1, column=0)
f4b2 = ttk.Entry(frame4, width=2)
f4b2.grid(row=1, column=1)
f4score = ttk.Label(frame4, textvariable=f4score_var).grid(row=2, column=1)

# frame 5
frame5 = ttk.Frame(window, relief="solid", borderwidth=1)
frame5.place(x=200, y=0, width=50, height=70)
frame5.columnconfigure((0,1), weight=1, uniform='a')
frame5.rowconfigure((0,1,2), weight=1)
label5 = ttk.Label(frame5, text="5").grid(row=0, column=0)
f5b1 = ttk.Entry(frame5, width=2)
f5b1.grid(row=1, column=0)
f5b2 = ttk.Entry(frame5, width=2)
f5b2.grid(row=1, column=1)
f5score = ttk.Label(frame5, textvariable=f5score_var).grid(row=2, column=1)

# frame 6
frame6 = ttk.Frame(window, relief="solid", borderwidth=1)
frame6.place(x=250, y=0, width=50, height=70)
frame6.columnconfigure((0,1), weight=1, uniform='a')
frame6.rowconfigure((0,1,2), weight=1)
label6 = ttk.Label(frame6, text="6").grid(row=0, column=0)
f6b1 = ttk.Entry(frame6, width=2)
f6b1.grid(row=1, column=0)
f6b2 = ttk.Entry(frame6, width=2)
f6b2.grid(row=1, column=1)
f6score = ttk.Label(frame6, textvariable=f6score_var).grid(row=2, column=1)

# frame 7
frame7 = ttk.Frame(window, relief="solid", borderwidth=1)
frame7.place(x=300, y=0, width=50, height=70)
frame7.columnconfigure((0,1), weight=1, uniform='a')
frame7.rowconfigure((0,1,2), weight=1)
label7 = ttk.Label(frame7, text="7").grid(row=0, column=0)
f7b1 = ttk.Entry(frame7, width=2)
f7b1.grid(row=1, column=0)
f7b2 = ttk.Entry(frame7, width=2)
f7b2.grid(row=1, column=1)
f7score = ttk.Label(frame7, textvariable=f7score_var).grid(row=2, column=1)

# frame 8
frame8 = ttk.Frame(window, relief="solid", borderwidth=1)
frame8.place(x=350, y=0, width=50, height=70)
frame8.columnconfigure((0,1), weight=1, uniform='a')
frame8.rowconfigure((0,1,2), weight=1)
label8 = ttk.Label(frame8, text="8").grid(row=0, column=0)
f8b1 = ttk.Entry(frame8, width=2)
f8b1.grid(row=1, column=0)
f8b2 = ttk.Entry(frame8, width=2)
f8b2.grid(row=1, column=1)
f8score = ttk.Label(frame8, textvariable=f8score_var).grid(row=2, column=1)

# frame 9
frame9 = ttk.Frame(window, relief="solid", borderwidth=1)
frame9.place(x=400, y=0, width=50, height=70)
frame9.columnconfigure((0,1), weight=1, uniform='a')
frame9.rowconfigure((0,1,2), weight=1)
label9 = ttk.Label(frame9, text="9").grid(row=0, column=0)
f9b1 = ttk.Entry(frame9, width=2)
f9b1.grid(row=1, column=0)
f9b2 = ttk.Entry(frame9, width=2)
f9b2.grid(row=1, column=1)
f9score = ttk.Label(frame9, textvariable=f9score_var).grid(row=2, column=1)

# frame 10
frame10 = ttk.Frame(window, relief="solid", borderwidth=1)
frame10.place(x=450, y=0, width=75, height=70)
frame10.columnconfigure((0,1,2), weight=1, uniform='a')
frame10.rowconfigure((0,1,2), weight=1)
label10 = ttk.Label(frame10, text="10").grid(row=0, column=0)
f10b1 = ttk.Entry(frame10, width=2)
f10b1.grid(row=1, column=0)
f10b2 = ttk.Entry(frame10, width=2)
f10b2.grid(row=1, column=1)
f10b3 = ttk.Entry(frame10, width=2)
f10b3.grid(row=1, column=2)
f10score = ttk.Label(frame10, textvariable=f10score_var).grid(row=2, column=2)



window.mainloop()