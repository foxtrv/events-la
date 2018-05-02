from colors import colors
from bs4 import BeautifulSoup
import requests

url = 'https://www.unionclubla.com/all-events/'
response = requests.get(url, headers = {'User-agent': 'event bot 1.0'})
soup = BeautifulSoup(response.text, "html.parser")
a = soup.select('div.list-view-item')

print (colors.red + "================ Collected from Union Nightclub website ================" + colors.black)
print("LINK = " + url)
print(colors.green + "(" + str(len(a)) + ") Events found for Union Nightclub" + colors.black + "\n")

for i in range(len(a)):
    #.lstrip() - remove leading whitespace. for some reason it kept parsing stuff with awkward spacing
    print(colors.green + "Event " + str(i+1) + ":" + colors.black)
    if (a[i].find('topline-info') != None):
        print(a[i].find('topline-info').text) # "<> Presents...
    print(a[i].find('h1').text) # Title of event
    if (a[i].find(class_="supports description") != None):
        print(a[i].find(class_="supports description").text) # Artists Performing
    print(a[i].find(class_="dates").text) # Date
    print(a[i].find(class_="times").text.lstrip()) # Time
    print(a[i].find(class_="venue location").text) # Location (Union has 3 rooms)
    if (a[i].find(class_="age-restriction") != None):
        print(a[i].find(class_="age-restriction").text.lstrip()) # Age Restriction
    if (a[i].find(class_="price-range") != None):
        print(a[i].find(class_="price-range").text.lstrip()) # Price
    print(a[i].find("img").get('src')) # Image
    print() # print extra line for readability
