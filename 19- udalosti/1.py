# import tkinter
# import random
#
#
# def vypis():
#     text = "PYTHON"
#     x = random.randrange(50,330)
#     y = random.randrange(20,24)
#     canvas.create_text(x,y, text= text ,font="arial 20")
#
# def zmaz():
#     canvas.delete("all")
#
#
# canvas = tkinter.Canvas()
# canvas.pack()
# tkinter.Button(text= "Vypíš text", command=vypis).pack()
# tkinter.Button(text="Zmaž plochu",command= zmaz).pack()
#
# vstup = tkinter.Entry(width = 10)
# vstup.pack()
#
#
#
#
#
# canvas.mainloop()




# import tkinter
#
# def klik(event):
#     canvas.create_line(100, 200, event.x, event.y)
#
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.bind('<ButtonPress>', klik)
#
# tkinter.mainloop()




# import tkinter
# import random
#
# def klik(event):
#     x, y = event.x, event.y
#     for r in range(50, 0, -5):
#         farba = f'#{random.randrange(256**3):06x}'
#         canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)
#
# canvas = tkinter.Canvas(width = 1000,height = 1000)
# canvas.pack()
# canvas.bind('<ButtonPress>', klik)
#
# tkinter.mainloop()


#
# import tkinter
#
#
# def ťahaj(udalost):
#     x,y = udalost.x,udalost.y
#     canvas.create_oval(x-10,y-10,x+10,y+10,fill = "blue")
#
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.bind("<Motion>", ťahaj)
#
# tkinter.mainloop()



#
# import tkinter,random
# zoznam=[]
#
# def klik(udalost):
#     global poly
#     zoznam[:]= [udalost.x,udalost.y]
#     farba = f"#{random.randrange(256**3):06x}"
#     poly = canvas.create_polygon(0,0,0,0,fill = farba)
#
#
# def ťahaj(udalost):
#     zoznam.extend([udalost.x,udalost.y])
#     canvas.coords(poly,zoznam)
#
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.bind("<ButtonPress>",klik)
# canvas.bind("<B1-Motion>", ťahaj)
#
#
#
# canvas.mainloop()





import tkinter

def klik(event):
    global xx, yy
    xx, yy = event.x, event.y

def tahaj(event):
    canvas.create_line(xx, yy, event.x, event.y)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)
canvas.bind('<B1-Motion>', tahaj)

tkinter.mainloop()