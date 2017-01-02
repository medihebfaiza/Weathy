import os
import requests
from appJar import gui

APIKey = "APPID=affd60b454bf07754ead0c6265738496"
icons = {
    "Clouds" : "icons/cloud.png",
    "Clear" : "icons/sun.png",
    "Mist" : "icons/cloud.png",
    "Rain" : "icons/rain.png",
    "Snow" : "icons/snow.png",
    "Thunderstorm" : "icons/storm.png",
    "Thunderstorm" : "icons/storm.png",
    "Drizzle" : "icons/rain.png"
}

def update(btn) :
    City = app.getLabel("currentcity")
    request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+City+"&"+APIKey)
    dictionnary = eval(request.text)
    Description = dictionnary["weather"][0]["description"]
    Main = dictionnary["weather"][0]["main"]
    Temp = dictionnary["main"]["temp"]
    app.setLabel("currentcity",City)
    app.setImage("icon",icons[Main])
    app.zoomImage("icon", -5)
    app.setLabel("description", Description)
    app.setLabel("temp",Temp)

def loadCurrentCity() :
    if os.path.exists("currentcity") :
        current = open("currentcity",'r')
        return current.read()
    return None

def changeCity(btn) :
    City = app.getEntry("Set City")
    current = open("currentcity",'w')
    current.write(City)
    app.removeEntry("Set City")
    app.removeButton("Confirm")
    app.addLabel("currentcity", City)
    app.addImage("icon","icons/sun.png")
    app.addLabel("description", text=None)
    app.addLabel("temp", text=None)
    app.addButton("Update", update)
    update(0)

app = gui()
app.setTitle("Weathy")
app.setBg("White")
app.addImage("logo", "Weathy_logo.png")
app.zoomImage("logo", -2)

if loadCurrentCity() :
    app.addLabel("currentcity", loadCurrentCity())
    app.addImage("icon","icons/sun.png")
    app.addLabel("description", text=None)
    app.addLabel("temp", text=None)
    app.addButton("Update", update)
    update(0)
else :
    app.addLabelEntry("Set City")
    app.addButton("Confirm", changeCity)


app.go()
