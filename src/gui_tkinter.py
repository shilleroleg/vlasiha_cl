import tkinter as tk


def callback_button_help(event):
    table_name.delete(0, tk.END)
    table_name.insert(tk.END, ("click! x =", event.x, "y =", event.y))


def callback_button_ins(event):
    canvas.create_rectangle(100, 100, 200, 200, tags='home')

    canvas.create_line(100, 100, 150, 50, tags='roof1')
    canvas.create_line(150, 50, 200, 100, tags='roof2')

    canvas.create_rectangle(130, 130, 170, 170, fill='orange', tags='window')

    canvas.create_oval(140, 70, 160, 90, tags='roof_window')

    canvas.create_line(0, 0, 150, 50, fill='green',
                       width=5, arrow=tk.LAST, dash=(10, 2),
                       activefill='lightgreen',
                       arrowshape="10 20 10")


def callback_button_clear(event):
    canvas.delete('all')


def canvas_callback(event):
    win_color = canvas.itemcget('roof_window', 'fill')
    if win_color != 'orange':
        canvas.itemconfig('roof_window', fill="orange")
    else:
        canvas.itemconfig('roof_window', fill="white")


# You should only create one root widget for each program, and it must be created before any other widgets.
root = tk.Tk()
# root.minsize(width=500, height=400)  # Размер окна

# Next, we create a Label widget as a child to the root window:
# Располагаем по сетке, в ячейке (0, 0) от левого верхнего угла окна
tk.Label(root, text="Имя:", font="Times 14").grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
#
table_name = tk.Entry(width=30)
table_name.grid(row=0, column=1, columnspan=3, sticky=tk.W+tk.E, padx=10)
#
tk.Label(text="Столбцов:", font="Times 14").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
table_column = tk.Spinbox(width=7, from_=1, to=50)
table_column.grid(row=1, column=1, padx=10)

tk.Label(text="Строк:", font="Times 14").grid(row=1, column=2, sticky=tk.E)
table_row = tk.Spinbox(width=7, from_=1, to=100)
table_row.grid(row=1, column=3, sticky=tk.E, padx=10)

# Создаем холст
canvas = tk.Canvas(root, width=300, height=250, bg='white')
canvas.tag_bind('roof_window', '<Button-1>', canvas_callback)  # Событие при клике на фигуру(маленькое окно на крыше)
# canvas.bind("<Button-1>", canvas_callback)
canvas.grid(row=2, column=0, columnspan=4)

# Создаем кнопки
b_help = tk.Button(text="Справка", width=10, height=2)
b_ins = tk.Button(text="Вставить", width=10, height=2)
b_clear = tk.Button(text="Отменить", width=10, height=2)

# Привязываем события
b_help.bind('<Button-1>', callback_button_help)   # Левая кнопка
b_help.bind('<Return>', callback_button_help)     # Enter

b_ins.bind('<Button-1>', callback_button_ins)

b_clear.bind('<Button-1>', callback_button_clear)

# Пакуем кнопки
b_help.grid(row=3, column=0, pady=10, padx=10)
b_ins.grid(row=3, column=2)
b_clear.grid(row=3, column=3, padx=10)


# The program will stay in the event loop until we close the window.
root.mainloop()
