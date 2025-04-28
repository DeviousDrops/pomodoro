from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps=0
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer",fg=GREEN)
    ch['text']=''

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(): 
    global reps    
    reps += 1
    if reps%8==0:
        ch['text']+='✔'
        timer.config(text="Break",fg=PINK)
        countdown(LONG_BREAK_MIN*60)
    elif reps%2==0:
        ch['text']+='✔'
        timer.config(text="Break",fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        timer.config(text="Work",fg=RED)
        countdown(WORK_MIN*60)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(a):
    global reps
    if(a>=0 and reps!=0):
        canvas.itemconfig(timer_text,text=f"{a//60:02}:{a%60:02}")
        window.after(1000,countdown,a-1)
        if(a==0):
            start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=240,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,120, image=tomato)
timer_text=canvas.create_text(100,135,text="00:00",font=(FONT_NAME,35,'bold'),fill="white")
start=Button(text="start",command=start_timer)
reset=Button(text="reset",command=reset_timer)
timer=Label(text="Timer",font=(FONT_NAME,35,'bold'),fg=GREEN,bg=YELLOW)
ch=Label(fg=GREEN,bg=YELLOW,text="")
timer.grid(column=2,row=1)
start.grid(column=1,row=3)
reset.grid(column=3,row=3)
canvas.grid(column=2,row=2)
ch.grid(column=2,row=4)









window.mainloop()