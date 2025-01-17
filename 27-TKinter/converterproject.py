from tkinter import *

window = Tk()
window.title("Converter")
window.config(padx=50, pady=50)

def calculate():
    result = float(mile.get()) * 1.609
    km.config(text=round(result, 2))


mile = Entry(width=10)
mile.grid(column=2, row=1)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)

km = Label(text=0)
km.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

button = Button(text="calculate", command=calculate)
button.grid(column=2, row=3)

window.mainloop()