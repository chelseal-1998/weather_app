from tkinter import *
import tkinter as tk
import requests

height = 500
width = 500


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']

        if button1:
            final_str = "Place: %s \nWeather: %s \nTemperature: %s \nHumidity: %s\n Wind speed: %s " % (name, desc, temp, humidity, wind)

        if button2:
            final_str = "Place: %s \nWeather: %s \nTemperature: %s \nHumidity: %s\n Wind speed: %s" % (name, desc, temp , humidity, wind)
    except:
        final_str = "There was a problem retrieving that information"

    return final_str


def get_weather(city):
    weather_key = '3b78eb34193f80550abac60986461e7b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units': "metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


def Clearing():
    entry.delete(0, END)


root = Tk()
canvas = tk.Canvas(root, height=height, width=width, bg="grey")
canvas.pack()

frame = tk.Frame(root, bg="cyan", bd='25')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.14, anchor='n')

entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.5, relheight=1)

button1 = tk.Button(frame, text="Get Weather", font="times 13", command=lambda: get_weather(entry.get()))
button1.place(relx=0.53, rely=0, relheight=1.25, relwidth=0.50)

button2 = tk.Button(frame, text="Clear", font="times 13", command=Clearing)
button2.place(relx=0.125, rely=1.05, relheight=1.25, relwidth=0.25)

lower_frame = tk.Frame(root, bg="cyan", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)
root.mainloop()
