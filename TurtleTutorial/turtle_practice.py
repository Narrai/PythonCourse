from turtle import Turtle

t = Turtle()


def draw_square(x, y, length):
    t.screen.bgcolor("cyan")
    t.up()
    t.goto(x, y)
    # t.setheading(270)
    t.down()
    t.position()
    print(t.position())
    for count in range(4):
        t.forward(length)
        t.left(90)


if __name__ == "__main__":
    draw_square(10, 10, 100)