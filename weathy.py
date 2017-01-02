import os
import requests
from appJar import gui

APIKey = "APPID=affd60b454bf07754ead0c6265738496"
icons = {
    "Clouds" : "icons/cloud.gif",
    "Clear" : "icons/sun.gif",
    "Mist" : "icons/cloud.gif",
    "Rain" : "icons/rain.gif",
    "Snow" : "icons/snow.gif",
    "Thunderstorm" : "icons/storm.gif",
    "Thunderstorm" : "icons/storm.gif",
    "Drizzle" : "icons/rain.gif"
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
    current.close()
    app.removeEntry("Set City")
    app.removeButton("Confirm")
    build()

def build() :
        app.addLabel("currentcity", loadCurrentCity())
        app.addImage("icon","icons/sun.gif") #icon by default
        app.zoomImage("icon", -5)
        app.addLabel("description", text=None)
        app.addLabel("temp", text=None)
        app.addHorizontalSeparator()
        app.addButton("Update", update)
        update(0)

#GUI Options
app = gui()
app.setTitle("Weathy")
app.setIcon("icons/Weathy.ico")
app.setBg("White")
app.addImage("logo", "icons/Weathy_logo.gif")
app.zoomImage("logo", -2)

if loadCurrentCity() :
    build()
else :
    app.addLabelEntry("Set City")
    app.addButton("Confirm", changeCity)


app.go()
