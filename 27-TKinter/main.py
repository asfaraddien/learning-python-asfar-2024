import tkinter

window = tkinter.Tk()
window.title("Belajar demi Akhirat")
window.minsize(width=600, height=600)
window.config(padx=200, pady=200)

# TODO: Label
tulisan = tkinter.Label(text="[kosong]")
# tulisan.pack()
# tulisan.place(x=0, y=0)
tulisan.grid(column=0, row=0)
tulisan.config(padx=10, pady=10)

def pencet():
    tulisan.config(text=inp.get())



# TODO: Button
button = tkinter.Button(text="Click Me!", command=pencet)
# button.pack()
button.grid(column=2, row=2)

button2 = tkinter.Button(text="New Button")
button2.grid(column=3, row=0)

# TODO: Entry
inp = tkinter.Entry(width=10)
# inp.pack()
inp.grid(column=4, row=4)




window.mainloop()