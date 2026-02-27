import turtle

# Buat turtle baru
t = turtle.Turtle()
t.speed(0)
t.color("green")

def matahari():
    for i in range(36):
        t.circle(100)
        t.right(10)

matahari()

turtle.done()