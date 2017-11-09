#dataframe to Excel
import pandas as pd
writer = pd.ExcelWriter('pandas_simple.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
-----------------------------------------
#dataframe to CSV
df.to_csv(file_name)
----------------------------------------------------------------------------------------------
#Calculate time to run a code
%timeit function
----------------------------------------------------------------------------------------------
#json to dataframe python
#https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe
import json
from pandas.io.json import json_normalize
parsed_json = json.loads(json_string)
json_normalize(parsed_json['results'])
----------------------------------------------------------------------------------------------
#fetch data from url
import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read()
----------------------------------------------------------------------------------------------
