# -*- coding: utf-8 -*-

"""retrieve data for product from page by css selectors from user input"""

import requests
from bs4 import BeautifulSoup

def get_html (url):
    """ feed url and return html"""
    r = requests.get(url)
    return r.text

def get_data(html, title, price, sku, description, image):
	"""feed html and css selectors and return data for each of them"""
	soup = BeautifulSoup(html, 'lxml')
	title = soup.select_one(str(title)).text
	price = soup.select_one(str(price)).text
	sku = soup.select_one(str(sku)).text
	description = soup.select_one(str(description)).text
	image = soup.select_one(str(image))['src']

	i = {
      'title' : title, 
      'price' : price, 
      'sku' : sku, 
      'description' : description, 
      'image' : image
      }

	return i

if __name__ == "__main__":

	# incoming data from user
	title = 'h1.prod-ProductTitle'
	price = 'span.price span.visuallyhidden'
	sku = 'div.wm-item-number'
	description = 'div.about-desc'
	image = 'img.hover-zoom-hero-image'

	# test urls for checking the outcome from the parser
	test_url = 'https://www.walmart.com/ip/BFGoodrich-Rugged-Terrain-T-A-Tire-P235-75R15-XL-108T/680065983'

	html = get_html(test_url)
	data = get_data(html, title, price, sku, description, image)
#	for key, value in data.items():
#		print (key, value)