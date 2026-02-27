import turtle
import math

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ===== Fungsi membuat lingkaran =====
def draw_circle(radius, color_fill, color_outline, width=3):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.pensize(width)
    t.color(color_outline, color_fill)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# ===== Lingkaran luar =====
draw_circle(200, "white", "black", 5)

# ===== Lingkaran biru dalam =====
draw_circle(150, "#2b3b73", "black", 3)

# ===== Teks melingkar atas =====
def draw_text_circle(text, radius, start_angle):
    angle = start_angle
    for char in text:
        t.penup()
        t.setheading(0)
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(radius)
        t.setheading(angle + 90)
        t.write(char, align="center", font=("Arial", 14, "bold"))
        angle -= 360 / len(text)

# Teks atas
draw_text_circle("SEKOLAH MENENGAH KEJURUAN", 175, 110)

# Teks bawah
draw_text_circle("PRESTASI PRIMA", 175, -70)

# ===== Bintang kiri =====
t.penup()
t.goto(-160, 0)
t.pendown()
t.color("black")
t.write("★", align="center", font=("Arial", 20, "bold"))

# ===== Bintang kanan =====
t.penup()
t.goto(160, 0)
t.pendown()
t.write("★", align="center", font=("Arial", 20, "bold"))

# ===== Gambar tangan sederhana =====
t.penup()
t.goto(0, -60)
t.setheading(90)
t.pendown()
t.color("red", "red")
t.begin_fill()

# Telapak
t.forward(120)
t.right(90)
t.forward(40)
t.right(90)
t.forward(120)
t.right(90)
t.forward(40)

t.end_fill()

# Jari telunjuk
t.penup()
t.goto(0, 60)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(70)
t.right(90)
t.forward(25)
t.right(90)
t.forward(70)
t.right(90)
t.forward(25)
t.end_fill()

turtle.done()