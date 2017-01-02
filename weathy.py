import requests

APIKey = "APPID=affd60b454bf07754ead0c6265738496"
City = "London"
request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+City+"&"+APIKey)
dictionnary = eval(request.text)
print(dictionnary["weather"][0]["description"])
