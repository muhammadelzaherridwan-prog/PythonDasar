# Program Python menggambar pola menggunakan Turtle

import turtle
import time
import random

print("Program ini menggambar bangun berdasarkan jumlah sisi yang kamu masukkan.")
num_str = input("Masukkan jumlah sisi bangun yang ingin digambar: ")

if num_str.isdigit():
    squares = int(num_str)
else:
    print("Masukkan angka yang benar!")
    exit()

# Sudut luar poligon
angle = 360 / squares

turtle.speed(0)
turtle.penup()
turtle.setpos(0, 0)

numshapes = 8

for n in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    turtle.forward(10 * n)
    turtle.left(15)

    turtle.pendown()
    turtle.begin_fill()

    for i in range(squares):
        turtle.forward(40)
        turtle.left(angle)

    turtle.end_fill()
    turtle.penup()

time.sleep(5)
turtle.bye()