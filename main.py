from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():

    global reps, checks
    reps = 0
    checks = '1:'
    check_l.config(text=checks)
    canvas.itemconfig(timer_text, text='00:00')
    timer_l.config(text='Timer', fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, checks
    if reps == 9:
        reps = 0
        checks += ' 2:'
        check_l.config(text=checks)
    reps += 1
    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        checks += '✔'
        check_l.config(text=checks)
        timer_l.config(text='Break', fg=PINK)
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        timer_l.config(text='Break', fg=RED)
    else:
        count_down(WORK_MIN*60)
        timer_l.config(text='Work', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    if reps != 0:
        if len(str(count % 60)) < 2:
            time = str(count // 60) + ':0' + str(count % 60)
        else:
            time = str(count//60) + ':' + str(count % 60)
        canvas.itemconfig(timer_text, text=time)

        if count > 0:
            window.after(5, count_down, count-1)
        else:
            start_timer()
    else:
        return


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro time manager')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_l = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_l.grid(column=1, row=0)

checks = '1:'
check_l = Label(text=checks, bg=YELLOW, fg=GREEN)
check_l.grid(column=1, row=3)

start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset_b = Button(text='Reset', highlightthickness=0, command=reset)
reset_b.grid(column=2, row=2)

window.mainloop()
