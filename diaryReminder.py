import tkinter as tk 
from tkinter import *
import datetime
from datetime import datetime, date, time,timedelta
import time as t_sleep
import random




def generateTimes():
    start_time = datetime.combine(date.today(), time(9,00))
    end_time = datetime.combine(date.today(), time(17,00))
    delta = timedelta(minutes=30)
    times = [start_time]
    while times[-1] < end_time:
        times.append(times[-1] + delta)
    print([datetime.isoformat(t) for t in times])
    return times

def submit():
    global frame
    global newline
    newline=textBox.get("1.0","end-1c")
    frame.destroy()
    

index = 0
newline = ""
title = "Diary Reminder"
times = generateTimes()
random1 = random.randrange(1,20)
random2 = random.randrange(1,20)
wrong = False
random.seed(t_sleep.time())
while True:
    if(datetime.now() >= times[index]):
        frame = tk.Tk() 
        frame.geometry("200x100")
        frame.title("Diary Reminder")
        tk.Label(frame, text=f'Write down your record since {times[index].hour:02d}:{times[index].minute:02d}', wraplength=300).pack()
        if(wrong):
            tk.Label(frame, text="TRY AGAIN").pack()
        tk.Label(frame, text=f'What is {random1} x {random2}').pack()
        textBox=Text(frame, height=1, width=5)
        textBox.pack()
        Button(text="Submit", command=submit).pack()
        frame.bind('<Return>', lambda event: submit())       
        frame.mainloop()
        if(newline != "" and int(newline) == random1*random2):
            newline = ""
            index +=1
            print(f"Correct! Next time is {times[index]} ")
            if(datetime.now() - times[index] > timedelta(minutes=30)):
                t_sleep.sleep(3)
            else:
                t_sleep.sleep(60)
            random1 = random.randrange(1,20)
            random2 = random.randrange(1,20)
            wrong = False
        else:
            t_sleep.sleep(0.5)
            wrong = True
        


