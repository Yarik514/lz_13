import tkinter as tk
from tkinter import messagebox
from math import *

def suma_series(event):
    n = int(entry_n.get())
    x = float(entry_x.get())
    if n < 1:
        messagebox.showerror("Помилка", "Введіть ціле число більше або рівне 1 для n!")
        return

    result = 0
    for i in range(1, n+1):
        result += 5 * log(2*i*x, e) / (atan(2 * x) + i ** 2)

    label_result.config(text=f"Сума ряду: {result}")

root = tk.Tk()
root.title("Обчислення суми ряду")
root.geometry("400x200")

label_n = tk.Label(root, text="Введіть значення n:")
label_n.grid(row=0, column=0, padx=10, pady=10)

entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1, padx=10, pady=10)
entry_n.focus()

label_x = tk.Label(root, text="Введіть значення x:")
label_x.grid(row=1, column=0, padx=10, pady=10)

entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Обчислити")
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
button_calculate.bind("<Button-1>", suma_series)

label_result = tk.Label(root, text="Результат:")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
