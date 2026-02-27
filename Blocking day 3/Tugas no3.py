import turtle

t = turtle.Turtle()
t.speed(0)

def persegi(panjang, lebar, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(2):
        t.forward(panjang)
        t.right(90)
        t.forward(lebar)
        t.right(90)
    t.end_fill()

# Posisi awal
t.penup()
t.goto(-150, 100)
t.setheading(0)
t.pendown()

# Bagian merah
persegi(300, 100, "red")

# Turun untuk bagian putih
t.right(90)
t.forward(100)
t.left(90)

# Bagian putih
persegi(300, 100, "white")

turtle.done()