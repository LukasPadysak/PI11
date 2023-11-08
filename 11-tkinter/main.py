import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 50
dlzka = 20
canvas.create_rectangle(x, y, x + dlzka, y + dlzka, fill="blue")
canvas.create_rectangle(x + dlzka , y , x + (2*dlzka) , y + dlzka)
canvas.create_rectangle(x +(2*dlzka), y+dlzka,x+ (2* dlzka),y +(2*dlzka)



canvas.mainloop()


