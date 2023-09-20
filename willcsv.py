from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://tech4gamers.com/'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


# Extracting the number of titles
newstitle = soup.select('h3 a')
print(newstitle[0])
print(" ")
print("how many titles are available?",len(soup.select('h3.title')))

# Get links
text = soup.select('h3 a')
print(text)

# Target the attribute inside the tag, to reveal link cleanly
links=[]
for a in soup.select('h3 a'):
  links.append(a.attrs.get('href'))

print(links[0])

# Storing the data with the help of a loop
article_title=[]
links=[]

for t in soup.select('h3 a'):
  article_title.append(t.get_text())
  links.append(t.attrs.get('href'))

print(article_title)
print(links)


df = pd.DataFrame(
    {'article title': article_title,
     'link': links}
    )

print (df.head())

df.to_csv('neeeeeeeerd.csv', index=False)











