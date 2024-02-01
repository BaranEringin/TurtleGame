import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("gray")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("white")
turtle_colors = ["white", "red" , "yellow"]

for a in range(15):
    turtle_instance.color(turtle_colors[a % 3])
    turtle_instance.circle(10 * a)
    turtle_instance.circle(-10 * a)
    turtle_instance.left(a)



turtle.mainloop()