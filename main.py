import tkinter
import random
canvas = tkinter.Canvas(width = 950,height = 700)
canvas.pack()
x= 20
y= 20
d= 30
vyfarbenie  = random.choice(("blue","red","dark red","dark blue","sky blue"))
c = "darkblue"
m = "brown"
g = "lightblue"
j = "blue3"
e = "#3d84df"
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
canvas.create_rectangle(x+6*d,y,x+7*d,y+d,fill = c)
canvas.create_rectangle(x+6*d,y+d,x+7*d,y+2*d, fill = c)
canvas.create_rectangle(x+6*d,y+2*d,x+7*d,y+3*d,fill = c)
canvas.create_rectangle(x+6*d,y+3*d,y+7*d,y+4*d,fill=  c)
canvas.create_rectangle(x+6*d,y+4*d,y+7*d,y+5*d,fill = c)
canvas.create_rectangle(x+7*d,y+5*d,y+8*d,y+6*d,fill = c)
canvas.create_rectangle(x+8*d,y+6*d,x+9*d,y+7*d,fill = c)
canvas.create_rectangle(x+9*d,y+6*d,x+10*d,y+7*d,fill = c)
canvas.create_rectangle(x+10*d,y+6*d,x+11*d,y+7*d,fill = c)
canvas.create_rectangle(x+11*d,y+5*d,x+12*d,y+6*d,fill =c)
canvas.create_rectangle(x+12*d,y+4*d,x+13*d,y+5*d,fill =c)
canvas.create_rectangle(x+12*d,y+3*d,x+13*d,y+4*d,fill =c)
canvas.create_rectangle(x+12*d,y+2*d,x+13*d,y+3*d,fill =c)
canvas.create_rectangle(x+12*d,y+d,x+13*d,y+2*d, fill =c)
canvas.create_rectangle(x+12*d,y,x+13*d,y+d, fill =c)
canvas.create_rectangle(x+14*d,y,x+15*d,y+d, fill = g)
canvas.create_rectangle(x+14*d,y+d,x+15*d,y+2*d,fill = g)
canvas.create_rectangle(x+14*d,y+2*d,x+15*d,y+3*d, fill =g)
canvas.create_rectangle(x+14*d,y+3*d,x+15*d,y+4*d ,fill =g)
canvas.create_rectangle(x+14*d,y+4*d,x+15*d,y+5*d, fill =g)
canvas.create_rectangle(x+14*d,y+5*d,x+15*d,y+6*d, fill =g)
canvas.create_rectangle(x+14*d,y+6*d,x+15*d,y+7*d, fill =g)
canvas.create_rectangle(x+15*d,y+3*d,x+16*d,y+4*d, fill =g)
canvas.create_rectangle(x+16*d,y+2*d,x+17*d,y+3*d,fill =g)
canvas.create_rectangle(x+17*d,y+d,x+18*d,y+2*d,fill = g)
canvas.create_rectangle(x+18*d,y,x+19*d,y+d, fill = g)
canvas.create_rectangle(x+16*d,y+4*d,x+17*d,y+5*d, fill =g)
canvas.create_rectangle(x+17*d,y+5*d,x+18*d,y+6*d, fill =g)
canvas.create_rectangle(x+18*d,y+6*d,x+19*d,y+7*d, fill = g)
canvas.create_rectangle(x+20*d,y+6*d,x+21*d,y+7*d, fill = j)
canvas.create_rectangle(x+20*d,y+5*d,x+21*d,y+6*d, fill = j)
canvas.create_rectangle(x+20*d,y+4*d,x+21*d,y+5*d, fill =j)
canvas.create_rectangle(x+20*d,y+3*d,x+21*d,y+4*d, fill =j)
canvas.create_rectangle(x+20*d,y+2*d,x+21*d,y+3*d,fill =j)
canvas.create_rectangle(x+21*d,y+2*d,x+22*d,y+3*d, fill =j)
canvas.create_rectangle(x+22*d,y+2*d,x+23*d,y+3*d, fill =j)
canvas.create_rectangle(x+23*d,y+2*d,x+24*d,y+3*d, fill =j)
canvas.create_rectangle(x+20*d,y+d,x+21*d,y+2*d, fill =j)
canvas.create_rectangle(x+21*d,y,x+22*d,y+d, fill =j)
canvas.create_rectangle(x+22*d,y,x+23*d,y+d, fill =j)
canvas.create_rectangle(x+23*d,y+d,x+24*d,y+2*d, fill=j)
canvas.create_rectangle(x+23*d,y+2*d,x+24*d,y+3*d, fill =j)
canvas.create_rectangle(x+23*d,y+3*d,x+24*d,y+4*d, fill =j)
canvas.create_rectangle(x+23*d,y+4*d,x+24*d,y+5*d, fill =j)
canvas.create_rectangle(x+23*d,y+5*d,x+24*d,y+6*d, fill =j)
canvas.create_rectangle(x+23*d,y+6*d,x+24*d,y+7*d, fill =j)
canvas.create_rectangle(x+25*d,y+d,x+26*d,y+2*d, fill =e) ,
canvas.create_rectangle(x+26*d,y,x+27*d,y+d, fill =e)
canvas.create_rectangle(x+27*d,y,x+28*d,y+d, fill =e)
canvas.create_rectangle(x+28*d,y+d,x+29*d,y+2*d,fill =e)
canvas.create_rectangle(x+25*d,y+2*d,x+26*d,y+3*d, fill=e)
canvas.create_rectangle(x+26*d,y+3*d,x+27*d,y+4*d, fill=e)
canvas.create_rectangle(x+27*d,y+3*d,x+28*d,y+4*d, fill=e)
canvas.create_rectangle(x+28*d,y+4*d,x+29*d,y+5*d, fill=e)
canvas.create_rectangle(x+28*d,y+5*d,x+29*d,y+6*d, fill=e)
canvas.create_rectangle(x+27*d,y+6*d,x+28*d,y+7*d, fill=e)
canvas.create_rectangle(x+26*d,y+6*d,x+27*d,y+7*d, fill=e)
canvas.create_rectangle(x+25*d,y+5*d,x+26*d,y+6*d, fill=e)


















# ry hard















canvas.mainloop()
