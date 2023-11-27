# import tkinter
# import random
#
# canvas = tkinter.Canvas(width = 600,height = 500)
# canvas.pack()
# x = 3
# xx = 3
# d = 30
# pocet = 598// d     # //dve znamenaju celociselne delenie 7//3 = 2
#
#         for i in range(pocet):
#         farba = random.choice(("green", "red", "blue", "orange"))
#
# canvas.create_rectangle(x, y, x + d, y + d, fill=farba)
#          canvas.create_line(x,y,x+d,y+d)
#         canvas.create_line(x,y+d,x+d,y)
#         x = x+d
# y = y+d
#      x = 3
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # canvas.mainloop()


import tkinter
import random


canvas = tkinter.Canvas(width = 800,height = 700)
canvas.pack()
x = 10
y = 10
d = 20
pocet = 792//d

for i in range (pocet):
        farba= random.choice(("blue","green","orange"))

canvas.create_line(x+d,y,x+2*d,y+2*d, fill = farba)
canvas.create_line(x+2*d,y+2*d,x,y+2*d, fill = farba)
canvas.create_line(x,y+2*d,x+d,y,fill = farba)
canvas.create_rectangle(x,y+2*d,x+2*d,y+4*d, fill = farba)
canvas.create_rectangle(x+2*d//4,y+5*d//2,x+3*d//2,y+7*d//2, fill= farba)
canvas.create_line(x+2*d//2,y+5*d//2,x+2*d//2,y+7*d//2)
canvas.create_line(x+2*d//4,y+6*d//2,x+3*d//2,y+6*d//2)
x = x+d
y = x+d

















canvas.mainloop()