# import colorgram
#
# rgb = []
# colors = colorgram.extract('painting.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb.append(new_colour)
#
# print(rgb)
import random
import turtle
from turtle import Turtle,Screen
color_list = [(176, 48, 79), (42, 98, 146),
              (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173),
              (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71),
              (94, 158, 65), (227, 170, 187)]
my_screen = Screen()
turtle_tim = Turtle()
turtle.colormode(255)
turtle_tim.penup()
turtle_tim.setheading(225)
turtle_tim.forward(310)
turtle_tim.setheading(0)

def make_dots():
    for po in range(10):
        turtle_tim.dot(20, random.choice(color_list))
        turtle_tim.forward(50)

for op in range(10):
    make_dots()
    turtle_tim.setheading(90)
    turtle_tim.forward(50)
    turtle_tim.setheading(180)
    turtle_tim.forward(50)
    turtle_tim.forward(500)
    turtle_tim.setheading(360)
    turtle_tim.forward(50)














my_screen.exitonclick()
