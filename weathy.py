import os
import requests
from appJar import gui

APIKey = "APPID=affd60b454bf07754ead0c6265738496"

def update(btn) :
    City = app.getLabel("currentcity")
    request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+City+"&"+APIKey)
    dictionnary = eval(request.text)
    Description = dictionnary["weather"][0]["description"]
    Temp = dictionnary["main"]["temp"]
    app.setLabel("currentcity",City)
    app.setLabel("description", Description)
    app.setLabel("temp",Temp)

def loadCurrentCity() :
    if os.path.exists("currentcity") :
        current = open("currentcity",'r')
        return current.read()
    return None

def changeCity(btn) :
    City = app.getEntry("Change City")
    current = open("currentcity",'w')
    current.write(City)
    app.removeEntry("Change City")
    app.removeButton("Change")
    app.addLabel("currentcity", City)
    app.addLabel("description", text=None)
    app.addLabel("temp", text=None)
    app.addButton("Update", update)
    update(0)

app = gui()
app.setBg("White")
app.addImage("logo", "Weathy_logo.png")

if loadCurrentCity() :
    app.addLabel("currentcity", loadCurrentCity())
    app.addLabel("description", text=None)
    app.addLabel("temp", text=None)
    app.addButton("Update", update)
    update(0)
else :
    app.addLabelEntry("Change City")
    app.addButton("Change", changeCity)


app.go()
