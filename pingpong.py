import os
import turtle

# Vytvoření obrazovky
screen_1 = turtle.Screen()
screen_1.title("Ping-Pong")
screen_1.bgcolor("white")
screen_1.setup(width=1050, height=650)

# Levý paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("Red")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# Pravý paddle


# Míček
hit_ball = turtle.Turtle()
hit_ball.speed(45)
hit_ball.shape("circle")
hit_ball.color("Black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Iniciální scóre
left_player = 0
right_player = 0

#Pozice
sketch_x = turtle.Turtle()
sketch_x.speed(0)
sketch_x.color("blue")
sketch_x.penup()
sketch_x.hideturtle()
sketch_x.goto(0, 460)

# Zobrazení skóre
sketch_1 = turtle.Turtle()
sketch_1.speed(0)
sketch_1.color("blue")
sketch_1.penup()
sketch_1.hideturtle()
sketch_1.goto(0, 260)
sketch_1.write("Levý hráč R/C : 0    Pravý hráč šipky: 0",
               align="center", font=("Courier", 20, "normal"))


# Funkce pro vertikální pohyb paddlu
def paddle_L_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def paddle_L_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)



# Pohyb klávesnicí
screen_1.listen()
screen_1.onkeypress(paddle_L_up, "r")
screen_1.onkeypress(paddle_L_down, "c")
# Klávesa nahoru Up, klávesa dolů Down

while True:
    # Aktualizace
    screen_1.update()

    # Iniciální pozice středu míčku
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)


    # Kontrola ohraničení
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    #if..



    # Detekce vítěze dle pozice
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch_1.clear()
        sketch_1.write("Levý hráč : {}    Pravý hráč: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 20, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch_1.clear()
        sketch_1.write("Levý hráč : {}    Pravý hráč: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 20, "normal"))

    #if..


    #Pomůcka - do konzole souřadnice kuličky
    #print("Right: "+str(right_paddle.ycor()) + " Left: "+str(left_paddle.ycor()) + "Koule:" + str(hit_ball.xcor()) + "x" + str(hit_ball.ycor()))



    # Kolize kuličky a paddle
    if (hit_ball.xcor() > 360 and
        hit_ball.xcor() < 370) and (hit_ball.ycor() < right_paddle.ycor() + 70 and
                                    hit_ball.ycor() > right_paddle.ycor() - 70):
        hit_ball.setx(360)
        hit_ball.dx *= -1

