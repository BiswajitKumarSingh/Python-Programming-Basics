import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

my_turtle = turtle.Turtle()
my_turtle.color("red")          # make tess blue
my_turtle.pensize(0)            # set the width of her pen
my_turtle.speed(100)
my_turtle.align="Right"

def square(length, angle):
    for i in range(5):
        my_turtle.forward(length)
        my_turtle.right(angle)
        
for i in range(70):
     square(200,80)
     my_turtle.right(11)
    
wn=turtle.Screen()
wn.bgcolor('black')
my_turtle.pendown()
turtle=turtle.Turtle()
wn.exitonclick()
