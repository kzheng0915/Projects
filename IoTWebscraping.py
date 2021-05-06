import urllib.request
from bs4 import BeautifulSoup
import re

headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

url = 'https://www.amazon.com/s?k=wemo+plug&ref=nb_sb_noss'
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
respData = resp.read()

soup = BeautifulSoup(respData, 'html.parser')
soup.prettify()

class Product:
    def __init__(self, productDiv):
        self.productDiv = productDiv
        self.name = self.findName()
        self.price = self.findPrice()
        self.img = self.findImg()
        self.rating = self.findRating()
        self.numOfRating = self.findNumOfRating()

    def __repr__(self):
        return '\n'.join((attr + ': ' + str(getattr(self, attr))) for attr in vars(self) if attr != 'productDiv')

    def __bool__(self):
        return all(getattr(self, attr) for attr in vars(self))

    #this method converts price, rating, or the number of ratings from string to int or float
    def convertToNum(self, string):
        string = string.strip()
        if ',' in string:
            index = string.index(',')
            string = string[:index] + string[index+1:]
        if string[-1] == '.':
            string = string[:-1]
        if '.' in string: #the string is a rating
            index = string.index(' ')
            string = string[:index]
            return float(string)
        return int(string)
        
    def findName(self):
        for name in self.productDiv.select("span.a-color-base.a-text-normal"):
            return name.get_text() if name else None

    def findImg(self):
        for image in self.productDiv.find_all('img'):
            source = image['src']
            if re.search('m.media-amazon.com.*jpg$', source):
                return source
        return None

    def findPrice(self):
        price = self.productDiv.find('span',{'class': 'a-price-whole'})
        return self.convertToNum(price.get_text()) if price else None

    def findRating(self):
        row = self.productDiv.find('div', {'class', 'a-row a-size-small'})
        if not row:
            return
        rating = row.find('span', {'class', 'a-icon-alt'})
        return self.convertToNum(rating.get_text()) if rating else None

    def findNumOfRating(self):
        row = self.productDiv.find('div', {'class', 'a-row a-size-small'})
        if not row:
            return
        numOfRating = row.find('span', {'class', 'a-size-base'})
        return self.convertToNum(numOfRating.get_text()) if numOfRating else None

def main():
    products = set({})
    for productDiv in soup.find_all('div',{'class': 'a-section a-spacing-medium'}): #common parent tag for every product
        product = Product(productDiv)
        if product:
            products.add(product)
            print(product)
            print()

if __name__ == '__main__':
    main()
