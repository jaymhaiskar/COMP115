import turtle
import random

screen = turtle.Screen()
# screen.setup(width=100, height=100)
screen.bgcolor("lightblue")

pen = turtle.Turtle()

turtle_colors = [
    "red",
    "yellow",
    "orange",
    "cyan",
    "purple",
    "violet",
    "pink",
    "white",
    "skyblue",
    "beige",
]


def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)


def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.left(120)


def draw_grass():
    pen.color("green")
    pen.begin_fill()
    for i in range(2):
        pen.forward(1600)
        pen.left(90)
        pen.forward(300)
        pen.left(90)
    pen.end_fill()


def draw_house():
    pen.color("darkblue")
    pen.begin_fill()
    pen.goto(-100, 100)
    draw_square(200)
    pen.end_fill()


def draw_roof():
    pen.color("brown")
    pen.begin_fill()
    pen.goto(-100, 100)
    pen.forward(200)
    pen.left(140)
    pen.forward(141)
    pen.left(85)
    pen.forward(141)
    pen.end_fill()


def draw_chimney():
    pen.penup()
    pen.goto(-90, 100)
    pen.color("brown")
    pen.begin_fill()
    pen.left(90)
    pen.forward(30)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.forward(30)
    pen.left(90)
    pen.forward(100)
    pen.end_fill()


def draw_door():
    pen.penup()
    pen.goto(-25, -100)
    pen.pendown()
    pen.right(225)
    pen.color("gray")
    pen.begin_fill()
    pen.forward(50)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(60)
    pen.end_fill()


def draw_window(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    # window sill
    pen.penup()
    pen.goto(x + 25, y - 25)
    pen.color("black")
    pen.pendown()
    pen.begin_fill()
    for i in range(4):
        pen.forward(25)
        pen.backward(25)
        pen.left(90)
    pen.end_fill()


def draw_sun():
    pen.penup()
    pen.goto(-390, 200)
    pen.color("yellow")
    pen.pendown()
    pen.begin_fill()
    pen.circle(40)
    pen.end_fill()

    for i in range(12):
        pen.penup()
        pen.goto(-350, 200)
        pen.pendown()
        pen.forward(90)

        # pen.penup()
        # pen.goto(-350, 240)
        pen.left(360 // 12)


def draw_cloud():
    for i in range(8):
        randx = random.randint(210, 250)
        randy = random.randint(215, 270)
        pen.penup()
        pen.goto(
            randx + 10, randy + 5
        )  # change these to diff. coordinates so you have diff. circles
        pen.pendown()
        pen.color("white")
        pen.begin_fill()
        pen.circle(25)
        pen.end_fill()


def draw_small_petal_flower():
    for i in range(10):
        randx = random.randint(-600, 600)
        randy = random.randint(-300, -100)
        print("randx= ", randx)
        print("randy= ", randy)
        pen.penup()
        pen.goto(randx, randy)
        # pen.right(90)
        pen.pendown()
        pen.color("black")
        pen.forward(40)
        pen.backward(40)

        pen.color("red")
        for _ in range(6):
            pen.begin_fill()
            pen.circle(20, 60)
            pen.left(120)
            pen.circle(20, 60)
            pen.left(120)
            pen.end_fill()
            pen.right(60)


def draw_multicolor_flower():
    # pen.right(90)
    for i in range(10):
        randx = random.randint(-600, 600)
        randy = random.randint(-300, -100)
        pen.penup()
        pen.goto(randx, randy)
        pen.pendown()
        pen.color("black")
        pen.forward(40)
        pen.backward(40)

        pen.color(turtle_colors[i])
        for _ in range(1):
            pen.goto(randx - 10, randy)
            pen.begin_fill()
            pen.circle(10)
            # pen.left(120)
            # pen.circle(20, 60)
            # pen.left(120)
            pen.end_fill()
            # pen.right(60)


pen.penup()
pen.goto(-800, -400)
draw_grass()
draw_house()
draw_roof()
draw_door()
draw_window(-90, 70)
draw_window(-90, 0)
draw_window(40, 70)
draw_window(40, 0)
draw_chimney()
draw_sun()

draw_cloud()

draw_small_petal_flower()


draw_multicolor_flower()
turtle.done()
