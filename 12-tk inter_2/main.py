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


# import tkinter
# import random
#
#
# canvas = tkinter.Canvas(width = 1200,height = 600)
# canvas.pack()
# x = 10
# y = 10
# d = 20
# xx = x
# pocet = 1198//d
# for j in range (598//d):
#         for i in range (pocet):
#                 farba= random.choice(("blue","green","orange"))
#
# canvas.create_line(x+d,y,x+2*d,y+2*d, fill = farba)
# canvas.create_line(x+2*d,y+2*d,x,y+2*d, fill = farba)
# canvas.create_line(x,y+2*d,x+d,y,fill = farba)
# canvas.create_rectangle(x,y+2*d,x+2*d,y+4*d,width = 2, fill = farba)
# canvas.create_rectangle(x+2*d//4,y+5*d//2,x+3*d//2,y+7*d//2,width = 2, fill= farba)
# canvas.create_line(x+2*d//2,y+5*d//2,x+2*d//2,y+7*d//2,width = 2)
# canvas.create_line(x+2*d//4,y+6*d//2,x+3*d//2,y+6*d//2,width = 2)
# x = x + d
# y = y + d + d // 2
# x = xx
#
# canvas.mainloop()











import tkinter
import random

cv = tkinter.Canvas(width=800, height=600,)
cv.pack()

x = 10
y = 10
d = 20
pocet = 798 // d
xx = x

for j in range(598 // d):
    for i in range(pocet):
        farba = random.choice(("green", "red", "blue", "orange", "purple", "yellow","dark blue","brown"))
        cv.create_rectangle(x,y+d//2,x+d,y+d+d//2,fill=farba)
        cv.create_polygon(x,y+d//2,x+d//2,y,x+d,y+d//2,fill="brown",outline="black")
        cv.create_rectangle(x+d//4,y+d//4+d//2,x+d//4*3,y+d//4*3+d//2,width=2,fill="sky blue")
        cv.create_line(x+d//2,y+d//4+d//2,x+d//2,y+d//4*3+d//2,width=2)
        cv.create_line(x+d//4,y+d,x+d//4+d//2,y+d,width=2)
        x = x + d
    y = y + d + d//2
    x = xx


tkinter.mainloop()


