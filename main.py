import tkinter
import random
canvas = tkinter.Canvas(width = 800,height = 700)
canvas.pack()
x= 20
y= 20
d= 30
vyfarbenie  = random.choice(("blue","red","dark red","dark blue","sky blue"))
canvas.create_rectangle(x,y,x+d,y+d,fill = vyfarbenie)
canvas.create_rectangle(x,y+d,x+d,y+2*d,fill = vyfarbenie)
canvas.create_rectangle(x,y+2*d,x+d,y+3*d,fill = vyfarbenie)
canvas.create_rectangle(x,y+3*d,x+d,y+4*d,fill = vyfarbenie)
canvas.create_rectangle(x,y+4*d,x+d,y+5*d,fill = vyfarbenie)
canvas.create_rectangle(x,y+5*d,x+d,y+6*d,fill = vyfarbenie)
canvas.create_rectangle(x,y+6*d,x+d,y+7*d,fill = vyfarbenie)
canvas.create_rectangle(x+d,y+6*d,x+2*d,y+7*d,fill = vyfarbenie)
canvas.create_rectangle(x+2*d,y+6*d,x+3*d,y+7*d,fill = vyfarbenie)
canvas.create_rectangle(x+3*d,y+6*d,x+4*d,y+7*d,fill = vyfarbenie)
canvas.create_rectangle(x+4*d,y+6*d,x+5*d,y+7*d,fill = vyfarbenie)
canvas.create_rectangle(x+7*d,y+d,x+8*d,y+2*d,fill = vyfarbenie )


# it s very hard















canvas.mainloop()
