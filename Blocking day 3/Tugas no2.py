import turtle

t = turtle.Turtle()
t.speed(0)

# ========================
# FUNCTION BANGUN DATAR
# ========================

def persegi_panjang(p, l, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(2):
        t.forward(p)
        t.right(90)
        t.forward(l)
        t.right(90)
    t.end_fill()

def segitiga(s, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(3):
        t.forward(s)
        t.left(120)
    t.end_fill()

def trapezium():
    t.fillcolor("green")
    t.begin_fill()
    t.forward(120)
    t.right(60)
    t.forward(80)
    t.right(120)
    t.forward(120)
    t.right(60)
    t.forward(80)
    t.end_fill()

def jajar_genjang(p, l, warna):
    t.fillcolor(warna)
    t.begin_fill()
    t.forward(p)
    t.right(60)
    t.forward(l)
    t.right(120)
    t.forward(p)
    t.right(60)
    t.forward(l)
    t.end_fill()

def segilima(s, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(5):
        t.forward(s)
        t.right(72)
    t.end_fill()


# ========================
# GAMBAR
# ========================

t.penup()
t.goto(-250, 100)
t.setheading(0)
t.pendown()
persegi_panjang(120, 60, "red")

t.penup()
t.goto(-50, 100)
t.setheading(0)
t.pendown()
segitiga(100, "yellow")

t.penup()
t.goto(150, 100)
t.setheading(0)
t.pendown()
trapezium()

t.penup()
t.goto(-150, -100)
t.setheading(0)
t.pendown()
jajar_genjang(120, 70, "blue")

t.penup()
t.goto(100, -100)
t.setheading(0)
t.pendown()
segilima(80, "purple")

turtle.done()