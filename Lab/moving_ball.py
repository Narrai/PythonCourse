from tkinter import *
import time

tk = Tk()
Height = 480
Width = 600

tk.title("Moving ball demo")
canvas = Canvas(tk, width=Width, height=Height)
canvas.pack()

ball = canvas.create_oval(1, 1, 50, 50, fill='red')
delta_x1 = 5
delta_y1 = 0

ball1 = canvas.create_oval(1, 1, 50, 50, fill='blue')
delta_x2 = 0
delta_y2 = 8

var1 = StringVar()
var1.set('(0,0)')

var2 = StringVar()
var2.set('(0, 0)')

coord1 = Label(canvas, textvariable=var1, fg='red')
label_font1 = ('times', 20, 'bold', 'italic')
coord1.configure(font=label_font1)
coord1.pack()
canvas.create_window(300, 240, window=coord1)

coord2 = Label(canvas, textvariable=var2, fg='blue')
label_font2 = ('times', 20, 'bold', 'italic')
coord2.configure(font=label_font2)
coord2.pack()
canvas.create_window(250, 200, window=coord2)

# move the red ball and blue ball
while True:
    canvas.move(ball, delta_x1, delta_y1)
    pos = canvas.coords(ball)

    if pos[0] <= 1 and pos[1] <= 1:
        delta_x1 = 5
        delta_y1 = 0
    elif pos[2] >= Width and pos[3] <= Height:
        delta_x1 = 0
        delta_y1 = 5
    elif pos[2] >= Width and pos[3] >= Height:
        delta_x1 = -5
        delta_y1 = 0
    elif pos[0] <= 1 and pos[3] >= Height:
        delta_x1 = 0
        delta_y1 = -5
    var1.set('(%d, %d)' % (pos[0], pos[1]))

    canvas.move(ball1, delta_x2, delta_y2)
    pos1 = canvas.coords(ball1)

    if pos1[0] <= 1 and pos1[1] <= 1:
        delta_y2 = 8
        delta_x2 = 0
    elif pos1[0] <= 1 and pos1[3] >= Height:
        delta_y2 = 0
        delta_x2 = 8
    elif pos1[2] >= Width and pos1[3] >= Height:
        delta_x2 = 0
        delta_y2 = -8
    elif pos1[0] <= Width and pos1[1] <= 1:
        delta_x2 = -8
        delta_y2 = 0
    var2.set('(%d, %d)' % (pos1[0], pos1[1]))
    tk.update()
    time.sleep(0.03)
