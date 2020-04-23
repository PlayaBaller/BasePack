try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import time
import os
import datetime

# Defining the main window
root = Tk()
root.title('Clock')
clock = Label(root, font=('times', 30, 'bold'), bg='purple')
clock.pack(fill=BOTH, expand=1)


# Delete entry field placeholder
def clear_filed(alarm_time):
    entry_field.delete(0, END)


def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_time) == 1:  # [Hour] Format
        if 24 > alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2:  # [Hour:Minute] Format
        if 24 > alarm_time[0] >= 0 and \
                60 > alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:  # [Hour:Minute:Second] Format
        if 24 > alarm_time[0] >= 0 and \
                60 > alarm_time[1] >= 0 and \
                60 > alarm_time[2] >= 0:
            return True
    return False


print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
while True:
    alarm_input = input(">> ")
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Enter time in HH:MM or HH:MM:SS format")

# Define entry field
entry_field = Entry(root, width=50)
entry_field.insert(0, "When to alarm? Enter in format: "'"HH:MM"')
entry_field.pack(side='bottom')
entry_field.focus_set()
# Enter button
buttonCommit = Button(root, height=1, width=20, text="Enter alarm", command=lambda: input_value)
buttonCommit.pack()
# Delete entry field placeholder
entry_field.bind("<Button-1>", clear_filed)

input_value = entry_field.get()


# Clock itself
def tick():
    s = time.strftime('%D | %H:%M:%S')
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)


# Clock 'ticks' and updates
tick()
root.mainloop()

