from tkinter import *
import json
import datetime
import os
os.system('pip install requests')
import requests
os.system('pip install Pillow')
from PIL import ImageTk, Image

main = Tk()
main.title("Weather Forecast")
main.geometry("450x700")
main['background'] = "white"
script_dir = os.path.dirname(os.path.abspath(__file__))

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
    coords = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + city_entry.get() + "&limit=1&appid=6ae75eb1bdf34f48ab2620416253ee2b").json()
    temp_coords = coords[0]
    latitude = str(temp_coords.get("lat"))
    longtitude = str(temp_coords.get("lon"))
    country = str(temp_coords["country"])
    citi = str(temp_coords["name"])
    api_request = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat="+ latitude +"&lon="+ longtitude +"&units=imperial&appid=6ae75eb1bdf34f48ab2620416253ee2b")
    api = json.loads(api_request.content)
    y = api["current"]
    current_temprature = y['temp']
    humidity = y['humidity']
    tempmin = api['daily'][0]['temp']['min']
    tempmax = api['daily'][0]['temp']['max']
    lable_temp.configure(text=current_temprature)
    lable_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    lable_lon.configure(text=longtitude)
    lable_lat.configure(text=latitude)
    lable_country.configure(text=country)
    lable_citi.configure(text=citi)

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
humi = Label(main, text="Humidity: ", width=0, bg='white', font=("bold", 15))
humi.place(x=3, y=400)
lable_humidity = Label(main, text="...", width=0, bg='white', font=("bold", 15))
lable_humidity.place(x=107, y=400)

new = ImageTk.PhotoImage(Image.open(script_dir + '\logo.png'))
panel = Label(main, image=new)
panel.place(x=0, y=520)

if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <= 5:
    img = ImageTk.PhotoImage(Image.open(script_dir + '\moon.png'))
    panel = Label(main, image=img)
    panel.place(x=210, y=200)
else:
    img = ImageTk.PhotoImage(Image.open(script_dir + '\sun.png'))
    panel = Label(main, image=img)
    panel.place(x=210, y=200)

note = Label(main, text="All temperatures are listed in Fahrenheit", bg='white', font=("italic", 10))
note.place(x=95, y=495)

main.mainloop()