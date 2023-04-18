import turtle

window = turtle.Screen()
turtle.bgcolor("red")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()

for i in range (3):
 turtle.forward(300)
 turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(-350,100)
pen_color = input("Enter pen oolor: ")
fill_color = input(" Enter Fill color: ")
turtle.color(pen_color, fill_color)
turtle.begin_fill()
for i in range(3):
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.penup()
    turtle.end_fill()


window.exitonclick()
