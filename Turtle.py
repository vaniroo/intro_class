import turtle
window = turtle.Screen()
window.bgcolor("white")


def draw_square(new_turtle):
    for x in range(0, 4):
        new_turtle.pendown()
        new_turtle.right(90)
        new_turtle.forward(100)
# def draw_triangle(vanessa_turtle):
#     for x in range(0, 3):
#         vanessa_turtle.pendown()
#         vanessa_turtle.right(120)
#         vanessa_turtle.forward(60)
def draw_straight_line
    for x in range(0,3)
        vanessa_turtle.pendown()
        vanessa_turtle.right(120)
        vanessa_turtle.left(65)


def main():
    # create an instance of Turtle
    fred = turtle.Turtle()

    # set values on attributes in the Turtle module
    fred.shape("turtle")
    fred.color("green", "yellow")  # outline color, fill color
    fred.penup()
    fred.setx(150)

    # create another instance of Turtle and set its values
    ginger = turtle.Turtle()
    ginger.shape("classic")
    ginger.color("blue")
    ginger.penup()
    ginger.setx(-150)

    # draw one square filled with color with the fred instance
    fred.begin_fill()
    draw_square(fred)
    fred.end_fill()

     # create another instance of Turtle and set its values
    vanessa = turtle.Turtle()
    vanessa.shape("turtle")
    vanessa.color("black", "green")
    vanessa.penup()
    vanessa.sety(200)

    for x in range


    # draw offset squares in a loop with the ginger instance
    for x in range(0,5 ):
        draw_triangle(vanessa)
        vanessa.left(80)



    # draw offset squares in a loop with the ginger instance
    for x in range(0, 36):
        draw_square(ginger)
        ginger.right(10)

    window.exitonclick()


if __name__ == '__main__':
    main()
