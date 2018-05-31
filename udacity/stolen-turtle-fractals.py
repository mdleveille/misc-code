import turtle


def fractal(turt, len, depth):
    if depth == 0:
        for i in range(3):
            turt.forward(len)
            turt.left(120)
    else:
        for i in range(3):
            turt.forward(len)
            turt.left(120)
            fractal(turt, len / 2, depth - 1)
            turtle.speed(1000)


window = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
window.bgcolor('green')
turtle.fillcolor('red')
fractal(turtle, 500, 3)
window.exitonclick()
