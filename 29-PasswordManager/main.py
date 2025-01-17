from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from pass_gen import go
def genit():
    pass_inp.delete(0, END)
    pass_inp.insert(0, go())
    pyperclip.copy(pass_inp.get())

def find_pass():
    web = web_inp.get().lower()
    try:
        with open("data.json") as data:
            datum = json.load(data)
            web_go = datum.get(web)
            email_go = web_go.get("email")
            pass_go = web_go.get("password")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="Belum ada file-nya")wili
    except:
        messagebox.showwarning(title="Error", message="Enggak nemu key-nya")
    else:
        messagebox.askokcancel(title="Browse", message=f"email: {email_go}\npassword: {pass_go}\nAre you sure?")
        print(web_go)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_inp.get().lower()
    email = email_inp.get()
    password = pass_inp.get()

    new = {f"{web}":{
        "email":email,
        "password":password
    }}
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Hmmm!!", message="You missing something!")
    else:
        verif = messagebox.askokcancel(title="Verification", message=f"website: {web_inp.get()}\nemail: {email_inp.get()}\n"f"password: {pass_inp.get()}")
        if verif:
            with open("data.txt", "a") as data:
                data.write(f"{web} | {email} | {password}\n")

            try:
                data = open("data.json")
            except FileNotFoundError:
                data = open("data.json", "w")
                json.dump(new,data ,indent=4)
            else:
                datum = json.load(data)
                datum.update(new)
                with open("data.json", "w") as data:
                    json.dump(datum, data, indent=4)
            finally:
                web_inp.delete(0, END)
                pass_inp.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)
photo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

web_label = Label(text="website:")
web_label.grid(row=1, column=0)

web_search = Button(text="Search", command=find_pass)
web_search.grid(row=1, column=2, sticky="w")

email_label = Label(text="Email/username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

web_inp = Entry(width=17)
web_inp.focus()
web_inp.grid(row=1, column=1)

email_inp = Entry(width=35)
email_inp.insert(0, "asfar@gmail.com")
email_inp.grid(row=2, column=1, columnspan=2)

pass_inp = Entry(width=17)
pass_inp.grid(row=3, column=1)

pass_button = Button(text="Generate Password", command=genit)
pass_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()