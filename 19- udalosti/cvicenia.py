#cvicenie 3
import turtle
import tkinter
import random
t = turtle.Turtle()
turtle.delay(1)
def slnko(pocet,velkost):
    for i in range(pocet):
        t.pencolor("gold")
        t.pensize(5)
        t.fd(velkost)
        t.fd(-velkost)
        t.lt(360/pocet)
    t.dot(velkost)
def nove_slnko():
    t.clear()
    slnko (random.randint(100,200),random.randint(20,100))







tkinter.Button(text= "slnko",command=nove_slnko).pack()
slnko(12,50)







turtle.mainloop()



#cvcenie 12
import turtle
import random

def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()

def stvorce(dlzka, krok):
    t.pu()
    while dlzka > 0:
        stvorec(dlzka)
        t.fd(krok / 2)
        t.rt(90)
        t.fd(krok / 2)
        t.lt(90)
        dlzka -= krok


t = turtle.Turtle()

stvorce(200, 25)

turtle.done()



#cvicenie 13
import turtle,random
t = turtle.Turtle()

def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256 ** 3):06x}')
    t.begin_fill()

    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()

def veza(dlzka,krok):
    t.pu()
    while dlzka > 0:
        stvorec(dlzka)
        dlzka -= krok
        t.fd(krok / 2)
        t.lt(90)
        t.fd(dlzka)
        t.rt(90)



veza(120,30)




stvorec(100)



turtle.mainloop()