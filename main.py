from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My snake game")

ranges = [(0,0),(-20,0),(20,0)]
for range in ranges:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(range)





















screen.exitonclick()

