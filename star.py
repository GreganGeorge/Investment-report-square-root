import turtle
import random
t=turtle.Turtle()
def star(length):
    colors=["green","red","purple","black","blue","orange","cyan"]
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    for side in range(5):
        t.forward(length)
        t.right(120)
        t.forward(length)
        t.left(48)
    t.end_fill()
def pattern(n,length):
    for count in range(n):
        star(length)
        t.left(360/n)
        
