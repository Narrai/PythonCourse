"""
    Program file: c-curve.py
    Author: Nar Rai

    This program prompts the user for the level of a c-curve
    and draws a c-curve of that level
"""

from turtle import Turtle


def c_curve(t, x1, y1, x2, y2, level):
    """Draws a c-curve of the given level."""
    if level == 0:
        draw_line(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        c_curve(t, x1, y1, xm, ym, level - 1)
        c_curve(t, xm, ym, x2, y2, level - 1)


def draw_line(x1, y1, x2, y2):
    """Draws a line segment between the endpoints."""
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

if __name__ == "__main__":
    level = int(input("Enter the level (0 or greater): "))
    t = Turtle()
    t.hideturtle()
    c_curve(t, 50, -50, 50, 50, level)

