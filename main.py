import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
# the screen
wn = turtle.Screen()
wn.title("Snake Game by @Deathplay")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# the head
myboy = turtle.Turtle()
myboy.speed(0)
myboy.shape("square")
myboy.color("light blue")
myboy.penup()
myboy.goto(0, 0)
myboy.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 0)

body = []

# Scoring
pen = turtle.Turtle()
pen.goto(0, 260)
pen.shape("square")
pen.color("Red")
pen.penup()
pen.hideturtle()
pen.write("Score:0  High Score:0", align="center", font=("Times New Roman", 20, "bold"))


# functions
def go_up():
    if myboy.direction != "down":
        myboy.direction = "up"


def go_down():
    if myboy.direction != "up":
        myboy.direction = "down"


def go_left():
    if myboy.direction != "right":
        myboy.direction = "left"


def go_right():
    if myboy.direction != "left":
        myboy.direction = "right"


def move():
    if myboy.direction == "up":
        y = myboy.ycor()
        myboy.sety(y + 20)
    if myboy.direction == "down":
        y = myboy.ycor()
        myboy.sety(y - 20)
    if myboy.direction == "left":
        x = myboy.xcor()
        myboy.setx(x - 20)
    if myboy.direction == "right":
        x = myboy.xcor()
        myboy.setx(x + 20)


# keyboard bindings

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:

    wn.update()
    # wall clash
    if myboy.xcor() > 290 or myboy.xcor() < -290 or myboy.ycor() > 290 or myboy.ycor() < -290:
        time.sleep(0.5)
        myboy.goto(0, 0)
        myboy.direction = "stop"
        for bodies in body:
            bodies.goto(1000, 1000)
        body.clear()
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                  font=("Times New Roman", 20, "bold"))

    if myboy.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # new body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.colour = ("black")
        new_body.penup()
        body.append(new_body)

        # Score
        score += 10
        if high_score < score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                  font=("Times New Roman", 20, "bold"))

    # attatching body
    for index in range(len(body) - 1, 0, -1):
        body[index].goto(body[index - 1].xcor(), body[index - 1].ycor())
    # for 0th segment
    if len(body) > 0:
        body[0].goto(myboy.xcor(), myboy.ycor())

    move()
    # body eating
    for bodies in body:
        if bodies.distance(myboy) < 20:
            time.sleep(1)
            myboy.goto(0, 0)
            myboy.direction = "stop"
            for bodies in body:
                bodies.goto(1000, 1000)
            body.clear()
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Times New Roman", 20, "bold"))

    time.sleep(delay)

wn.mainloop()