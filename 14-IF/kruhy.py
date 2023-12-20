import tkinter
canvas_width = 500
canvas_height = 500


canvas = tkinter.Canvas(width = canvas_width,height = canvas_height)
canvas.pack()
x = 10
y = 10
d = 20
xx = x


for j in range(498): # má na starosť riadky
    for i in range(498):
        canvas.create_oval(x,y,x+d,y+d,fill = "blue")

        x = x+d
    y = y+d
    x = xx










canvas.mainloop()