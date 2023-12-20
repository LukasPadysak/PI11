import tkinter
import random
canvas_width = 900
canvas_height =900
pocet = 100000
polomer = 10
canvas = tkinter.Canvas(width = canvas_width,height = canvas_height)
canvas.pack()
for i in range(pocet):
    x = random.randint(polomer + 2,canvas_width - polomer)
    y = random.randint(polomer + 2,canvas_height - polomer)

    if x < canvas_width//2 and y < canvas_height //2 :
        farba = "blue"
    elif x < canvas_height //2 and y >= canvas_height//2:
        farba = "lightgreen"
    elif x > canvas_width//2 and y < canvas_width//2:
        farba= "brown"
    else:
        farba = "red"
    canvas.create_oval(x-polomer,y-polomer,x+polomer,y+polomer,fill = farba)






canvas.mainloop()
