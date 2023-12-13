import tkinter,time,random
canvas_width = 500
canvas_height =600
santa_x = canvas_width//2
santa_y = 64
santa_posun = 1


canvas = tkinter.Canvas(width = canvas_width,height = canvas_height)
image_santa = tkinter.PhotoImage(file = "santa.png.png")
santa = canvas.create_image(santa_x,santa_y, image = image_santa)
canvas.pack()
while True:
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa,0,santa_posun)
    santa_y = santa + santa_posun
    if santa_y == canvas_height+ 64:
        canvas.delete(santa)
        santa_y = 64
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)





import tkinter,time,random
canvas_width = 500
canvas_height =600
santa_y = canvas_width//2
santa_x = 64
santa_posun = 1


canvas = tkinter.Canvas(width = canvas_width,height = canvas_height, )
image_santa = tkinter.PhotoImage(file = "santa.png.png")
santa = canvas.create_image(santa_y,santa_x, image = image_santa)
canvas.pack()
while True:
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa,0,santa_posun)
    santa_y = santa + santa_posun
    if santa_x == canvas_width- 64:
        canvas.delete(santa)
        santa_x = 64
        santa = canvas.create_image(santa_x, santa_x, image=image_santa)




canvas = tkinter.Canvas(width = canvas_width,height = canvas_height)
image_santa = tkinter.PhotoImage(file = "santa.png.png")
santa = canvas.create_image(santa_y,santa_x, image = image_santa)
canvas.pack()
while True:
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa,0,santa_posun)
    santa_y = santa + santa_posun
    if santa_y == canvas_height+64:
        canvas.delete(santa)
        santa_x = 66
        santa = canvas.create_image(santa_x, santa_x, image=image_santa)












