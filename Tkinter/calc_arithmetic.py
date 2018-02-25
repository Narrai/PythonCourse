import tkinter
from tkinter import messagebox


# function to do arithmetic calculations
def arithmetic_operations():
    try:
        num1 = float(textbox1.get())
        num2 = float(textbox2.get())
        if rbVar.get() == 1:
            return num1 + num2
    except ValueError:
        messagebox.showwarning(message="Invalid input format")
        return
    try:
        num1 = float(textbox1.get())
        num2 = float(textbox2.get())
        if rbVar.get() == 2:
            return num1 - num2
    except ValueError:
        messagebox.showwarning(message="Invalid input format")
        return
    try:
        num1 = float(textbox1.get())
        num2 = float(textbox2.get())
        if rbVar.get() == 3:
            return num1 * num2
    except ValueError:
        messagebox.showwarning(message="Invalid input format")
        return
    try:
        num1 = float(textbox1.get())
        num2 = float(textbox2.get())
        if rbVar.get() == 4:
            try:
                return num1 / num2
            except ZeroDivisionError:
                messagebox.showwarning(message="Divide by Zero ERROR!")
                return
    except ValueError:
        messagebox.showwarning(message="Invalid input format")
        return


# function to show the result
def show():
    result_var = str(arithmetic_operations())
    show_var.set(result_var)

# mainWindow
mainWindow = tkinter.Tk()
mainWindow.title("COMP3140 GUI Practice")
mainWindow.geometry("600x480+50+20")

frame1 = tkinter.Frame(mainWindow)
frame1.grid(row=0, column=0, sticky='ne')

label1 = tkinter.Label(frame1, text="Number 1")
label1.grid(row=0, column=0)
label1.configure(pady=20, padx=20)

textbox1 = tkinter.Entry(frame1)
textbox1.grid(row=0, column=1)

label2 = tkinter.Label(frame1, text="Number 2")
label2.grid(row=2, column=0)

textbox2 = tkinter.Entry(frame1)
textbox2.grid(row=2, column=1)


frame2 = tkinter.LabelFrame(mainWindow, text="Arithmetic operations")
frame2.grid(row=1, column=0, padx=20, pady=20)

rbVar = tkinter.IntVar()
rbVar.set(2)

add_button = tkinter.Radiobutton(frame2, text="Add(+)", value=1, variable=rbVar)
subtract_button = tkinter.Radiobutton(frame2, text="Subtract(-)", value=2, variable=rbVar)
multiply_button = tkinter.Radiobutton(frame2, text="Multiply(x)", value=3, variable=rbVar)
divide_button = tkinter.Radiobutton(frame2, text="Divide(/)", value=4, variable=rbVar)
add_button.grid(row=0, column=0, sticky='w')
subtract_button.grid(row=1, column=0, sticky='w')
multiply_button.grid(row=2, column=0, sticky='w')
divide_button.grid(row=3, column=0, sticky='w')

frame3 = tkinter.Frame(mainWindow)
frame3.grid(row=2, column=0, sticky='se')

calc_button = tkinter.Button(frame3, text="Calculate", command=show)
calc_button.grid(row=0, column=0, padx=20)

show_var = tkinter.StringVar()
result_box = tkinter.Entry(frame3, textvariable=show_var)
result_box.grid(row=0, column=1)

mainWindow.mainloop()
