import turtle 

t = turtle.Turtle()

t.color('RED')
t.pensize(5)

for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()
t.forward(150)
t.pendown()
t.circle(15)

turtle.done()
