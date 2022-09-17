import requests
from tkinter import *

api_key = "4f11d7752117d41f67948b27dd410e38"
city = "Florianópolis"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

req = requests.get(link)
req_dic = req.json()
description = req_dic['weather'][0]['description']
temp = req_dic['main']['temp'] - 273.15

print(description, f'{temp: .2f}ºC')

window = Tk()
window.title("Previsão do Tempo")

text1 = Label(window, text="Cidade: ")
text1.grid(column=0, row=0)
text2 = Label(window, text="   ")
text2.grid(column=1, row=1)

window.mainloop()