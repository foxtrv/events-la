from colors import colors
from bs4 import BeautifulSoup
import requests

### sports collection ###
url = 'https://gametime.co/los-angeles-tickets/metros/losangeles'
response = requests.get(url, headers = {'User-agent': 'event bot 1.0'})
soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll(class_="_2h2W9WsYjZ0nMQMlLrr4cJ")

# a is the collection of events. b is each individual event
b = a[0].findAll(class_="col-md-6")

print (colors.red + "================ Collected from GameTime website - Sports ================" + colors.black)

for i in range(len(b)):
    print(colors.green + "Event " + str(i+1) + ":" + colors.black)
    eventName = b[i].find(class_="_3QpUIoSPLTS7PxcIALO8Re")
    if (eventName != None):
        print(eventName.text)
    eventDate = b[i].find(class_="LIsmOmbzL4AwaITrZy_0N")
    if (eventDate != None):
        eventDateActual = eventDate.find(class_="_2opqbRqujFoCFp0b6jZeMY")
        if (eventDateActual != None):
            print(eventDateActual.text)
        eventPrice = eventDate.find(class_="_2mZMUi21HU4ydbF4R-70DQ")
        if (eventPrice != None):
            print(eventPrice.text[7:]+"+")
    print()





### music/concerts collection ###
url = 'https://gametime.co/los-angeles-tickets/metros/losangeles/concert'
response = requests.get(url, headers = {'User-agent': 'event bot 1.0'})
soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll(class_="_2h2W9WsYjZ0nMQMlLrr4cJ")

# a is the collection of events. b is each individual event
b = a[0].findAll(class_="col-md-6")

print (colors.red + "================ Collected from GameTime website - Music/Concerts ================" + colors.black)

for i in range(len(b)):
    print(colors.green + "Event " + str(i+1) + ":" + colors.black)
    eventName = b[i].find(class_="X47khF4xL4X-kF84-zkUQ container")
    if (eventName != None):
        eventNameActual = eventName.find(class_="_30B4YbPIjfZuZ03--GRTyB")
        eventLoc = eventName.find(class_="_3j0gTA8nYDiv1k6Lg0nJqV")
        if (eventNameActual != None):
            print(eventNameActual.text)
        if (eventLoc != None):
            print(eventLoc.text)
    eventDate = b[i].find(class_="LIsmOmbzL4AwaITrZy_0N")
    if (eventDate != None):
        eventDateActual = eventDate.find(class_="_2opqbRqujFoCFp0b6jZeMY")
        eventPrice = eventDate.find(class_="_2mZMUi21HU4ydbF4R-70DQ")
        if (eventDateActual != None):
            print(eventDateActual.text)
        if (eventPrice != None):
            print(eventPrice.text[7:]+"+") # remove first 2 char from string in python. original string was "| from $.."

    print()






### shows/theater collection ###
url = 'https://gametime.co/los-angeles-tickets/metros/losangeles/theater'
response = requests.get(url, headers = {'User-agent': 'event bot 1.0'})
soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll(class_="_2h2W9WsYjZ0nMQMlLrr4cJ")

# a is the collection of events. b is each individual event
b = a[0].findAll(class_="col-md-6")

print (colors.red + "================ Collected from GameTime website - Shows/Theater ================" + colors.black)

for i in range(len(b)):
    print(colors.green + "Event " + str(i+1) + ":" + colors.black)
    eventName = b[i].find(class_="X47khF4xL4X-kF84-zkUQ container")
    if (eventName != None):
        eventNameActual = eventName.find(class_="_30B4YbPIjfZuZ03--GRTyB")
        eventLoc = eventName.find(class_="_3j0gTA8nYDiv1k6Lg0nJqV")
        if (eventNameActual != None):
            print(eventNameActual.text)
        if (eventLoc != None):
            print(eventLoc.text)
    eventDate = b[i].find(class_="LIsmOmbzL4AwaITrZy_0N")
    if (eventDate != None):
        eventDateActual = eventDate.find(class_="_2opqbRqujFoCFp0b6jZeMY")
        eventPrice = eventDate.find(class_="_2mZMUi21HU4ydbF4R-70DQ")
        if (eventDateActual != None):
            print(eventDateActual.text)
        if (eventPrice != None):
            print(eventPrice.text[7:]+"+") # remove first 2 char from string in python. original string was "| from $.."

    print()





