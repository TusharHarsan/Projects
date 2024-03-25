#Importing libiraries
import tkinter as tk
from time import time, sleep
import random as r
from datetime import datetime
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from threading import Thread
import requests
import ttkbootstrap as ttkb

#bg color
bg_color = '#ffffff'
col = '#566FC6'
co2 = '#000000'


window = ttkb.tk.Tk()
window.title("Alarm Clock")
window.geometry('470x200')
window.resizable(False, False)

#frames up
frame_line= Frame(window, width =500 , height=6 )
frame_line.grid (row=0 , column = 0 )



frame_body= Frame(window, width =500 , height=290 , bg = bg_color)
frame_body.grid (row=1 , column = 0 )

#configuration frame body
img= Image.open('img2.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body , height=100 , image = img , bg=bg_color)
app_image.place(x=8,y=25)


name = Label(frame_body , text='Alarm', height = 1 , font = ('Ivy 20 bold'), bg = bg_color)
name.place(x=100 , y=8)

hour = Label(frame_body , text='Hour', height = 1 , font = ('Ivy 12 bold'), bg = bg_color ,fg = col )
hour.place(x=130 , y=40)

c_hour = Combobox(frame_body,width=2 , font=('arial 15') )
c_hour['values'] = ('00' , '01','02','03','04' , '05','06','07','08','09','10','11','12')
c_hour.current(0)
c_hour.place(x = 150 , y = 65)

minute = Label(frame_body , text='Minute', height = 1 , font = ('Ivy 12 bold'), bg = bg_color ,fg = col )
minute.place(x=190 , y=40)

c_minute = Combobox(frame_body,width=2 , font=('arial 15') )
c_minute['values'] = ('00' , '01','02','03','04' , '05','06','07','08','09','10','11' , '12','13','14','15' , '16','17','18','19','20','21','22' , '23','24','25','26' , '27','28','29','30','31','32','33' , '34','35','36','37' , '38','39','40','41','42','43','44' , '45','46','47','48' , '49','50','51','52','53','54','55' , '56','57','58','59' )
c_minute.current(0)
c_minute.place(x = 210 , y = 65)


seconds = Label(frame_body , text='Seconds', height = 1 , font = ('Ivy 12 bold'), bg = bg_color ,fg = col )
seconds.place(x=250 , y=40)

c_seconds = Combobox(frame_body,width=2 , font=('arial 15') )
c_seconds['values'] = ('00' , '01','02','03','04' , '05','06','07','08','09','10','11' , '12','13','14','15' , '16','17','18','19','20','21','22' , '23','24','25','26' , '27','28','29','30','31','32','33' , '34','35','36','37' , '38','39','40','41','42','43','44' , '45','46','47','48' , '49','50','51','52','53','54','55' , '56','57','58','59' )
c_seconds.current(0)
c_seconds.place(x = 270 , y = 65)

Period = Label(frame_body, text='Period', height = 1 , font = ('Ivy 12 bold'), bg = bg_color ,fg = col )
Period.place(x=330 , y=40)

c_Period = Combobox(frame_body,width=3 , font=('arial 15') )
c_Period['values'] = ('AM','PM')
c_Period.current(0)
c_Period.place(x = 330 , y = 65)

def activate_alarm():
    t= Thread(target = alarm)
    t.start()

rad1 = tk.Radiobutton(frame_body , font = ('arial 10 bold'), value=2,text='Activate',bg = bg_color,command= activate_alarm )
rad1.place(x=125 , y = 110)

def deactivate_alarm():
    print('deactivated alarm', selected.get())
    mixer.music.stop()

def terminate_alarm():
    print('Terminated Alarm')
    exit()

rad3 = tk.Radiobutton(frame_body , font = ('arial 11 bold'), value=2,text='Terminate',bg = bg_color,command= terminate_alarm)
rad3.place(x=320 , y = 110)

selected = IntVar()

forweather=0

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    time_rr = time_r/10
    speed = len(userinput) / time_rr
    return round(speed)

def start_typing_test():
    global test1, start_time
    test1 = r.choice(test)
    typing_label.config(text=test1)
    user_input_entry.delete(0, "end")
    start_time = time()
    start_button.config(state=ttkb.NORMAL)
    user_input_entry.config(state=ttkb.NORMAL)
    user_input_entry.bind('<Return>', lambda event=None: check_typing())
    check_button.config(state=ttkb.NORMAL)

def check_typing():
    global test1
    user_input = user_input_entry.get()
    end_time = time()
    time_taken = end_time - start_time
    typing_speed = speed_time(start_time, end_time, user_input)
    typing_errors = mistake(test1, user_input)
    result_labe2.config(text=f"Speed: {typing_speed} wpm\nErrors: {typing_errors}")
    start_button.config(state=tk.NORMAL)
    user_input_entry.config(state=tk.NORMAL)
    check_button.config(state=tk.DISABLED)
    forweather=+1
    if forweather==1:
       submit_button.config(state=ttkb.DISABLED)
    else:
        submit_button.config(state=ttkb.DISABLED)

# Initialize the alarm clock variables
alarm_control = 0

def sound_alarm():
    mixer.music.load('ss.mp3')
    mixer.music.play()
    selected.set(0)

rad2 = tk.Radiobutton(frame_body , font = ('arial 10 bold'), value=2,text='Deactivate',bg = bg_color,command= deactivate_alarm )
rad2.place(x=220 , y = 110)


def alarm():
    while True:
        control = 1
        print(control)
        alarm_hour = c_hour.get()
        alarm_minute = c_minute.get()
        alarm_sec = c_seconds.get()
        alarm_period = c_Period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break")
                            sound_alarm()
                            global alarm_control
                            alarm_control = 1
        sleep(1)


mixer.init()

#weather app Functions and logic
api_key = '30d4741c779ba94c470ca1f63045390a'

def get_weather():
    if start_type==1:
        submit_button.config(state=ttkb.NORMAL)
    else:
        submit_button.config(state=ttkb.DISABLED)
    city = input_area.get()
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        result_label.config(text="No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        result_label.config(text=f"The weather in {city} is: {weather}\nThe temperature in {city} is: {temp}ºF")

# creating start and stop for Typing Test
def start_typing_test_with_alarm():
    global alarm_control
    if alarm_control == 1:
        start_typing_test()
    else:
        messagebox.showinfo("Alarm Not Triggered", "The alarm has not been triggered yet.")

def stop_alarm_with_typing_test():
    global alarm_control
    if alarm_control == 1:
        check_typing()
        mixer.music.stop()
        alarm_control = 0
    else:
        messagebox.showinfo("Alarm Not Triggered", "The alarm has not been triggered yet.")

# Create the main window
root = ttkb.tk.Tk()
root.title("Typing Test")
root.configure(bg='#2b3e50')

# Configure the window size and position
root.geometry("400x320")
root.resizable(False, False)




# Create and configure the GUI components
heading_label=ttkb.tk.Label(root,text='Typing Test',font=('Arial', 22))
heading_label.pack(pady=10)

typing_label = tk.Label(root, text="", wraplength=380, font=("Arial", 12))
typing_label.pack(pady=10)


user_input_entry = ttkb.tk.Entry(root, width=50,font=("Arial", 12))
user_input_entry.pack(pady=10)
user_input_entry.config(state=tk.NORMAL)

start_button = tk.Button(root, text="Start The Typing Test", command=start_typing_test, font=("Arial", 12))
start_button.pack(pady=10)
start_button.config(state=tk.DISABLED)


check_button = tk.Button(root, text="Check", command=check_typing, font=("Arial", 12))
check_button.pack(pady=10)
check_button.config(state=tk.DISABLED)

result_labe2 = tk.Label(root, text="", font=("Arial", 12))
result_labe2.pack(pady =10)


# Sample typing test data
test = ["a paragraph is a self-contained unit of dicourse in wn",
        "my name is Tushar Harsan",
        "welcome to Bnnett University"]

# Initialize variables
test1 = ""
start_time = 0

# Create a "Start Typing Test with Alarm" button
start_typing_with_alarm_button = Button(frame_body, text='Start Typing Test with Alarm', font=('arial 11 bold'),
bg=bg_color, command=start_typing_test_with_alarm,)
start_typing_with_alarm_button.place(x=10, y=140)

# Create a "Stop Alarm with Typing Test" button
stop_alarm_with_typing_test_button = Button(frame_body, text='Stop Alarm with Typing Test', font=('arial 11 bold'),
bg=bg_color, command=stop_alarm_with_typing_test)
stop_alarm_with_typing_test_button.place(x=250, y=140)

start_type=0

#creating the GUi of Weather
rooot = ttkb.Window(themename="superhero")
rooot.title("Weather Forecast")
rooot.geometry('500x300')
rooot.resizable(False, False)

my_label = ttkb.Label(rooot, text='Weather', font=('Helvetica', 28))
my_label.grid(row=0, column=0, pady=20,padx=180)


input_area = ttkb.Entry(rooot)
input_area.grid(row=1, column=0, pady=10)

submit_button = ttkb.Button(rooot, text="Get Weather", command=get_weather)
submit_button.grid(row=2, column=0, pady=10)
submit_button.config(state=ttkb.DISABLED)

result_label = ttkb.Label(rooot, text="")
result_label.grid(row=3, column=0, pady=20)

# Run the GUI
window.mainloop()
