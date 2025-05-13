import tkinter as tk
from tkinter import messagebox
from math import sqrt

def calculate_triangle(event):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a + b > c and a + c > b and b + c > a:
            wb = sqrt(a*c*(a + b + c)*(a + c - b)) / (a + c)
            wg = sqrt(a * b * (a + b + c) * (a + b - c)) / (a + b)

            entry_wb.delete(0, tk.END)
            entry_wb.insert(tk.END, "{:.2f}".format(wb))

            entry_wg.delete(0, tk.END)
            entry_wg.insert(tk.END, "{:.2f}".format(wg))
        else:
            messagebox.showerror("Помилка", "Трикутник із заданими сторонами не існує!")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення для сторін трикутника!")

def highlight_active(event):
    event.widget.configure(bg="yellow")

def remove_highlight(event):
    event.widget.configure(bg="white")

root = tk.Tk()
root.title("Обчислення площі і периметра трикутника")
root.geometry("400x300")

label_a = tk.Label(root, text="Сторона a:")
label_a.place(x=20, y=20)
entry_a = tk.Entry(root)
entry_a.place(x=120, y=20)
entry_a.focus()

label_b = tk.Label(root, text="Сторона b:")
label_b.place(x=20, y=50)
entry_b = tk.Entry(root)
entry_b.place(x=120, y=50)

label_c = tk.Label(root, text="Сторона c:")
label_c.place(x=20, y=80)
entry_c = tk.Entry(root)
entry_c.place(x=120, y=80)

entry_a.bind("<FocusIn>", highlight_active)
entry_a.bind("<FocusOut>", remove_highlight)
entry_b.bind("<FocusIn>", highlight_active)
entry_b.bind("<FocusOut>", remove_highlight)
entry_c.bind("<FocusIn>", highlight_active)
entry_c.bind("<FocusOut>", remove_highlight)

button_calculate = tk.Button(root, text="Обчислити", bg="#3030fc")
button_calculate.place(x=120, y=120)
button_calculate.bind("<Button-1>", calculate_triangle)

label_wb = tk.Label(root, text="Бісектриса wb:")
label_wb.place(x=20, y=160)
entry_wb = tk.Entry(root, width=10)
entry_wb.place(x=120, y=160)

label_wg = tk.Label(root, text="Бісектриса wg:")
label_wg.place(x=20, y=190)
entry_wg = tk.Entry(root, width=10)
entry_wg.place(x=120, y=190)

root.mainloop()
