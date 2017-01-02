import requests

APIKey = "APPID=affd60b454bf07754ead0c6265738496"
City = input("Enter City : ")
request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+City+"&"+APIKey)
dictionnary = eval(request.text)
print("status : ",dictionnary["weather"][0]["description"])
print("temp : ",dictionnary["main"]["temp"])
