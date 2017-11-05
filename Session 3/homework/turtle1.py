from turtle import *
speed(-1)
# colors = ['red', 'blue', 'orange', 'yellow','grey']
# n = int(input("How many edge? "))
# speed(-1)
# for i in range(3, n+1):
#
#     for _ in range(i):
#         color = 'red'
#         forward(100)
#         left(360/i)
# mainloop()
color = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(3,8):
    for _ in range(i):
        EdgeColor = i - 3
        pencolor(color[EdgeColor])
        forward(100)
        left(360/i)


mainloop()
