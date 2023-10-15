import turtle
from turtle import Screen, Turtle
from random import randint

SMALL_FONT = ('Arial', 15, 'normal')
MEDIUM_FONT = ('Arial', 30, 'normal')
LARGE_FONT = ('Arial', 50, 'normal')


def change_position():
    target.hideturtle()
    x = randint(-300, 300)
    y = randint(-300, 300)
    target.goto(x, y)
    target.showturtle()


score = 0


def update_score():
    global score
    score += 1
    score_keeper.clear()
    score_keeper.write(score, align='center', font=SMALL_FONT)


def update_time():
    time_keeper.undo()
    time_keeper.write(seconds, align='center', font=LARGE_FONT)


def target_clicked(x, y):
    if seconds > 0:
        update_score()
        change_position()


def action():
    global seconds

    seconds -= 1

    if seconds <= 0:
        target.hideturtle()

        time_keeper.clear()
        time_keeper.sety(320)
        time_keeper.write("Time Over", align='center', font=MEDIUM_FONT)
    else:
        update_time()
        my_screen.ontimer(action, 1000)  # 1 seconds 1000 milliseconds


# Screen

my_screen = turtle.Screen()
my_screen.bgcolor("Light Blue")
my_screen.title("Catch The Turtle")
my_screen.addshape("ezgif.com-resize.gif")

target = Turtle()
target.penup()
target.setposition(randint(-300, 300), randint(-300, 300))
target.shape("ezgif.com-resize.gif")

score_keeper = Turtle()
score_keeper.hideturtle()
score_keeper.penup()
score_keeper.sety(-300)

seconds = int(my_screen.numinput("Timer", "Enter the seconds", minval=0, maxval=59))

time_keeper = score_keeper.clone()

time_keeper.sety(370)
time_keeper.write("Time Left: ", align='center', font=SMALL_FONT)
time_keeper.sety(300)
time_keeper.write(seconds, align='center', font=LARGE_FONT)

target.onclick(target_clicked)

action()

my_screen.mainloop()
