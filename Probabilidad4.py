from bs4 import BeautifulSoup

import urllib.request

import nltk

response = urllib.request.urlopen('https://es.wikipedia.org/wiki/Investigaci%C3%B3n')

html = response.read()

soup = BeautifulSoup(html, "html.parser")

text = soup.get_text(strip=True)

tokens = [t for t in text.split()]

freq = nltk.FreqDist(tokens)

####for key, val in freq.items():
##    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)
print(freq)
