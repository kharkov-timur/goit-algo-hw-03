import turtle


def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)


def draw_snowflake(t, length, depth):
    for i in range(3):
        koch_curve(t, length, depth)
        t.right(120)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    length = 300
    depth = int(input("Введіть рівень рекурсії: "))

    t.penup()
    t.goto(-length / 2, length / 2)
    t.pendown()

    draw_snowflake(t, length, depth)

    turtle.done()
