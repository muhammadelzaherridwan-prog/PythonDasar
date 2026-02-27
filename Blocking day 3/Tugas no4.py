import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)  # Menghadap ke atas

def fibonacci_tree(panjang, depth):
    if depth == 0:
        return

    t.forward(panjang)

    t.left(30)
    fibonacci_tree(panjang * 0.7, depth - 1)

    t.right(60)
    fibonacci_tree(panjang * 0.7, depth - 1)

    t.left(30)
    t.backward(panjang)

# Posisi awal di bawah
t.penup()
t.goto(0, -250)
t.setheading(90)
t.pendown()

# Depth jangan terlalu besar!
fibonacci_tree(100, 6)

turtle.done()