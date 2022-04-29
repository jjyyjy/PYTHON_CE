import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

list = ["yellow", "red", "blue", "green"]
list2 = [50, 25, 40, 100, 300]

cl = random.randint(0, 3)
r = random.randint(0, 4)

t.fillcolor(list[cl])
t.begin_fill()
t.circle(list2[r])
t.end_fill()

turtle.done()