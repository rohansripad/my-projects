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
#xml to dataframe python
import xml.etree.ElementTree as ET
import pandas as pd

xml_data = open('/path/user_agents.xml').read()

def xml2df(xml_data):
    root = ET.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
            all_records.append(record)
    return pd.DataFrame(all_records)
----------------------------------------------------------------------------------------------
#Get Summary of a Text
f = open("/Users/rattravanam/Desktop/Sample_text.txt","r")
text = f.read()

def get_paragraphs(text):
    para = []
    total_para = text.count('\n')
    for i in range(total_para):
        para.append(text[:text.find('\n')])
        text = text[text.find('\n')+1:]
    return para

def summarize(text):
    print(text)
    parags = get_paragraphs(text)
    summary = []
    for i in parags:
        sent_tokenize_list = sent_tokenize(i)
        summary.append("* "+sent_tokenize_list[0]+". "+sent_tokenize_list[len(sent_tokenize_list)-1])
    return summary

summarize(text)
