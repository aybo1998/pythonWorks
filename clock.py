import turtle as tr
from time import sleep
from datetime import datetime 

wn = tr.Screen()
wn.title("AyBo Clock !!")
wn.screensize(202,202)
wn.setup(210,210)
wn.bgcolor("black")
wn.tracer(0)

clock = tr.Turtle()
clock.hideturtle()
clock.color("white")
clock.pensize(2)

# Draw the circle
clock.up()
clock.goto(0,-100)
clock.down()
clock.circle(100)
clock.up()

# Draw the lines for the hours
clock.goto(0,0)
clock.seth(90)

for _ in range(12):
    clock.fd(78)
    clock.down()
    clock.fd(20)
    clock.up()
    clock.goto(0,0)
    clock.rt(30)

pen = tr.Turtle()
pen.hideturtle()
pen.color("white")
pen.pensize(2)

while True:
    # Get time
    now = datetime.now()
    h = now.hour
    m = now.minute
    s = now.second

    # Draw the hour hand
    pen.goto(0,0)
    pen.seth(90)
    angle = (360/12)*h
    pen.right(angle)
    pen.down()
    pen.color("gray")
    pen.fd(50)
    pen.up()

    # Draw the minute hand
    pen.goto(0,0)
    pen.seth(90)
    angle = (m/60)*360
    pen.right(angle)
    pen.down()
    pen.color("red")
    pen.fd(50)
    pen.up()

    # Draw the second hand
    pen.goto(0,0)
    pen.seth(90)
    angle = (s/60)*360
    pen.right(angle)
    pen.down()
    pen.color("yellow")
    pen.fd(50)
    pen.up()
    wn.update()
    sleep(1)
    pen.clear()
    
wn.mainloop()
