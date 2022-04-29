import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(10):
    r = random.randint(1, 200)
    a = random.randint(1, 200)
    
    cc = (a, a)
    t.up()
    t.goto(cc)
    t.down()
    t.circle(r)

turtle.done()