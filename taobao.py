import requests
res = requests.get('https://s.taobao.com/search?q=%E5%A4%9A%E6%A8%A3%E5%B1%8B%E8%91%AB%E8%98%86&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20171121&ie=utf8')
'''
# Windows Traditional version will set default encoding while dumping results to terminal or file
# thus we need to overwrite the encoding setting
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text)
fh = open('res.txt', 'wt', encoding='utf8')
print(res.text, file=fh)
fh.close()
'''


import re

L = res.text.split('\n')
raw = ""
for itm in L :
    m = re.search('g_page_config = (.*)', itm)
    if m : raw = m.group(1)[:-1]
#print(raw)
import json
json_dat = json.loads(raw)



itm_list = json_dat['mods']['itemlist']['data']['auctions']
import sys
for i in itm_list :
    for k in i :
        m = re.search('(raw_title|view_price|view_fee)', k)
        if m :
            print ('{} => {}'.format(k, i[k]))


import pandas
df = pandas.DataFrame(itm_list)
df.to_csv('tao.csv', sep='\t', encoding='utf8', index=False)

