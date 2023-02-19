from random import random
import tkinter as tk
import GameOfLife


def play():
    game = GameOfLife.GameOfLife(random_state=True)


root = tk.Tk()
root.title("Game of Life")
# root.geometry("1000x700")

canvas = tk.Canvas(root, width=1000, height=700, bg="#222222")
canvas.pack()

# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

gliderButton = tk.Button(root, text="Glider", bg="white", fg="black", padx=10, pady=10)
gliderButton.pack()

playButton = tk.Button(
    root, text="Play", bg="white", fg="black", padx=10, pady=10, command=play
)
playButton.pack()


root.mainloop()
