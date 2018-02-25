from tkinter import *


def calculate():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 * num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!')


def calculate2():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 / num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!')


def calculate3():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 + num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!')


def calculate4():
    try:
        num1 = float(enter1.get())
        num2 = float(enter2.get())
        result = num1 - num2
        label3.config(text=str(result))
    except ValueError:
        label3.config(text='Enter numeric values!')

root = Tk()


label1 = Label(root, text='First Number:')
label1.grid(row=0, column=1)
enter1 = Entry(root, bg='white')
enter1.grid(row=1, column=1)


label2 = Label(root, text='Second Number:')
label2.grid(row=2, column=1)
enter2 = Entry(root, bg='white')
enter2.grid(row=3, column=1)


btn1 = Button(root, text='X', command=calculate)
btn1.grid(row=4, column=1)
btn2 = Button(root, text='/', command=calculate2)
btn2.grid(row=5, column=1)
btn3 = Button(root, text='+', command=calculate3)
btn3.grid(row=5, column=2)
btn4 = Button(root, text='-', command=calculate4)
btn4.grid(row=4, column=2)

label3 = Label(root)
label3.grid(row=6, column=1)


enter1.focus()

enter1.bind('<Return>', func=lambda e:enter2.focus_set())

root.mainloop()