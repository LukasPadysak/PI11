# cvicenie 11
import random
import tkinter
canvas = tkinter.Canvas(height = 600,width = 600)
canvas.pack()
x = random.randint(50,300)
y = random.randint(50,300)

def karticka(x,y,text):
    canvas.create_rectangle(x+50,y+50,x-50,y-20)
    canvas.create_text(x,y,text= text )





for i in range(10):




    karticka(random.randint(50,300) ,random.randint(50,200),"Python")




canvas.mainloop()







# cvicenie 17
import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()

x = random.randint(10,350)
y = random.randint(10,250)
polomer = 10

for i in range(1000):
    if y < 90:
        farba = "black"
    if y < 170:
        farba = "red"
    else:
        farba = "gold"


    canvas.create_oval(x+polomer,y+polomer,x-polomer,y-polomer,fill = farba)









canvas.mainloop()



# cvicenie 16
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

n = int(input('zadaj počet stĺpcov: '))
m = int(input('zadaj počet riadkov: '))

vel = 30
farba1, farba2 = 'maroon', 'gold'
x, y = 10, 10
for i in range(m):
    f1, f2 = farba1, farba2
    for j in range(n):
        canvas.create_rectangle(x + (vel+3) * j, y + (vel+3) * i,
                                x + (vel+3) * j + vel, y + (vel+3) * i + vel,
                                fill=f1)
        f1, f2 = f2, f1
    farba1, farba2 = farba2, farba1

tkinter.mainloop()



















