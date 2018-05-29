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
    eventName = b[i].find(class_="_2YoFuNQ31DP1tGi7SJSx9L")
    if (eventName != None):
        print(eventName.text)
    eventDate = b[i].find(class_="_2HXqS58qcLrerum_SzOdyb")
    if (eventDate != None):
        eventDateActual = eventDate.find(class_="VCS8tleOdm6_4nFDSF_AC")
        if (eventDateActual != None):
            print(eventDateActual.text)
        eventPrice = eventDate.find(class_="vhz-YnjOiZcynqmwAjbaE")
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
    eventName = b[i].find(class_="_2YoFuNQ31DP1tGi7SJSx9L")
    if (eventName != None):
        eventNameActual = eventName.find(class_="_3J1yVeOjo76PEdnHsjnCi6")
        eventLoc = eventName.find(class_="_1QH5kZPjz42BSlnEVdkzT1")
        if (eventNameActual != None):
            print(eventNameActual.text)
        if (eventLoc != None):
            print(eventLoc.text)
    eventDate = b[i].find(class_="_2HXqS58qcLrerum_SzOdyb")
    if (eventDate != None):
        eventDateActual = eventDate.find(class_="VCS8tleOdm6_4nFDSF_AC")
        eventPrice = eventDate.find(class_="vhz-YnjOiZcynqmwAjbaE")
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
    eventName = b[i].find(class_="_2YoFuNQ31DP1tGi7SJSx9L")
    if (eventName != None):
        eventNameActual = eventName.find(class_="_3J1yVeOjo76PEdnHsjnCi6")
        eventLoc = eventName.find(class_="_1QH5kZPjz42BSlnEVdkzT1")
        if (eventNameActual != None):
            print(eventNameActual.text)
        if (eventLoc != None):
            print(eventLoc.text)
    eventDate = b[i].find(class_="_2HXqS58qcLrerum_SzOdyb")
    if (eventDate != None):
        eventDateActual = eventDate.find(class_="VCS8tleOdm6_4nFDSF_AC")
        eventPrice = eventDate.find(class_="vhz-YnjOiZcynqmwAjbaE")
        if (eventDateActual != None):
            print(eventDateActual.text)
        if (eventPrice != None):
            print(eventPrice.text[7:]+"+") # remove first 2 char from string in python. original string was "| from $.."

    print()





