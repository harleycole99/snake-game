from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.clearscreen()
screen.bgcolor("green yellow")
screen.title("Snake Game")
screen.tracer(0)

marker = Turtle()
marker.hideturtle()

screen.update()

screen.exitonclick()
