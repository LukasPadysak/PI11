import turtle

pocet = 4
turtles = [] #list (resp.pole) korytnačiek

for i in range(pocet):
    t = turtle.Turtle()
    t.penup()
    t.setpos(i * 100, 0)
    t.pendown()
    turtles.append(t)


# for t in turtles:
#     for i in range(4):
#         t.fd(50)
#         t.lt(90)
for i in range(20):
    for i in range(4):
        for t in turtles:
            t.fd(50)
            t.lt(90)
    t.lt(360/20)



turtle.mainloop()