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
#         canvas.create_rectangle(x,y,x+d,y+d, fill = farba)
#         canvas.create_line(x,y,x+d,y+d)
#         canvas.create_line(x,y+d,x+d,y)
#         x = x+d
#     y = y+d
#      x = 3
#
#
#
#
#
#
#
#
#
#
#
# canvas.mainloop()


import tkinter


canvas = tkinter.Canvas(width = 800,height = 700)
canvas.pack()

canvas.create_line(150,100,200,200)
canvas.create_line(200,200,100,200)
canvas.create_line(100,200,150,100)
canvas.create_rectangle(100,200,200,300)
canvas.create_rectangle(125,225,175,275)
canvas.create_line(150,225,150,275)
canvas.create_line(125,250,175,275)














canvas.mainloop()