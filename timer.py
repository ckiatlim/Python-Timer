from tkinter import *
import time


def refresh_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    time_now_label.config(text=current_time)
    time_now_label.after(1000, refresh_current_time)
    return current_time


def start_timer():
    time_fraction = time.strptime(refresh_current_time(), '%Y-%m-%d %H:%M:%S')
    current_timestamp = time.mktime(time_fraction)
    print(current_timestamp)

    working_hour = int(hour_input.get())
    if working_hour > 23:
        duration_timer_label.config(text="Please key in the hour between 0 to 23.")
        return
    working_minute = int(minute_input.get())
    if working_minute > 59:
        duration_timer_label.config(text="Please key in the minute between 0 to 59.")
        return
    working_second = int(second_input.get())
    if working_second > 59:
        duration_timer_label.config(text="Please key in the second between 0 to 59.")
        return

    working_time = str(f"{working_hour}:{working_minute}:{working_second}")
    # print(type(working_time))
    working_time_tuple = time.strftime('%Y-%m-%d ') + working_time

    working_time_fraction = time.strptime(working_time_tuple, '%Y-%m-%d %H:%M:%S')
    working_timestamp = time.mktime(working_time_fraction)
    print(working_timestamp)
    
    if working_timestamp < current_timestamp:
        duration_timer_label.config(text="You have key in the wrong time.")

    time_difference = int(working_timestamp - current_timestamp)
    # print(time_difference)
    while time_difference > -1:
        if time_difference >= 1:
            minutes_remaining = time_difference // 60
            seconds_remaining = time_difference % 60
            hours_remaining = 0
            if minutes_remaining > 60:
                hours_remaining = minutes_remaining // 60
                minutes_remaining = minutes_remaining % 60
        time_remaining = f"{hours_remaining} hour {minutes_remaining} minutes {seconds_remaining} seconds"
        duration_timer_label.config(text=time_remaining)
        if time_difference == 0:
            duration_timer_label.config(text="You have finished your work today.")
        window.update()
        time.sleep(1)
        time_difference -= 1


window = Tk()
window.title("Timer")
window.config(padx=30, pady=30)

app_title = Label(text="Working Timer", font="Arial 20 bold", pady=10)
app_title.grid(row=0, column=0, columnspan=4)

current_time_text = Label(text="Current Time", font="Arial 14 bold", pady=5)
current_time_text.grid(row=1, column=0)
time_now_label = Label(text="Current Time")
time_now_label.grid(row=1, column=1, columnspan=4)
refresh_current_time()

finish_time_text = Label(text="Off From Work", font="Arial 14 bold")
finish_time_text.grid(row=2, column=0)
hour_input = Entry(width=2)
hour_input.insert(0, "23")
hour_input.grid(row=2, column=1)
minute_input = Entry(width=2)
minute_input.insert(0, "00")
minute_input.grid(row=2, column=2)
second_input = Entry(width=2)
second_input.insert(0, "00")
second_input.grid(row=2, column=3)

duration_label = Label(text = "Time Left", font="Arial 14 bold", pady=10)
duration_label.grid(row=3, column=0)
duration_timer_label = Label(text="00 Hours 00 Minutes 00 Seconds", pady=10)
duration_timer_label.grid(row=3, column=1, columnspan=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=4, column=0, columnspan=4)


window.mainloop()
