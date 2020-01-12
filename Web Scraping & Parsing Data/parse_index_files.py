
import pandas as pd 
import os


path = 'F:\\LTLP\\Documents\\HW\\2019 Fall\\MIS 6110\\data\\SEC data\\'
col_widths = [12,62,12,12,52]
columns = ['Form Type', 'Company Name', 'CIK', 'Date Filed', 'File Name']
forms_10k = []

# parse through all index files to find all 10-K forms and add to list
for file in os.listdir(path):
		parse_file = pd.read_fwf(file, skiprows=11, widths=col_widths, names=columns, compression='infer')
		find_form_type = parse_file.loc[parse_file['Form Type']=='10-K']
		forms_10k.append(find_form_type)

# append dataframes into one
forms_10k_df = pd.concat(forms_10k)

# save as .csv file
forms_10k_df.to_csv('F:\\LTLP\\Documents\\HW\\2019 Fall\\MIS 6110\\data\\forms_10k.csv', index=None)
