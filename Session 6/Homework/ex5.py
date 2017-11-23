from turtle import *
shape('turtle')

def draw_star(x, y, length):
    # speed(-1)
    penup()
    goto(x, y)
    for i in range(5):
        pendown()
        forward(length)
        right(144)
        penup()
    mainloop()
# x = 4
# y = 5
# length = 100
# draw_star(x, y, length)
