from tkinter import *
import json
import datetime
import os
os.system('pip install requests')
import requests

main = Tk()
main.title("Weather Forecast")
main.geometry("450x700")
main['background'] = "white"

dt = datetime.datetime.now()
date = Label(main, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(main, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

hour = Label(main, text=dt.strftime('%I : %M %p'),
             bg='white', font=("bold", 15))
hour.place(x=10, y=160)

city_name = StringVar()
city_entry = Entry(main, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

city_name = StringVar()
city_entry = Entry(main, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

def city_name():
    api_request = requests.get("https://api.openweathermap.org/data/3.0/onecall?q="+ city_entry.get() + "&units=metric&appid="+"6ae75eb1bdf34f48ab2620416253ee2b")
    api = json.loads(api_request.content)


city_nameButton = Button(main, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S)

lable_citi = Label(main, text="...", width=0, bg='white', font=("bold", 15))
lable_citi.place(x=10, y=63)
lable_country = Label(main, text="...", width=0, bg='white', font=("bold", 15))
lable_country.place(x=135, y=63)
lable_lon = Label(main, text="...", width=0, bg='white', font=("Helvetica", 15))
lable_lon.place(x=25, y=95)
lable_lat = Label(main, text="...", width=0, bg='white', font=("Helvetica", 15))
lable_lat.place(x=95, y=95)
lable_temp = Label(main, text="...", width=0, bg='white', font=("Helvetica", 110), fg='black')
lable_temp.place(x=18, y=220)
maxi = Label(main, text="Max. Temp.: ", width=0, bg='white', font=("bold", 15))
maxi.place(x=3, y=430)
 
max_temp = Label(main, text="...", width=0, bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)
mini = Label(main, text="Min. Temp.: ", width=0, bg='white', font=("bold", 15))
mini.place(x=3, y=460)
min_temp = Label(main, text="...", width=0, bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

main.mainloop()