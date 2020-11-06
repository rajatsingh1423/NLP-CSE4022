import requests 
from bs4 import BeautifulSoup 


def getText(URL):       
    r = requests.get(URL)    
    soup = BeautifulSoup(r.content, 'html5lib')    
    title = soup.find('h1')
    print(title.text)
    title = title.text
    
    filename = "NatGeo/"+title+".txt"
    f = open(filename, 'w')
    f.write(title)
    f.write('\n')
        
    
    table = soup.find('div', attrs = {'class':'storyWrap'})  
    for row in table.findAll('p'): 
        #print(row.text)
        f.write(row.text)
        f.write('\n')
    f.close()



URL = "http://www.natgeotraveller.in/author/lakshmi-sankaran/"
r = requests.get(URL)    
soup = BeautifulSoup(r.content, 'html5lib')    
URLs = []
table = soup.find('div', attrs = {'class': 'storyWrap'})

for url in table.findAll('div', attrs = {'class': 'cDescription'}):
    #print(url.h1.a['href'])
    URLs.append(str(url.h1.a['href']))
    
for url in URLs:
    getText(url)
    