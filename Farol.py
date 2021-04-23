import turtle
def farol(altura, lado, posx, posy, decremento, cor_1, cor_2, cor_3):
    # torre
    vai_para(posx, posy)
    for i in range(altura):
        # quadrado colorido
        if i % 2 == 0:
            turtle.fillcolor(cor_1)
        else:
            turtle.fillcolor(cor_2)
        turtle.begin_fill()

        for i in range(4):
            turtle.forward(lado)
            turtle.left(90)
        turtle.end_fill()
        vai_para(turtle.xcor() + decremento / 2, turtle.ycor() + lado)
        lado = lado - decremento

    # luz
    turtle.forward(lado)
    turtle.setheading(90)
    turtle.fillcolor(cor_3)
    turtle.begin_fill()
    turtle.circle(lado / 2, 180)
    turtle.end_fill()
    turtle.hideturtle()

def vai_para(posx, posy):
    #Vai para (posx, posy) sem deixar rasto.
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()

if __name__ == '__main__':
    farol(5, 100, -50, -250, 10, 'blue', 'green', 'orange')
    turtle.exitonclick()
