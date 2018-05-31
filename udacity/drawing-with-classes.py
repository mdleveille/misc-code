import turtle
# this code is an example that shows how to use a class. Here, Turtle is a class. It is a blueprint that has pre-defined attributes. Objects within that class (alice, bob, and charlie) are specific instances of that class.


def drawSquare(champion):
    for num in [0, 1, 2, 3]:
        champion.forward(200)
        champion.right(90)


def drawCirle(champion):
    champion.circle(100)


def drawTriangle(champion):
    for num in [0, 1, 2]:
        champion.forward(100)
        champion.left(120)


# def drawShapes():
#     # Make window
#     window = turtle.Screen()
#     window.bgcolor('red')

#     # Make Alice
#     alice = turtle.Turtle()
#     alice.shape('turtle')
#     alice.speed(10)

#     # Make Bob
#     bob = turtle.Turtle()
#     bob.shape('turtle')
#     bob.speed(10)

#     # Makes Charlie
#     charlie = turtle.Turtle()
#     charlie.shape('turtle')
#     charlie.speed(10)

#     drawSquare(alice)
#     drawCirle(bob)
#     drawTriangle(charlie)

#     window.exitonclick()


def drawCircleSquare():
    window = turtle.Screen()
    window.bgcolor('red')

    # Make Alice
    alice = turtle.Turtle()
    alice.shape('turtle')
    alice.speed(50)
    alice.color('yellow')

    for i in range(1, 37):
        drawSquare(alice)
        alice.right(10)

    window.exitonclick()


drawCircleSquare()
