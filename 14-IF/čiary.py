import tkinter
canvas = tkinter.Canvas(width =500, height = 500, bg =  "white")
canvas.pack()
x = 10
y = 10
d = 15
farba1 = "blue"
farba2 = "red"
pocet = (500//d)
for j in range(pocet):

    canvas.create_line(x,y,x,y*50,fill = farba1)
    x = x+d

for i in range(pocet):
    canvas.create_line(0,y,500,y,fill = farba2)
    y = y+d





canvas.mainloop()