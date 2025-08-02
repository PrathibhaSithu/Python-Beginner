import tkinter as tk


def greet():
    name = entry.get()
    label_output.config(text=f"Hello, {name}!")


window = tk.Tk()
window.title("Greeting App")
window.geometry("300x150")

label = tk.Label(window, text="Enter your name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Greet", command=greet)
button.pack()

label_output = tk.Label(window, text="")
label_output.pack()

window.mainloop()
