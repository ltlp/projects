import requests
from bs4 import BeautifulSoup
import os
import pandas as pd 
from datetime import datetime


year = datetime.now().year
path = r'F:\LTLP\Documents\HW\2019 Fall\MIS 6110\data\SEC data'
url = 'https://www.sec.gov/Archives/edgar/daily-index/'
page = requests.get(url)
data = []

# loop through year and search for quarter
for year in range(2011,2017):
	url1 = url+str(year)+'/'
	new_page1 = requests.get(url1)
	parse_new_page1 = BeautifulSoup(new_page1.text, 'html.parser')
	quarter = parse_new_page1.find_all('a', href=lambda x: x and x.startswith('QTR'))
			`
	# append quarter to url and loop through year/quarter to find form
	for x in quarter:
		url2 = url1+x.get_text()+'/'
		new_page2 = requests.get(url2)
		parse_new_page2 = BeautifulSoup(new_page2.text, 'html.parser')
		form = parse_new_page2.find_all('a', href=lambda x: x and x.startswith('form'))

		# append form to url to get full url
		for x in form:
			full_url = url2+x.get_text()
			data.append(full_url)
			# print(full_url)

# download files
for full_url in data:
	form_file = requests.get(full_url)
	with open(path + '\\' + os.path.basename(full_url), 'wb') as f:
		f.write(form_file.content)