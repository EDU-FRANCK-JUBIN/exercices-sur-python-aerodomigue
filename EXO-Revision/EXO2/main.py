import turtle as tt

def forme(turtle=tt, long_base=5, angle=0, cote=3 ):
    turtle.right(angle)
    for x in range(cote):
        turtle.forward(long_base)
        turtle.right(-360/cote)

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
    pen.color('red')
    pen.width(3)
    move(pen, 20)
    forme(turtle=pen, long_base=40, angle=0, cote=4)
    pen.color('green')
    move(pen, 0, 80)
    forme(turtle=pen, long_base=80, angle=0, cote=3)
    move(pen, 0,0)
    pen.color('black')
    forme(turtle=pen, long_base=80, angle=0, cote=4)

    tt.mainloop()
