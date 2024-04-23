from tkinter import *
import json
import datetime

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

main.mainloop()