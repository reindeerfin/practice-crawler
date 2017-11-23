import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
res = requests.get('https://www.xinshipu.com/zuofa/62273', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

reup = soup.select('.re-up')[0]
print(reup.select('.font18.no-overflow')[0].text)
sc = reup.select('.font16.ml10.col')

for i in sc:
    print(i.text)

misc = reup.select('.cg2.mt12 span')
for i in range(len(misc)):
    print(misc[i].text, end=' ')
    if i % 2 == 1: print()

    # print(reup.select('.cg2.mt12 span:nth-of-type(2)')[0].text)