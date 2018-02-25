from tkinter import *
from tkinter import messagebox, ttk


def open_msg_box():
    messagebox.showwarning("Event Triggered",
                           "Button Clicked")

root = Tk()

root.geometry("400x400+300+300")
root.resizable(width=False, height=False)
frame = Frame(root)

# http://wiki.tck/37701
style = ttk.Style()
style.configure("TButton",
                foreground="midnight blue",
                font="Times 20 bold italic",
                padding=20)

# Ttk widget names: TButton, TCheckbutton, TCombobox,
# TEntry: TFrame, TLable, TLabelFrame, TMenubutton,
# TNotebook, TProgressbar, TRadiobutton, TScale,
# TScrollbar, TSpinbox, Treeview

ttk.Style().theme_use("vista")
print(ttk.Style().theme_names())
print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "foreground"))
print(style.lookup("TButton", "padding"))

theButton = ttk.Button(frame,
                       text="Important button",
                       command=open_msg_box)
theButton['state'] = 'disabled'
theButton['state'] = 'normal'

theButton.pack()
frame.pack()

root.mainloop()
