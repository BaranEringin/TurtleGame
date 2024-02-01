import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("gray")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("white")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingSquare(300)
shrinkingSquare(280)
shrinkingSquare(260)
shrinkingSquare(240)
shrinkingSquare(220)
shrinkingSquare(200)
shrinkingSquare(180)
shrinkingSquare(160)
shrinkingSquare(140)
shrinkingSquare(120)
shrinkingSquare(100)
shrinkingSquare(80)
shrinkingSquare(60)
shrinkingSquare(40)
shrinkingSquare(20)

turtle.done()
