import turtle

t = turtle.Turtle()
t.speed(3)

def persegi_panjang(panjang, lebar):
    for i in range(2):
        t.forward(panjang)
        t.right(90)
        t.forward(lebar)
        t.right(90)

def segitiga(sisi):
    for i in range(3):
        t.forward(sisi)
        t.left(120)

def trapezium(a, b, tinggi):
    t.forward(a)
    t.left(120)
    t.forward(tinggi)
    t.right(120)
    t.forward(b)
    t.right(120)
    t.forward(tinggi)
    t.right(120)

def jajar_genjang(panjang, lebar):
    t.forward(panjang)
    t.left(60)
    t.forward(lebar)
    t.left(120)
    t.forward(panjang)
    t.left(60)
    t.forward(lebar)

def belah_ketupat(sisi):
    for i in range(2):
        t.forward(sisi)
        t.left(60)
        t.forward(sisi)
        t.left(120)

persegi_panjang(100,50)
t.penup(); t.goto(150,0); t.pendown()
segitiga(100)
t.penup(); t.goto(-150,0); t.pendown()
trapezium(120,60,80)
t.penup(); t.goto(0,-150); t.pendown()
jajar_genjang(100,60)
t.penup(); t.goto(-150,-150); t.pendown()
belah_ketupat(80)

turtle.done()