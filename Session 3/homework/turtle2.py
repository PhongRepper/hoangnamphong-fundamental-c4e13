from turtle import *
speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# for n in range(6):
for n in range(5):
    # color(colors.pop(1))
    color(colors.pop(0))
    begin_fill()
    for i in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    forward(100)
    end_fill()
    # forward(150)
    # left(90)
    # forward(100)
    # left(90)
    # forward(150)

mainloop()
