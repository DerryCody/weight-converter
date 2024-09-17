import tkinter

screen=tkinter.Tk()
screen.geometry("900x300")


screen.title("Weight conversion")
screen.configure(background="red")

def calculations():
    grams=int(weight.get())*1000
    pounds=int(weight.get())*2.2046
    ounces=int(weight.get())*35.274
    grams1.configure(text=grams)
    pounds1.configure(text=pounds)
    ounces1.configure(text=ounces)

label=tkinter.Label(screen,background="black",text="Enter the weight in Kg",font=("times new roman",35),padx=30,pady=30)
label.grid(row=0,column=0)

weight=tkinter.Entry(screen,fg="black",font=("times new roman",35))
weight.grid(row=0,column=1)

button=tkinter.Button(screen,background="black",text="Convert",font=("times new roman",35),command=calculations)
button.grid(row=0,column=2)

label=tkinter.Label(screen,background="black",text="Grams",font=("times new roman",35))
label.grid(row=1,column=0)

label=tkinter.Label(screen,background="black",text="Pounds",font=("times new roman",35))
label.grid(row=1,column=1)

label=tkinter.Label(screen,background="black",text="Ounces",font=("times new roman",35))
label.grid(row=1,column=2)

grams1=tkinter.Label(screen,background="black",font=("times new roman",35))
grams1.grid(row=2,column=0)

pounds1=tkinter.Label(screen,background="black",font=("times new roman",35))
pounds1.grid(row=2,column=1)

ounces1=tkinter.Label(screen,background="black",font=("times new roman",35))
ounces1.grid(row=2,column=2)

screen.mainloop()

