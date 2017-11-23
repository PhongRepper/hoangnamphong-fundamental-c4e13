from turtle import *
shape("turtle")
def draw_square(length, colo):
    speed(-1)
    color(colo)
    for i in range(4):
        forward(length)
        left(90)
    mainloop()
