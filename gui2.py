from tkinter import *

window = Tk()

def kg_to_lb_oz():
    print(e1_value.get())
    oz = float(e1_value.get())*35.274 % 16
    lb = (float(e1_value.get())*35.274 - oz)/16
    g = float(e1_value.get())*1000
    t0.insert(END, g)
    t1.insert(END, lb)
    t2.insert(END, oz)

b1 = Button(window, text = "Convert", command = kg_to_lb_oz)
b1.grid(row = 0, column = 2)

e0 = Label(window, text = "KG")
e0.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

t0 = Text(window, height = 1, width = 20)
t0.grid(row = 1, column =0)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column =1)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column =2)

window.mainloop()
