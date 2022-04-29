import turtle
t = turtle.Turtle()
t.shape("turtle")

a = input("직선값 : ")
d = int(input("작은직선값 : "))
s = int(input("각도 : "))

a = int(a)

for i in range(10):
    t.forward(a); t.right(s); t.forward(d); t.right(s); t.forward(a); t.left(s); t.forward(d); t.left(s)

turtle.done()