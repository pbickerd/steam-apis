#!/bin/python

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "http://store.steampowered.com"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Get top sellers
topsellers = soup.find(id="tab_topsellers_content")

gameslist = topsellers.find_all(class_="tab_item_name")
pricelist = topsellers.find_all(class_="discount_final_price")

gameslistTidy = [gl.get_text() for gl in gameslist]
pricelistTidy = [pl.get_text() for pl in pricelist]

topSellerTable = PrettyTable(["Game", "Price"])

#Put them in a table
for i in range(len(gameslistTidy)):
    topSellerTable.add_row([gameslistTidy[i], pricelistTidy[i]])

#Get Specials
specials = soup.find(id="tab_specials_content")

gameslist = specials.find_all(class_="tab_item_name")
pricelist = specials.find_all(class_="discount_final_price")

gameslistTidy = [gl.get_text() for gl in gameslist]
pricelistTidy = [pl.get_text() for pl in pricelist]

specialTable = PrettyTable(["Game", "Price"])

#Put them in a table
for i in range(len(gameslistTidy)):
    specialTable.add_row([gameslistTidy[i], pricelistTidy[i]])


print "Top Sellers"
print topSellerTable
print "\n\n"
print "Specials"
print specialTable

