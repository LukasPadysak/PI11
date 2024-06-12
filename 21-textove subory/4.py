import tkinter
canvas = tkinter.Canvas()
canvas.pack()
fsubor = open("subor.txt","r")


for riadok in fsubor:
  # r = fsubor.readline()
  # print(riadok[:-1])

  medzera = riadok.find('')
  tvar = riadok[:medzera]
  riadok = riadok[medzera+1:]
  medzera = riadok.find('')
  x = int(riadok[medzera:])
  riadok = riadok[medzera+1:]
  y = int(riadok[medzera])
  riadok = riadok.find('')
  print(tvar,x,y)
  if tvar == "r":
    canvas.create_rectangle(x,y,x+20,y+20)
  else:
    canvas.create_oval(x,y,x+20,y+20)





canvas.mainloop()