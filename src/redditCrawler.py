from colors import colors
from bs4 import BeautifulSoup
import requests

# First have to go to the subreddit and click on the new weekly post
response = requests.get("https://www.reddit.com/r/LosAngeles/", headers = {'User-agent': 'event bot 1.0'})
soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll(class_="thing")

for i in range(len(a)):
    if (a[i].find(class_="title") != None):
        title = a[i].find(class_="title").text
        if (title != None and title.find("Totally Awesome Things To Do In Los Angeles") > 0):
            link_suffix = a[i].find("a").get('href')

# sometimes a returns NoneType, I am not sure why. My guess is that python is not fully waiting for the get to complete and uses the first thing it sees.
url = 'https://www.reddit.com' + link_suffix + '.json'

# Now that you have the link, parse the json.
page = requests.get(url, headers = {'User-agent': 'event bot 1.0'})
for i in page.json(): # parses 2 {} inside the outer [] -
    for j in i['data']['children']:
        if j['data']['author'] == 'OnePunkArmy':
            print (colors.red + "================ Collected from weekly post on /r/LosAngeles ================" + colors.black)
            print("Link = " + url)
            print (j['data']['body'])
