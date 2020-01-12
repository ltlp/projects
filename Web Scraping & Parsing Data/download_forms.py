import requests
import pandas as pd 
import os


form10k_csv = pd.read_csv('F:\\LTLP\\Documents\\HW\\2019 Fall\\MIS 6110\\data\\forms_10k.csv')

path = 'F:\\LTLP\\Documents\\HW\\2019 Fall\\MIS 6110\\data\\10-K forms\\'
securl = 'https://www.sec.gov/Archives/'

# find all forms in 2015-16
form10k_1516 = form10k_csv.loc[(form10k_csv['Date Filed'] >= 20150000) & (form10k_csv['Date Filed'] <= 20170000)]


# pull all file names from 2015-16 and create list
series_file_name = form10k_1516['File Name']
url = series_file_name.tolist()

# download 10-K forms
for file_name in url:
	form10k = requests.get(securl+file_name)
	with open(path + os.path.basename(file_name), 'wb') as f:
		f.write(form10k.content)