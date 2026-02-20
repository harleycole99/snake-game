from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green yellow")
screen.title("Snake Game")
screen.tracer(0)


segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


# Adding Segments Function
def add_segments(position):
    new_segment = Turtle("square")
    new_segment.color("black")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


for position in starting_positions:
    add_segments(position)

screen.update()


screen.exitonclick()
