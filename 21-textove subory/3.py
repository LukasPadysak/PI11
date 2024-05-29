import tkinter
canvas = tkinter.Canvas()
canvas.pack()


fbody = open('body.txt','r')
for riadok in fbody:
    print (riadok)
    medzera = riadok.find(' ')
    print(medzera )
    x = int(riadok[:medzera])
    y = int(riadok[medzera:])
    print(x,y)

canvas.mainloop()

