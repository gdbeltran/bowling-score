import tkinter as tk
from tkinter import ttk, messagebox

def clear_variables():
    f1b1_var.set(0)
    f1b2_var.set(0)
    f2b1_var.set(0)
    f2b2_var.set(0)
    f3b1_var.set(0)
    f3b2_var.set(0)
    f4b1_var.set(0)
    f4b2_var.set(0)
    f5b1_var.set(0)
    f5b2_var.set(0)
    f6b1_var.set(0)
    f6b2_var.set(0)
    f7b1_var.set(0)
    f7b2_var.set(0)
    f8b1_var.set(0)
    f8b2_var.set(0)
    f9b1_var.set(0)
    f9b2_var.set(0)
    f10b1_var.set(0)
    f10b2_var.set(0)
    f10b3_var.set(0)
    f1score_var.set(0)
    f2score_var.set(0)
    f3score_var.set(0)
    f4score_var.set(0)
    f5score_var.set(0)
    f6score_var.set(0)
    f7score_var.set(0)
    f8score_var.set(0)
    f9score_var.set(0)
    f10score_var.set(0)

def save_game():
    if frame_number == 10:
        game1 = game1_var.get()
        game2 = game2_var.get()
        game3 = game3_var.get()
        if game1 == 0:
            game1_var.set(f10score_var.get())
            clear_variables()
        elif game2 == 0:
            game2_var.set(f10score_var.get())
            clear_variables()
        elif game3 == 0:
            game3_var.set(f10score_var.get())
            game3 = f10score_var.get()
            series_var.set(game1 + game2 + game3)
            
    else:
        messagebox.showinfo("Info", "Game not finished yet.")

def validate_score():
    ball1 = int(ball1.get())
    ball2 = int(ball2.get())

def score(frame_number):
    top = tk.Toplevel(window)
    window_width = 120
    window_height = 80

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int((screen_height/2 - window_height / 2) - 150)

    top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    top.minsize(window_width, window_height)
    top.maxsize(window_width, window_height)
    
    tk.Label(top, text="Ball 1:").grid(row=0, column=0)
    ball1 = tk.Entry(top, width=2)
    ball1.grid(row=0, column=1)
    tk.Label(top, text="Ball 2:").grid(row=1, column=0)
    ball2 = tk.Entry(top, width=2)
    ball2.grid(row=1, column=1)
    if frame_number == 10:
        tk.Label(top, text="Ball 3:").grid(row=2, column=0)
        ball3 = tk.Entry(top, width=2)
        ball3.grid(row=2, column=1)
    
    submit_button = tk.Button(top, text="Submit Frame", command=lambda: validate_score())
    submit_button.grid(row=3, columnspan=2)


window = tk.Tk()

window.title("Bowling Score")
window_width = 525
window_height = 150

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.minsize(window_width, window_height)
window.maxsize(window_width, window_height)

frame_number = 1

f1b1_var = tk.IntVar()
f1b2_var = tk.IntVar()
f2b1_var = tk.IntVar()
f2b2_var = tk.IntVar()
f3b1_var = tk.IntVar()
f3b2_var = tk.IntVar()
f4b1_var = tk.IntVar()
f4b2_var = tk.IntVar()
f5b1_var = tk.IntVar()
f5b2_var = tk.IntVar()
f6b1_var = tk.IntVar()
f6b2_var = tk.IntVar()
f7b1_var = tk.IntVar()
f7b2_var = tk.IntVar()
f8b1_var = tk.IntVar()
f8b2_var = tk.IntVar()
f9b1_var = tk.IntVar()
f9b2_var = tk.IntVar()
f10b1_var = tk.IntVar()
f10b2_var = tk.IntVar()
f10b3_var = tk.IntVar()
                
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

game1_var = tk.IntVar()
game2_var = tk.IntVar()
game3_var = tk.IntVar()
series_var = tk.IntVar()
game1_var.set(0)
game2_var.set(0)
game3_var.set(0)
series_var.set(0)

start_game_button = tk.Button(window,
                         text="Start Game", 
                         command=score(frame_number),
                         bd=1,
                         bg="black",
                         fg="white",
                         font=("Arial", 12),
                         height=2,
                         justify="center",
                         relief="solid")
start_game_button.pack(side="bottom")

save_game_button = tk.Button(window, 
                         text="Save Game", 
                         command=save_game,
                         bd=1,
                         bg="white",
                         fg="black",
                         font=("Arial", 12),
                         height=2,
                         justify="center",
                         relief="solid")
save_game_button.pack(side="right")
if frame_number != 10:
    save_game_button.config(state=tk.DISABLED)
else:
    save_game_button.config(state=tk.NORMAL)

# frame 1
frame1 = ttk.Frame(window, relief="solid", borderwidth=1)
frame1.place(x=0, y=0, width=50, height=70)
frame1.columnconfigure((0,1), weight=1, uniform='a')
frame1.rowconfigure((0,1,2), weight=1)
label1 = tk.Label(frame1, text="1", border=1, borderwidth=1).grid(row=0, column=0)
f1b1 = tk.Label(frame1, borderwidth=1, textvariable=f1b1_var, relief="solid", background="blue", foreground="white", width=3)
f1b1.grid(row=1, column=0)
f1b2 = tk.Label(frame1, borderwidth=1, textvariable=f1b2_var, relief="solid", background="blue", foreground="white", width=3)
f1b2.grid(row=1, column=1)
f1score = tk.Label(frame1, textvariable=f1score_var).grid(row=2, column=1)

# frame 2
frame2 = ttk.Frame(window, relief="solid", borderwidth=1)
frame2.place(x=50, y=0, width=50, height=70)
frame2.columnconfigure((0,1), weight=1, uniform='a')
frame2.rowconfigure((0,1,2), weight=1)
label2 = ttk.Label(frame2, text="2").grid(row=0, column=0)
f2b1 = tk.Label(frame2, borderwidth=1, textvariable=f2b1_var, relief="solid", background="blue", foreground="white", width=3)
f2b1.grid(row=1, column=0)
f2b2 = tk.Label(frame2, borderwidth=1, textvariable=f2b2_var, relief="solid", background="blue", foreground="white", width=3)
f2b2.grid(row=1, column=1)
f2score = ttk.Label(frame2, textvariable=f2score_var).grid(row=2, column=1)

# frame 3
frame3 = ttk.Frame(window, relief="solid", borderwidth=1)
frame3.place(x=100, y=0, width=50, height=70)
frame3.columnconfigure((0,1), weight=1, uniform='a')
frame3.rowconfigure((0,1,2), weight=1)
label3 = ttk.Label(frame3, text="3").grid(row=0, column=0)
f3b1 = tk.Label(frame3, borderwidth=1, textvariable=f3b1_var, relief="solid", background="blue", foreground="white", width=3)
f3b1.grid(row=1, column=0)
f3b2 = tk.Label(frame3, borderwidth=1, textvariable=f3b2_var, relief="solid", background="blue", foreground="white", width=3)
f3b2.grid(row=1, column=1)
f3score = ttk.Label(frame3, textvariable=f3score_var).grid(row=2, column=1)

# frame 4
frame4 = ttk.Frame(window, relief="solid", borderwidth=1)
frame4.place(x=150, y=0, width=50, height=70)
frame4.columnconfigure((0,1), weight=1, uniform='a')
frame4.rowconfigure((0,1,2), weight=1)
label4 = ttk.Label(frame4, text="4").grid(row=0, column=0)
f4b1 = tk.Label(frame4, borderwidth=1, textvariable=f4b1_var, relief="solid", background="blue", foreground="white", width=3)
f4b1.grid(row=1, column=0)
f4b2 = tk.Label(frame4, borderwidth=1, textvariable=f4b2_var, relief="solid", background="blue", foreground="white", width=3)
f4b2.grid(row=1, column=1)
f4score = ttk.Label(frame4, textvariable=f4score_var).grid(row=2, column=1)

# frame 5
frame5 = ttk.Frame(window, relief="solid", borderwidth=1)
frame5.place(x=200, y=0, width=50, height=70)
frame5.columnconfigure((0,1), weight=1, uniform='a')
frame5.rowconfigure((0,1,2), weight=1)
label5 = ttk.Label(frame5, text="5").grid(row=0, column=0)
f5b1 = tk.Label(frame5, borderwidth=1, textvariable=f5b1_var, relief="solid", background="blue", foreground="white", width=3)
f5b1.grid(row=1, column=0)
f5b2 = tk.Label(frame5, borderwidth=1, textvariable=f5b2_var, relief="solid", background="blue", foreground="white", width=3)
f5b2.grid(row=1, column=1)
f5score = ttk.Label(frame5, textvariable=f5score_var).grid(row=2, column=1)

# frame 6
frame6 = ttk.Frame(window, relief="solid", borderwidth=1)
frame6.place(x=250, y=0, width=50, height=70)
frame6.columnconfigure((0,1), weight=1, uniform='a')
frame6.rowconfigure((0,1,2), weight=1)
label6 = ttk.Label(frame6, text="6").grid(row=0, column=0)
f6b1 = tk.Label(frame6, borderwidth=1, textvariable=f6b1_var, relief="solid", background="blue", foreground="white", width=3)
f6b1.grid(row=1, column=0)
f6b2 = tk.Label(frame6, borderwidth=1, textvariable=f6b2_var, relief="solid", background="blue", foreground="white", width=3)
f6b2.grid(row=1, column=1)
f6score = ttk.Label(frame6, textvariable=f6score_var).grid(row=2, column=1)

# frame 7
frame7 = ttk.Frame(window, relief="solid", borderwidth=1)
frame7.place(x=300, y=0, width=50, height=70)
frame7.columnconfigure((0,1), weight=1, uniform='a')
frame7.rowconfigure((0,1,2), weight=1)
label7 = ttk.Label(frame7, text="7").grid(row=0, column=0)
f7b1 = tk.Label(frame7, borderwidth=1, textvariable=f7b1_var, relief="solid", background="blue", foreground="white", width=3)
f7b1.grid(row=1, column=0)
f7b2 = tk.Label(frame7, borderwidth=1, textvariable=f7b2_var, relief="solid", background="blue", foreground="white", width=3)
f7b2.grid(row=1, column=1)
f7score = ttk.Label(frame7, textvariable=f7score_var).grid(row=2, column=1)

# frame 8
frame8 = ttk.Frame(window, relief="solid", borderwidth=1)
frame8.place(x=350, y=0, width=50, height=70)
frame8.columnconfigure((0,1), weight=1, uniform='a')
frame8.rowconfigure((0,1,2), weight=1)
label8 = ttk.Label(frame8, text="8").grid(row=0, column=0)
f8b1 = tk.Label(frame8, borderwidth=1, textvariable=f8b1_var, relief="solid", background="blue", foreground="white", width=3)
f8b1.grid(row=1, column=0)
f8b2 = tk.Label(frame8, borderwidth=1, textvariable=f8b2_var, relief="solid", background="blue", foreground="white", width=3)
f8b2.grid(row=1, column=1)
f8score = ttk.Label(frame8, textvariable=f8score_var).grid(row=2, column=1)

# frame 9
frame9 = ttk.Frame(window, relief="solid", borderwidth=1)
frame9.place(x=400, y=0, width=50, height=70)
frame9.columnconfigure((0,1), weight=1, uniform='a')
frame9.rowconfigure((0,1,2), weight=1)
label9 = ttk.Label(frame9, text="9").grid(row=0, column=0)
f9b1 = tk.Label(frame9, borderwidth=1, textvariable=f9b1_var, relief="solid", background="blue", foreground="white", width=3)
f9b1.grid(row=1, column=0)
f9b2 = tk.Label(frame9, borderwidth=1, textvariable=f9b2_var, relief="solid", background="blue", foreground="white", width=3)
f9b2.grid(row=1, column=1)
f9score = ttk.Label(frame9, textvariable=f9score_var).grid(row=2, column=1)

# frame 10
frame10 = ttk.Frame(window, relief="solid", borderwidth=1)
frame10.place(x=450, y=0, width=75, height=70)
frame10.columnconfigure((0,1,2), weight=1, uniform='a')
frame10.rowconfigure((0,1,2), weight=1)
label10 = ttk.Label(frame10, text="10").grid(row=0, column=0)
f10b1 = tk.Label(frame10, borderwidth=1, textvariable=f10b1_var, relief="solid", background="blue", foreground="white", width=3)
f10b1.grid(row=1, column=0)
f10b2 = tk.Label(frame10, borderwidth=1, textvariable=f10b2_var, relief="solid", background="blue", foreground="white", width=3)
f10b2.grid(row=1, column=1)
f10b3 = tk.Label(frame10, borderwidth=1, textvariable=f10b3_var, relief="solid", background="blue", foreground="white", width=3)
f10b3.grid(row=1, column=2)
f10score = ttk.Label(frame10, textvariable=f10score_var).grid(row=2, column=2)



window.mainloop()