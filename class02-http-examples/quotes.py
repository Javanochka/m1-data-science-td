import requests
from bs4 import BeautifulSoup

def get_quotes(url):
    page = requests.get(url=url,headers={'User-Agent': 'Mozilla/5.0'}) #You retrieve all the content
    soup = BeautifulSoup(page.content, 'html.parser') #You parse it in a readable human way
    quotes = soup.find_all(class_="text") #Now you find wathever class is useful for you 
    return list(map(lambda x : x.get_text(), quotes)) #You extract the text and print it calling the function

def get_next(url):
    page = requests.get(url=url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    next_el = soup.find(class_="next") #Goes to all the elements that appear next to the one you are 
    return next_el

url= 'http://quotes.toscrape.com'
l = get_quotes(url)
print(l)
next_el = get_next(url)

while next_el is not None:
    link = next_el.find('a')['href']
    next_url = url + link
    l.extend(get_quotes(next_url))
    next_el = get_next(next_url)
    
with open('quotes.txt','w') as f:
    for i in range(len(l)):
        print(f"{i}: {l[i]}", file=f)
