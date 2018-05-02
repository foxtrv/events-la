from colors import colors
from bs4 import BeautifulSoup
import requests

url = 'https://gametime.co/los-angeles-tickets/metros/losangeles'
response = requests.get(url, headers = {'User-agent': 'event bot 1.0'})
soup = BeautifulSoup(response.text, "html.parser")
# a = soup.select('div.list-view-item')
a = soup.select('div.list-view-item')

#for i in page.json(): # parses 2 {} inside the outer [] -
#    print(i.text)
    # for j in i['data']['children']:
    #     if j['data']['author'] == 'OnePunkArmy':
    #         print (colors.red + "================ Collected from weekly post on /r/LosAngeles ================" + colors.black)
    #         print("LINK = " + current_link)
    #         print (j['data']['body'])


# for i in page.json(): # parses 2 {} inside the outer [] -
#     for j in i['data']['children']:
#         if j['data']['author'] == 'OnePunkArmy':
#             print (colors.red + "================ Collected from weekly post on /r/LosAngeles ================" + colors.black)
#             print (j['data']['body'])
