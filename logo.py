import turtle 

t = turtle.Turtle()

t.color('BLACK')
t.pensize(5)
#t.speed(1)

def draw_body():
    width = 60
    height = 100

    #t.setheading(90) # start facing up

    t.right(45)
    t.forward(30)
    t.circle(14, 180)
    t.forward(55)
    t.right(45)         

    t.forward(20)
    t.circle(height / 2, 180)
    t.forward(20)

    # left arm
    
    t.right(45)
    t.forward(55)
    t.circle(14, 180)
    t.forward(50)
    t.backward(25)
    t.right(135) 

    t.forward(width / 2)
    
    t.circle(14,45)
    t.forward(85)
    t.circle(14, 175)
    t.forward(45)
    t.right(40)
    t.forward(10)

    # legs

    t.left(130)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(20)
    t.circle(14, 180)

    t.forward(20)
    t.penup()
    t.forward(35)
    t.pendown()
    t.forward(30)
    t.circle(14,50)

    t.forward(width - 10)

def draw_face():
    # Eyes
    # left eye position
    t.penup()
    t.goto(-65, 57)
    t.pendown()
    t.dot(10, "black")
    
    t.penup()
    t.goto(-48, 55)
    t.pendown()
    t.circle(13)

    # right eye position
    t.penup()
    t.goto(-26, 51) # right eye position
    t.pendown()
    t.dot(10, "black")

    t.penup()
    t.goto(-11, 55)
    t.pendown()
    t.circle(13)

    # zig-zag mouth
    t.penup()
    t.goto(-52, 28)
    t.pendown()
    t.setheading(-10)
    for _ in range(2):
        t.right(30)
        t.forward(8)
        t.left(60)
        t.forward(8)
    t.left(30)

def draw_motion(x, y, arcSize, heading):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.circle(arcSize, 40)

draw_body()
draw_face()
draw_motion(60, -18, 20, 65) # right arm
draw_motion(70, -24, 40, 65)

draw_motion(-5, -120, 30, 25) # right leg

draw_motion(-150, 2, 20, -135) # left arm
draw_motion(-157, 12, 40, -135)

t.hideturtle()

turtle.done()
