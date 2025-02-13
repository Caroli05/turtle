import turtle as Turtle

dibujarCuadrado = Turtle.Turtle()

def miCuadrado():
    dibujarCuadrado.penup()
    dibujarCuadrado.goto(40, -45)
    dibujarCuadrado.pendown()

    for i in range(4):
        dibujarCuadrado.forward(100)
        dibujarCuadrado.left(90)

def miCudrado2():
    dibujarCuadrado.penup()
    dibujarCuadrado.goto(-50, 50)
    dibujarCuadrado.pendown()

    for i in range(4):
        dibujarCuadrado.forward(100)
        dibujarCuadrado.left(90)

def unirCuadrados():
    esquina1 = (40, -45)

    # Mover a la primera esquina
    dibujarCuadrado.penup()
    dibujarCuadrado.goto(esquina1)
    dibujarCuadrado.pendown()

    dibujarCuadrado.setheading(133)
    dibujarCuadrado.forward(130)

    dibujarCuadrado.setheading(0)
    dibujarCuadrado.forward(100)

    dibujarCuadrado.setheading(-47)
    dibujarCuadrado.forward(132)

    dibujarCuadrado.penup()
    dibujarCuadrado.setheading(90)
    dibujarCuadrado.forward(100)
    dibujarCuadrado.pendown()

    dibujarCuadrado.setheading(134)
    dibujarCuadrado.forward(135)

    dibujarCuadrado.penup()
    dibujarCuadrado.setheading(180)
    dibujarCuadrado.forward(100)
    dibujarCuadrado.pendown()

    dibujarCuadrado.setheading(-45)
    dibujarCuadrado.forward(135)


miCuadrado()
miCudrado2()
unirCuadrados()
input('hola')