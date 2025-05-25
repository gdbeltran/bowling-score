import tkinter as tk
from tkinter import ttk, messagebox
from bowl_frame import BowlFrame
from score import score_frame

def clear_variables():
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

frames = []

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

# frame 1
frame1 = ttk.Frame(window, relief="solid", borderwidth=1)
frame1.place(x=0, y=0, width=50, height=70)
frame1.columnconfigure((0,1), weight=1, uniform='a')
frame1.rowconfigure((0,1,2), weight=1)
label1 = ttk.Label(frame1, text="1", border=1, borderwidth=1)
label1.grid(row=0, column=0)
f1b1 = ttk.Entry(frame1, width=2)
f1b1.grid(row=1, column=0)
f1b2 = ttk.Entry(frame1, width=2)
f1b2.grid(row=1, column=1)
f1score = ttk.Label(frame1, textvariable=f1score_var, anchor="w", justify="left")
f1score.grid(row=2, column=1, padx=5)

# frame 2
frame2 = ttk.Frame(window, relief="solid", borderwidth=1)
frame2.place(x=50, y=0, width=50, height=70)
frame2.columnconfigure((0,1), weight=1, uniform='a')
frame2.rowconfigure((0,1,2), weight=1)
label2 = ttk.Label(frame2, text="2")
label2.grid(row=0, column=0)
f2b1 = ttk.Entry(frame2, width=2)
f2b1.grid(row=1, column=0)
f2b2 = ttk.Entry(frame2, width=2)
f2b2.grid(row=1, column=1)
f2score = ttk.Label(frame2, textvariable=f2score_var, anchor="w", justify="left")
f2score.grid(row=2, column=1, padx=5)
frame2.place_forget()

# frame 3
frame3 = ttk.Frame(window, relief="solid", borderwidth=1)
frame3.place(x=100, y=0, width=50, height=70)
frame3.columnconfigure((0,1), weight=1, uniform='a')
frame3.rowconfigure((0,1,2), weight=1)
label3 = ttk.Label(frame3, text="3")
label3.grid(row=0, column=0)
f3b1 = ttk.Entry(frame3, width=2)
f3b1.grid(row=1, column=0)
f3b2 = ttk.Entry(frame3, width=2)
f3b2.grid(row=1, column=1)
f3score = ttk.Label(frame3, textvariable=f3score_var, anchor="w", justify="left")
f3score.grid(row=2, column=1, padx=5)
frame3.place_forget()

# frame 4
frame4 = ttk.Frame(window, relief="solid", borderwidth=1)
frame4.place(x=150, y=0, width=50, height=70)
frame4.columnconfigure((0,1), weight=1, uniform='a')
frame4.rowconfigure((0,1,2), weight=1)
label4 = ttk.Label(frame4, text="4")
label4.grid(row=0, column=0)
f4b1 = ttk.Entry(frame4, width=2)
f4b1.grid(row=1, column=0)
f4b2 = ttk.Entry(frame4, width=2)
f4b2.grid(row=1, column=1)
f4score = ttk.Label(frame4, textvariable=f4score_var, anchor="w", justify="left")
f4score.grid(row=2, column=1, padx=5)
frame4.place_forget()

# frame 5
frame5 = ttk.Frame(window, relief="solid", borderwidth=1)
frame5.place(x=200, y=0, width=50, height=70)
frame5.columnconfigure((0,1), weight=1, uniform='a')
frame5.rowconfigure((0,1,2), weight=1)
label5 = ttk.Label(frame5, text="5")
label5.grid(row=0, column=0)
f5b1 = ttk.Entry(frame5, width=2)
f5b1.grid(row=1, column=0)
f5b2 = ttk.Entry(frame5, width=2)
f5b2.grid(row=1, column=1)
f5score = ttk.Label(frame5, textvariable=f5score_var, anchor="w", justify="left")
f5score.grid(row=2, column=1, padx=5)
frame5.place_forget()

# frame 6
frame6 = ttk.Frame(window, relief="solid", borderwidth=1)
frame6.place(x=250, y=0, width=50, height=70)
frame6.columnconfigure((0,1), weight=1, uniform='a')
frame6.rowconfigure((0,1,2), weight=1)
label6 = ttk.Label(frame6, text="6")
label6.grid(row=0, column=0)
f6b1 = ttk.Entry(frame6, width=2)
f6b1.grid(row=1, column=0)
f6b2 = ttk.Entry(frame6, width=2)
f6b2.grid(row=1, column=1)
f6score = ttk.Label(frame6, textvariable=f6score_var, anchor="w", justify="left")
f6score.grid(row=2, column=1, padx=5)
frame6.place_forget()

# frame 7
frame7 = ttk.Frame(window, relief="solid", borderwidth=1)
frame7.place(x=300, y=0, width=50, height=70)
frame7.columnconfigure((0,1), weight=1, uniform='a')
frame7.rowconfigure((0,1,2), weight=1)
label7 = ttk.Label(frame7, text="7")
label7.grid(row=0, column=0)
f7b1 = ttk.Entry(frame7, width=2)
f7b1.grid(row=1, column=0)
f7b2 = ttk.Entry(frame7, width=2)
f7b2.grid(row=1, column=1)
f7score = ttk.Label(frame7, textvariable=f7score_var, anchor="w", justify="left")
f7score.grid(row=2, column=1, padx=5)
frame7.place_forget()

# frame 8
frame8 = ttk.Frame(window, relief="solid", borderwidth=1)
frame8.place(x=350, y=0, width=50, height=70)
frame8.columnconfigure((0,1), weight=1, uniform='a')
frame8.rowconfigure((0,1,2), weight=1)
label8 = ttk.Label(frame8, text="8")
label8.grid(row=0, column=0)
f8b1 = ttk.Entry(frame8, width=2)
f8b1.grid(row=1, column=0)
f8b2 = ttk.Entry(frame8, width=2)
f8b2.grid(row=1, column=1)
f8score = ttk.Label(frame8, textvariable=f8score_var, anchor="w", justify="left")
f8score.grid(row=2, column=1, padx=5)
frame8.place_forget()

# frame 9
frame9 = ttk.Frame(window, relief="solid", borderwidth=1)
frame9.place(x=400, y=0, width=50, height=70)
frame9.columnconfigure((0,1), weight=1, uniform='a')
frame9.rowconfigure((0,1,2), weight=1)
label9 = ttk.Label(frame9, text="9")
label9.grid(row=0, column=0)
f9b1 = ttk.Entry(frame9, width=2)
f9b1.grid(row=1, column=0)
f9b2 = ttk.Entry(frame9, width=2)
f9b2.grid(row=1, column=1)
f9score = ttk.Label(frame9, textvariable=f9score_var, anchor="w", justify="left")
f9score.grid(row=2, column=1, padx=5)
frame9.place_forget()

# frame 10
frame10 = ttk.Frame(window, relief="solid", borderwidth=1)
frame10.place(x=450, y=0, width=75, height=70)
frame10.columnconfigure((0,1,2), weight=1, uniform='a')
frame10.rowconfigure((0,1,2), weight=1)
label10 = ttk.Label(frame10, text="10")
label10.grid(row=0, column=0)
f10b1 = ttk.Entry(frame10, width=2)
f10b1.grid(row=1, column=0)
f10b2 = ttk.Entry(frame10, width=2)
f10b2.grid(row=1, column=1)
f10b3 = ttk.Entry(frame10, width=2)
f10b3.grid(row=1, column=2)
f10score = ttk.Label(frame10, textvariable=f10score_var, anchor="w", justify="left")
f10score.grid(row=2, column=2, padx=5)
frame10.place_forget()

def end_frame():
    global frame_number, frames
    # validate entered scores, calculate frame and game scores, then generate the next frame
    match frame_number:
        case 1:
            try:
                ball1 = int(f1b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 1.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f1b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 1.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 1: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f1score_var.set(frames[0].score)
            frame2.place(x=50, y=0, width=50, height=70)
            frame_number += 1
            f1b1.config(state=tk.DISABLED)
            f1b2.config(state=tk.DISABLED)
        case 2:
            try:
                ball1 = int(f2b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 2.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f2b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 2.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 2: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f1score_var.set(frames[0].score)
            f2score_var.set(frames[1].running_total)
            frame3.place(x=100, y=0, width=50, height=70)
            frame_number += 1
            f2b1.config(state=tk.DISABLED)
            f2b2.config(state=tk.DISABLED)
        case 3:
            try:
                ball1 = int(f3b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 3.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f3b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 3.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 3: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f1score_var.set(frames[0].score)
            f2score_var.set(frames[1].running_total)
            f3score_var.set(frames[2].running_total)
            frame4.place(x=150, y=0, width=50, height=70)
            frame_number += 1
            f3b1.config(state=tk.DISABLED)
            f3b2.config(state=tk.DISABLED)
        case 4:
            try:
                ball1 = int(f4b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 4.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f4b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 4.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 4: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f2score_var.set(frames[1].running_total)
            f3score_var.set(frames[2].running_total)
            f4score_var.set(frames[3].running_total)
            frame5.place(x=200, y=0, width=50, height=70)
            frame_number += 1
            f4b1.config(state=tk.DISABLED)
            f4b2.config(state=tk.DISABLED)
        case 5:
            try:
                ball1 = int(f5b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 5.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f5b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 5.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 5: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f3score_var.set(frames[2].running_total)
            f4score_var.set(frames[3].running_total)
            f5score_var.set(frames[4].running_total)
            frame6.place(x=250, y=0, width=50, height=70)
            frame_number += 1
            f5b1.config(state=tk.DISABLED)
            f5b2.config(state=tk.DISABLED)
        case 6:
            try:
                ball1 = int(f6b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 6.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f6b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 6.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 6: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f4score_var.set(frames[3].running_total)
            f5score_var.set(frames[4].running_total)
            f6score_var.set(frames[5].running_total)
            frame7.place(x=300, y=0, width=50, height=70)
            frame_number += 1
            f6b1.config(state=tk.DISABLED)
            f6b2.config(state=tk.DISABLED)
        case 7:
            try:
                ball1 = int(f7b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 7.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f7b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 7.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 7: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f5score_var.set(frames[4].running_total)
            f6score_var.set(frames[5].running_total)
            f7score_var.set(frames[6].running_total)
            frame8.place(x=350, y=0, width=50, height=70)
            frame_number += 1
            f7b1.config(state=tk.DISABLED)
            f7b2.config(state=tk.DISABLED)
        case 8:
            try:
                ball1 = int(f8b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 8.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f8b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 8.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 8: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f6score_var.set(frames[5].running_total)
            f7score_var.set(frames[6].running_total)
            f8score_var.set(frames[7].running_total)
            frame9.place(x=400, y=0, width=50, height=70)
            frame_number += 1
            f8b1.config(state=tk.DISABLED)
            f8b2.config(state=tk.DISABLED)
        case 9:
            try:
                ball1 = int(f9b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 9.")
                return
            if ball1 == 10:
                ball2 = 0
            else:
                try:
                    ball2 = int(f9b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 9.")
                    return
            if ball1 < 0 or ball2 < 0 or ball1 + ball2 > 10:
                messagebox.showerror("Invalid Input", "Frame 9: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2))
            score_frame(frame_number, frames, ball1, ball2)
            f7score_var.set(frames[6].running_total)
            f8score_var.set(frames[7].running_total)
            f9score_var.set(frames[8].running_total)
            frame10.place(x=450, y=0, width=75, height=70)
            frame_number += 1
            f9b1.config(state=tk.DISABLED)
            f9b2.config(state=tk.DISABLED)
        case 10:
            try:
                ball1 = int(f10b1.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 10.")
                return
            if ball1 == 10:
                try:
                    ball2 = int(f10b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 10.")
                    return
                if ball2 == 10:
                    try:
                        ball3 = int(f10b3.get())
                    except ValueError:
                        messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 10.")
                        return
            else:
                try:
                    ball2 = int(f10b2.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 10.")
                    return
                if ball1 + ball2 == 10:
                    try:
                        ball3 = int(f10b3.get())
                    except ValueError:
                        messagebox.showerror("Invalid Input", "Please enter valid numbers for Frame 10.")
                        return
            if ball1 < 0 or ball2 < 0 or ball3 < 0 or ball1 + ball2 + ball3 > 30:
                messagebox.showerror("Invalid Input", "Frame 10: Invalid scores entered.")
                return
            frames.append(BowlFrame(ball1, ball2, ball3))
            score_frame(frame_number, frames, ball1, ball2, ball3)
            f8score_var.set(frames[7].running_total)
            f9score_var.set(frames[8].running_total)
            f10score_var.set(frames[9].running_total)
            f10b1.config(state=tk.DISABLED)
            f10b2.config(state=tk.DISABLED)
            f10b3.config(state=tk.DISABLED)
            
end_frame_button = tk.Button(window, 
                         text="End Frame", 
                         command=end_frame,
                         bd=1,
                         bg="white",
                         fg="black",
                         font=("Arial", 12),
                         height=2,
                         justify="center",
                         relief="solid")
end_frame_button.pack(side="bottom")

window.mainloop()