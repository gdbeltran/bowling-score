from tkinter import ttk, messagebox
from window import game_window

def main():
    print("Welcome to the Bowling Score Tracker!")
    game1 = game_window(1)
    game2 = game_window(2)
    game3 = game_window(3)
    series = game1 + game2 + game3
    average = series / 3
    messagebox.showinfo("Bowling Score Tracker", f"Game 1: {game1}\nGame 2: {game2}\nGame 3: {game3}\nSeries: {series}\nAverage: {average:.2f}")

    return

if __name__ == "__main__":
    main()