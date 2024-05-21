#--Request Module--
import requests

response = requests.get("https://www.google.com") #Get Request
print(response.text)

url = "https://jsonplaceholder.typicode.com/posts" #Post Request

data = {
    "title": 'harry',
    "body": 'bhai'
}
headers = {
    'content-type': 'application/json;charset=UTF-8',
}
response = requests.post(url, headers=headers, json=data)

#bs4 
import requests
from bs4 import BeautifulSoup
url = "https://www.google.com"
r = requests.get(url) 
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"): #h2 wala sabai lai print garxa in the code
    print(heading.text)

#Exercise 10, News App in Python

import requests
import json

query = input("What type of news are you interested in? :")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-02-08&sortBy=publishedAt&apiKey=738057562f1940088f22359bc176e9dc"
r = requests.get(url)
# print(r.text)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------")

#Exercise 11, Drink Water Reminder

import time
from plyer import notification

time_hour = float(input("Set the hours after you want to drink water : "))
while(True):
    time.sleep(3600 * time_hour)
    notification.notify(title = "Water",
                        message = "You should drink water",
                        timeout = 2)
                   
                   