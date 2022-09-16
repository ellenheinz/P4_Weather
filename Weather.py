import requests

api_key = "4f11d7752117d41f67948b27dd410e38"
city = "Florianópolis"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

requisicao = requests.get(link)