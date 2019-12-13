import turtle as tt


def forme(turtle=tt, long_base=5, angle=0, cote=3):
    turtle.right(angle)
    for x in range(cote):
        turtle.forward(long_base)
        turtle.right(-360 / cote)


def move(turtle=tt, x=None, y=None):
    turtle.up()
    if x is None:
        x = turtle.pos()[0]
    if y is None:
        y = turtle.pos()[1]
    turtle.setposition(x, y)
    turtle.down()


if __name__ == "__main__":

    pen = tt.Turtle()
    pen.width(5)
    pen.speed(40)
    pen.color('gray')
    move(pen, -400, -300)
    pen.forward(800)
    move(pen, 350, -300)
    pen.color('brown')
    pen.left(90)
    pen.forward(450)

    pen.color('green')
    for x in range(0, 6):
        forme(turtle=pen, long_base=80, angle=(-60), cote=3)

    pen.color('brown')
    move(pen, 350, -180)
    pen.right(-70)
    pen.forward(120)

    pen.color('green')
    for x in range(0, 6):
        forme(turtle=pen, long_base=60, angle=(-60), cote=3)

    pen.color('brown')
    move(pen, 350, -50)
    pen.forward(120)
    pen.color('green')
    for x in range(0, 6):
        forme(turtle=pen, long_base=60, angle=(-60), cote=3)

    pen.right(70)

    pen.color('cyan')
    move(pen, -250, 200)
    for x in range(0, 6):
        forme(turtle=pen, long_base=40, angle=(-60), cote=3)

    move(pen, -150, 120)
    for x in range(0, 6):
        forme(turtle=pen, long_base=40, angle=(-60), cote=3)

    move(pen, -100, 230)
    for x in range(0, 6):
        forme(turtle=pen, long_base=40, angle=(-60), cote=3)

    move(pen, 0, 130)
    for x in range(0, 6):
        forme(turtle=pen, long_base=40, angle=(-60), cote=3)

    move(pen, 50, 240)
    for x in range(0, 6):
        forme(turtle=pen, long_base=40, angle=(-60), cote=3)

    pen.color("yellow")
    move(pen, -300, -260)
    for x in range(0, 6):
        forme(turtle=pen, long_base=40, angle=(-60), cote=3)

    pen.color("orange")
    pen.right(35)
    pen.forward(60)
    pen.left(35)
    guidon = pen.pos()

    pen.color("yellow")
    move(pen, -176, -260)
    for x in range(0, 6):
        forme(turtle=pen, long_base=40, angle=(-60), cote=3)

    pen.color("orange")
    move(pen, -206, -210)
    pen.right(-30)
    for x in range(0, 2):
        forme(turtle=pen, long_base=60, angle=-60, cote=3)

    pen.color("red")
    pen.right(-160)
    pen.forward(25)

    pen.right(40)
    pen.backward(25)
    move(pen, guidon[0], guidon[1])
    pen.left(40)
    pen.forward(25)

    pen.ht()

    tt.done()
