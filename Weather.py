import requests
from tkinter import *


def request():
    api_key = "4f11d7752117d41f67948b27dd410e38"
    city = entry.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    req = requests.get(link)
    req_dic = req.json()
    description = req_dic['weather'][0]['description']
    temp = req_dic['main']['temp'] - 273.15

    result['text'] = f'{temp: .0f}ºC'

    if temp < 16:
        window.config(bg=col1)
        text1.config(bg=col1)
        text2.config(bg=col1)
        result.config(bg=col1)
    elif temp < 25:
        window.config(bg=col2)
        text1.config(bg=col2)
        text2.config(bg=col2)
        result.config(bg=col2)
    else:
        window.config(bg=col3)
        text1.config(bg=col3)
        text2.config(bg=col3)
        result.config(bg=col3)


col0 = "#D8BFD8"
col1 = "#1E90FF"
col2 = "#FFD700"
col3 = "#FF4500"

window = Tk()
window.title("Previsão do Tempo")
window.geometry("313x95")
window.config(bg=col0)

text1 = Label(window, text="Cidade:")
text1.grid(column=0, row=0)
text1.config(bg=col0)
text1.place(x=3, y=3)

text2 = Label(window, text="Temperatura:")
text2.grid(column=0, row=1)
text2.config(bg=col0)
text2.place(x=3, y=27)

button = Button(window, text="Pesquisar", command=request)
button.grid(column=2, row=0)
button.place(x=185, y=3)

entry = Entry(window)
entry.grid(column=1, row=0)
entry.place(x=53, y=5)

result = Label(window)
result.grid(column=1, row=1)
result.config(bg=col0)
result.place(x=75, y=27)

window.mainloop()