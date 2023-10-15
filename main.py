import turtle
from turtle import Screen, Turtle
from random import randint
import time

SMALL_FONT = ('Arial', 15, 'normal')
MEDIUM_FONT = ('Arial', 30, 'normal')
LARGE_FONT = ('Arial', 50, 'normal')

# Portal
def change_position():
    target.hideturtle()
    x = randint(-300, 300)
    y = randint(-300, 300)
    target.goto(x, y)
    target.showturtle()

score = 0
# Score
def update_score():
    global score
    score += 1
    score_keeper.clear()
    score_keeper.write('Score: {} '.format(score), align='center', font=MEDIUM_FONT)


#Süre
seconds = 0
def update_time():
    time_keeper.undo()
    time_keeper.write(seconds, align= 'center', font=LARGE_FONT)

#Tıklama olayı
def target_clicked(x,y):
    if seconds > 0:
        update_score()
        change_position()

def action():
    global seconds

    seconds -= 1

    if seconds <=0:
        target.hideturtle()

        time_keeper.clear()
        time_keeper.sety(320)
        time_keeper.write("Time Over", align='center', font=MEDIUM_FONT)
    else:
        update_time()
        screen.ontimer(action , 1000) #1 seconds 1000 milliseconds




# Screen

screen = turtle.Screen()
screen.bgcolor("Light Blue")
screen.setup(width=800 ,height=800)
screen.title("Catch The Turtle")
screen.addshape("ezgif.com-resize.gif")

draw_playground = turtle.Turtle()

draw_playground.speed(0)

draw_playground.shape("turtle")

draw_playground.color("black")

draw_playground.penup()

draw_playground.hideturtle()

draw_playground.goto(310, 310)

draw_playground.pendown()

draw_playground.goto(-310, 310)

draw_playground.goto(-310, -310)

draw_playground.goto(310, -310)

draw_playground.goto(310, 310)

draw_playground.penup()


#Target
target = Turtle()
target.penup()
target.setposition(randint(-300,300),randint(-300,300))
target.shape("ezgif.com-resize.gif")

#Score
score_keeper = Turtle()
score_keeper.hideturtle()
score_keeper.penup()
score_keeper.sety(-400)


#Time

seconds = int(screen.numinput("Timer","Enter the seconds",minval=0,maxval=59))

time_keeper = score_keeper.clone()

time_keeper.sety(370)
time_keeper.write("Time Left: ", align='center',font=SMALL_FONT)
time_keeper.sety(300)
time_keeper.write(seconds , align='center', font=LARGE_FONT)

target.onclick(target_clicked)


action()

screen.mainloop()
