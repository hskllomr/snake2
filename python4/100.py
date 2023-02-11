import turtle
import random
import math

wn=turtle.Screen()
wn.bgcolor("red")
wn.title("Snake")

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290,310)
        self.score=0

    def update_score(self):
        self.clear()
        self.write("Score:{}".format(self.score),False,align="left",font=("Arial",20,"normal"))

    def change_score(self,points):
        self.score=self.score+points
        self.update_score()

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed=0
        self.shape("triangle")
        self.color("white")
        self.speed=1

    def move(self):
        self.forward(self.speed)

        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increaspeed(self):
        self.speed=self.speed+1

class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.speed=1
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

def iscollission(t1,t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 20:
        return True
    else:
        return False


game=Game()
ply=Player()
border=Border()
goal=Goal()
border.draw_border()

goals=[]
for count in range(6):
    goals.append(Goal())


turtle.listen()
turtle.onkey(ply.turnleft,"Left")
turtle.onkey(ply.turnright,"Right")
turtle.onkey(ply.increaspeed,"Up")
wn.tracer(0)

while True:
    wn.update()
    ply.move()

    for goal in goals:
        goal.move()

        if iscollission(ply,goal):
            goal.jump()
            game.change_score(10)

















