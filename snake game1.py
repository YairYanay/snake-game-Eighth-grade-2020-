#snake game by yair yanay kfar yona


import turtle
import time
import random
from tkinter import *



def open():
    delay = 0.1

    # Score
    score = 0
    high_score = 0

     # setup the screen

    windows = turtle.Screen()
    windows.title("                                                    SNAKE BAM BY YAIR YANAY KFAR YONA")
    windows.bgcolor("green")
    windows.setup(width=600, height=600)
    windows.tracer(0)  # screen updates


    # snake
    t = turtle.Turtle()
    t.speed(0)
    t.shape("square")
    t.color("black")
    t.penup()
    t.goto(0, 0)
    t.direction = "stop"


    # snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    body = []

    # pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0 High score: 0", align="center", font=("Courier", 24, "normal"))

    # Functions
    def go_up():
        if t.direction != 'down':
            t.direction = 'up'

    def go_down():
        if t.direction != 'up':
            t.direction = 'down'

    def go_left():
        if t.direction != 'right':
            t.direction = 'left'

    def go_right():
        if t.direction != 'left':
            t.direction = 'right'

    def move():
        if t.direction == "up":
            y = t.ycor()
            t.sety(y + 20)

        if t.direction == "down":
            y = t.ycor()
            t.sety(y - 20)

        if t.direction == "left":
            x = t.xcor()
            t.setx(x - 20)

        if t.direction == "right":
            x = t.xcor()
            t.setx(x + 20)

    # keyboard
    windows.listen()
    windows.onkeypress(go_up, 'Up')
    windows.onkeypress(go_down, 'Down')
    windows.onkeypress(go_left, 'Left')
    windows.onkeypress(go_right, 'Right')

    while True:
        windows.update()

        # dont go over the corners
        if t.xcor() > 290 or t.xcor() < -290 or t.ycor() > 290 or t.ycor() < -290:
            time.sleep(1)
            t.goto(0, 0)
            t.direction = 'stop'

            # hide the body
            for new_body in body:
                new_body.goto(1000, 1000)

            # clear the body list
            body.clear()

            # Reset the score
            score = 0

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        if t.distance(food) < 20:
            # move the food
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # add a new body
            new_body = turtle.Turtle()
            new_body.speed(0)
            new_body.shape("square")
            new_body.color('gray')
            new_body.penup()
            body.append(new_body)

            # the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # move body add
        for index in range(len(body) - 1, 0, -1):
            x = body[index - 1].xcor()
            y = body[index - 1].ycor()
            body[index].goto(x, y)

        # move body 0 to the head
        if len(body) > 0:
            x = t.xcor()
            y = t.ycor()
            body[0].goto(x, y)

        move()

        # her body to her body
        for new_body in body:
            if new_body.distance(t) < 20:
                time.sleep(1)
                t.goto(0, 0)
                t.direction = 'stop'
                score = 0
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

                # hide the body
                for new_body in body:
                    new_body.goto(1000, 1000)

                # clear the body list
                body.clear()

        time.sleep(delay)

    windows.mainloop()





def sucssec():
    Label(screen1, text="Log in Sucess", fg="green", font=("calibri", 11)).pack()
    for i in range(1):
        #start button and exit
        button_S = Tk()
        button_S.title("SNAKE GAME")
        Label(button_S, text="SNAKE BAM", font="Times 30 bold underline").pack()
        Label(button_S, text="BY YAIR YANAY", font="Helvetica 18 italic").pack()
        Label(button_S, text="welcome", font="Helvetica 18 italic").pack()
        Label(button_S, text=username.get(), font="Helvetica 18 italic").pack()
        start_Botton = Button(button_S, text="start", command=open).pack()
        button_S.geometry("350x350+200+250")
        exit_button = Button(button_S, text="exit", command=quit).pack()
        button_S.mainloop()


def error():
    Label(screen1, text="No text write! Try Again", fg="red", font=("calibri", 11)).pack()
    #Button(screen1, text="OK", command=delete).pack()





def CheckNotUserWrite():
    username_info = username.get()
    if  username_info == "":
                error()
    else:
        sucssec()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global username_entry
    username = StringVar()

    global password
    global password_entry
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    #password
    Label(screen1, text="password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()

    Label(screen1, text="").pack()
    Button(screen1, text="Submit", width=10, height=1, command=CheckNotUserWrite).pack()

def Login():
    global screen1
    Loginscreen = Toplevel(screen)
    Loginscreen.title("Login")
    Loginscreen.geometry("300x250")





def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Register")
    Label(text="Login system", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=register).pack()
    Label(text="", height="1", width="1").pack()
    Button(text="Register", height="2", width="30", command=Login).pack()
    Label(text="", height="1", width="1").pack()
    exit_button = Button(screen, text="exit", command=quit).pack()
    screen.mainloop()



main_screen()

















