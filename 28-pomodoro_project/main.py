from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
######
CHECK = '✔️'
mark = ""
reps = 0
timer_sys = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    # window.after_cancel(timer_sys)
    canvas.itemconfig(timer, text="00.00")
    timer_label.config(fg=GREEN, text="TIMER")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global reps
    reps += 1

    if reps > 8:
        timer_label.config(fg=GREEN, text="TIMER")
        return
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(fg=GREEN, text="WORK")
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(fg=RED, text="BREAK")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(fg=PINK, text="BREAK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    global reps, mark
    min = math.floor(count / 60)
    if min < 10:
        min = f"0{min}"

    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer, text=f"{min}:{sec}")
    if count > 0:
        global timer_sys
        timer_sys = window.after(10, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0:
            mark += CHECK
            check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
img = PhotoImage(file="tomato.png")
canvas = Canvas(width=208, height=233, background=YELLOW, highlightthickness=0)

window.title("Pomodoro Alarm")
window.config(padx=100, pady=100, background=YELLOW)
canvas.create_image(103, 113, image=img)
timer = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=2, row=2)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"), highlightthickness=0)
timer_label.grid(column=2, row=1)

start_button = Button(text="START", highlightthickness=0, command=start)
start_button.grid(column=1, row=3)

reset_button = Button(text="RESET", highlightthickness=0, command=reset)
reset_button.grid(column=3, row=3)

check_label = Label(fg=GREEN,bg=YELLOW, highlightthickness=0)
check_label.grid(column=2, row=4)




window.mainloop()