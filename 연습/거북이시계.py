import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.stamp()
move = 30

for i in range(12):
    t.up()
    t.forward(50)
    t.down()
    t.forward(25)
    t.up()
    t.forward(15)
    t.stamp()
    t.home()
    t.right(move)
    move += 30

turtle.done()