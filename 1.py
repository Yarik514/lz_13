#Варіант №8
import tkinter as tk
from math import *

def calculate_function(event=None):
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    result = (e**b + 3 * log(a + c)) / atan(a) + trunc(b*c)
    format_result = "{:.2f}".format(result)
    label_result.config(text="Результат: " + format_result)

root = tk.Tk()
root.title("Обчислення функції")
root.geometry("300x300")


# Зображення
label_image = tk.Label()
label_image.grid(row = 0, column=0, columnspan = 2)
photo = tk.PhotoImage(file="function.png")
label_image.configure(image=photo)
label_a = tk.Label(root, text="Введіть значення a:")
label_a.grid(row = 1, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row = 1, column=1)

# Написи та поля введення
label_b = tk.Label(root, text="Введіть значення b:")
label_b.grid(row = 2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row = 2, column=1)

label_c = tk.Label(root, text="Введіть значення c:")
label_c.grid(row = 3, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row = 3, column=1)

# Кнопка для обчислення
button_calculate = tk.Button(root, text="Обчислити")
button_calculate.grid(row = 4, column=0, columnspan = 2)
button_calculate.bind('<Button-1>', calculate_function)

# Відображення результату
label_result = tk.Label(root, text="")
label_result.grid(row = 5, column=0, columnspan = 2)

root.mainloop()