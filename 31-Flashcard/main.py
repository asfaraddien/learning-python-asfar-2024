from tkinter import *
import pandas as pd
from random import choice



BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card")

# ---------------------------------backstage----------------------------------------
# ---------get data---------
try:
    data = pd.read_csv("data/learn.csv")
    data_list = pd.DataFrame.to_dict(data, orient="records")
except:
    data = pd.read_csv("data/french_words.csv")
    data_list = pd.DataFrame.to_dict(data, orient="records")



# ---------get random---------
def ch():
    global kata, data_list
    try:
        kata = choice(data_list)
    except IndexError:
        mentah = pd.read_csv("data/french_words.csv")
        data_list = pd.DataFrame.to_dict(mentah, orient="records")
        kata = choice(data_list)
    finally:
        print(kata)
        return kata

# ---------fungsi ganti kata---------
def random_word():
    # window.after_cancel(balik_sys)
    ch()
    fr = kata.get("French")
    front.itemconfig(front_image, image=image1)
    front.itemconfig(lang, text="French", fill="black")
    front.itemconfig(mean_text, text=fr, fill="black")
    balik_func()


# ---------balik kartu---------
def balik_kartu():
    eng = kata.get("English")
    front.itemconfig(front_image, image=image1_2)
    front.itemconfig(lang, text="English", fill="white")
    front.itemconfig(mean_text, text=eng, fill="white")

def balik_func():
    global balik_sys
    balik_sys = window.after(3000, balik_kartu)

# ---------remove and write again---------
def right():
    data_list.remove(kata)
    random_word()
    write_csv()
    print(len(data_list))

def write_csv():
    new_data = pd.DataFrame(data_list)
    new_data.to_csv("data/learn.csv", index=False)




# ---------------------------------layout----------------------------------------
image1 = PhotoImage(file="images/card_front.png")
image1_2 = PhotoImage(file="images/card_back.png")
front = Canvas(height=526, width=800,bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = front.create_image(400, 263, image=image1)
lang = front.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
mean_text = front.create_text(400, 263, text=ch().get("French"), font=("Ariel", 60, "bold"))
front.grid(row=0, column=0, columnspan=2)

image2 = PhotoImage(file="images/right.png")
right_button = Button(image=image2,bg=BACKGROUND_COLOR, highlightthickness=0, command=right)
right_button.grid(row=1, column=1)

image3 = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=image3,bg=BACKGROUND_COLOR, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)







balik_func()
window.mainloop()