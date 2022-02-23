import pandas
import json
from os import listdir
import os

path = os.path.abspath(os.getcwd())
lst = [f for f in listdir(path)]

def conversion():
	for i in lst:
		if i.endswith('xlsx'):
			excel_data_df = pandas.read_excel('{}'.format(i))
			thisisjson = excel_data_df.to_json(orient='records')
			print('Excel Sheet to Json:\n', thisisjson)
			thisisjson_dict = json.loads(thisisjson)
			with open('{}.json'.format(i.rsplit(".",1[0]),'w') as json_file:
				json.dump(thisisjson_dict, json_file)
		else:
			continue
conversion()