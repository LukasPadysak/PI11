import tkinter, time,random
canvas = tkinter.Canvas()
canvas.pack()

stvorec1 = canvas.create_rectangle(10,10,110,110,fill = "blue")
for i in range(1000):
    canvas.update()
    time.sleep(0.01)
    canvas.move(stvorec1,1,0)  #stvorec1 je objekt,ktorý sa bude posúvať,100 na x a 0 o kolko na y osi
    farba = random.choice(("red","green","blue","brown","pink"))
    canvas.itemconfig(stvorec1, fill = farba)



canvas.mainloop()