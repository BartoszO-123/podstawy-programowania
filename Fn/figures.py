
import turtle


def draw_square(length):
    pen = turtle.Turtle()

    for _ in range(4):
        pen.forward(length)
        pen.right(90)


def draw_trangle(length):
    pen = turtle.Turtle()
    pen.speed(0)

    for _ in range(3):
        pen.forward(length)
        pen.right(120)


def draw_rectangle(lenght_a, lenght_b):
    pen = turtle.Turtle()
    pen.speed(0)

    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)
