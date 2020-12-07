import tkinter



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="Start!")
    tick_label.config(text="")
    timer_label.config(text="Hi!")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0:
        if reps % 8 == 0:
            countdown(60 * LONG_BREAK_MIN)
            timer_label.config(text="Long Break", fg=RED)
        else:
            countdown(60 * SHORT_BREAK_MIN)
            timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(60 * WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)
        tick_label.config(text="☑" * (reps // 2) + "☐")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# The window itself
window = tkinter.Tk()
window.title(string="Pomodoro!")
window.config(padx=30, pady=20, bg=YELLOW)

# The where the picture is located
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="Start!", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# The timer name
timer_label = tkinter.Label()
timer_label.config(text="Hi!", padx=6, pady=6, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# The start button
start_button = tkinter.Button()
start_button.config(text="Start!", padx=6, pady=6, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# The reset button
reset_button = tkinter.Button()
reset_button.config(text="Reset", padx=6, pady=6, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# The tick marks
tick_label = tkinter.Label()
tick_label.config(text="", padx=6, pady=6, font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
tick_label.grid(column=1, row=3)

window.mainloop()
