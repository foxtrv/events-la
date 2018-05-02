from colors import colors
from bs4 import BeautifulSoup
import requests
import sys

# First have to go to the subreddit and click on the new weekly post
response = requests.get("https://www.reddit.com/r/LosAngeles/", headers = {'User-agent': 'event bot 1.0'})
soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll(class_="thing")

for i in range(len(a)):
    if (a[i].find(class_="title") != None):
        title = a[i].find(class_="title").text
        if (title != None and title.find("Totally Awesome Things To Do In Los Angeles") > 0):
            link_suffix = a[i].find("a").get('href')

# else link is down, throw error
if (link_suffix == None):
    sys.exit('link url not available on site')

url = 'https://www.reddit.com' + link_suffix + '.json'

# Now that you have the link, parse the json.
page = requests.get(url, headers = {'User-agent': 'event bot 1.0'})
for i in page.json(): # parses 2 {} inside the outer [] -
    for j in i['data']['children']:
        if j['data']['author'] == 'OnePunkArmy':
            print (colors.red + "================ Collected from weekly post on /r/LosAngeles ================" + colors.black)
            print("Link = " + url)
            print (j['data']['body'])
