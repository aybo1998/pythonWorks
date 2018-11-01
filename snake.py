import turtle as tr
from time import sleep
from random import randint

wn = tr.Screen()
wn.bgcolor("green")
wn.title("Snake Game")
wn.setup(width=580,height=580)
wn.tracer(0)

score = 0
high_score = 0

track = tr.Turtle()
track.speed(0)
track.color("white")
track.hideturtle()
track.pensize(3)
track.penup()
track.goto(-255,255)
track.down()
for i in range(4):
    track.fd(510)
    track.right(90)

score_text = tr.Turtle()
score_text.speed(0)
score_text.color("white")
score_text.hideturtle()
score_text.up()
score_text.goto(-250,260)
score_text.write("Score: {} , High Score: {}".format(score,high_score),font=("Courier", 18, "normal"))

segments = []

# snake head
snake_head = tr.Turtle()
snake_head.shape("square")
snake_head.color("red")
snake_head.speed(0)
snake_head.penup()
snake_head.direction = "stop"

# food
food = tr.Turtle()
food.shape("circle")
food.color("yellow")
food.speed(0)
food.penup()
food.y = randint(-230,230)
food.x = randint(-230,230)
food.goto(food.y,food.x)


# function to change the direction
def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

# function to move the snake
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y+20)
    elif snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y-20)
    elif snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x+20)
    elif snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x-20)

def game_over():
    sleep(1)
    snake_head.goto(0,0)
    snake_head.direction = "stop"
            
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()

    score = 0
    score_text.clear()
    score_text.write("Score: {} , High Score: {}".format(score,high_score),font=("Courier", 18, "normal"))

# events listner
wn.listen()
wn.onkey(go_up,"Up")
wn.onkey(go_down,"Down")
wn.onkey(go_right,"Right")
wn.onkey(go_left,"Left")

while True:
    wn.update()

    # when the snake eat food
    if snake_head.distance(food) < 20:
        food.y = randint(-220,220)
        food.x = randint(-220,220)
        food.goto(food.y,food.x)
        new_segment = tr.Turtle()
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        if score > high_score:
            high_score = score

        score_text.clear()
        score_text.write("Score: {} , High Score: {}".format(score,high_score),font=("Courier", 18, "normal"))

    for i in range(len(segments)-1,-1,-1):
        if i == 0 :
            snake_head.x = snake_head.xcor()
            snake_head.y = snake_head.ycor()
            segments[0].goto(snake_head.x,snake_head.y)
        else:
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x,y)
    
        
    move()

    for segment in segments:
        if segment.distance(snake_head) < 20:
            game_over()

    if (snake_head.ycor() >= 255 or \
        snake_head.xcor() >= 255  or \
        snake_head.ycor() <= -255 or \
        snake_head.xcor() <= -255):
        game_over()

    sleep(0.1)


wn.mainloop()
