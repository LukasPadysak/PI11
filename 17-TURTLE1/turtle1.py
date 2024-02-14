import turtle,random

def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

t = turtle.Turtle()
stvorec(30)

for i in range(10):
    t.penup()
    t.setposition(random.randint(-200, 100) , random.randint(-200, 100))
    t.left(45)
    t.pendown()
    t.fillcolor(random.choice(("red","blue","green")))
    t.begin_fill()






    stvorec(30)
    t.end_fill()

