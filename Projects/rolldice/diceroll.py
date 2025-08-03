import tkinter as tk
from tkinter import PhotoImage
import random
import os

# Create main window
window = tk.Tk()
window.title("Dice Roll Game")
window.geometry("300x300")
window.config(bg="#f0f0f0")

# Load dice images
dice_images = []
for i in range(1, 7):
    path = os.path.join("assets", f"dice{i}.png")
    img = PhotoImage(file=path)
    dice_images.append(img)

# Label to display dice
dice_label = tk.Label(window, image=dice_images[0])
dice_label.pack(pady=20)

# Label for result text
result_label = tk.Label(
    window, text="Click to Roll the Dice!", font=("Arial", 14), bg="#f0f0f0")
result_label.pack()

# Roll dice function


def roll_dice():
    roll = random.randint(1, 6)
    dice_label.config(image=dice_images[roll - 1])
    result_label.config(text=f"You rolled a {roll}!")


# Roll button
roll_button = tk.Button(window, text="Roll Dice 🎲", command=roll_dice, font=(
    "Arial", 12), bg="#4caf50", fg="white")
roll_button.pack(pady=20)

# Run the app
window.mainloop()
