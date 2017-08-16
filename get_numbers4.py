import urllib
import html5lib
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# スクレイピングのコードはここを参考に作成
# http://qiita.com/hitoribucho/items/2fcfde45e1863bb3bad4

def get_numbers4():
    url = 'http://www.takarakujinet.co.jp/ajax/numbers4/pastResultPage.do'
    params = {
        'searchway': 'date',
        'year': '2017',
        'month': '8',
        'day': '16', 
        'kaigou': '',
        'howmany': '5000',  # 取得する件数
        }
    data = urllib.parse.urlencode(params).encode(encoding = 'ascii')
    with urllib.request.urlopen(url = url, data = data) as html:
         HTML = html.read().decode('utf-8')
    soup = BeautifulSoup(HTML, 'html5lib')
    tr_list = soup.find("table", {"class":"list"}).find_all("tr")
    all_data = []

    for i in range(2, len(tr_list)):
        if i%2 == 0:
            vol = tr_list[i].find_all('td')[0].text
            numbers = tr_list[i].find_all('td')[2].text
            all_data.append((vol, numbers))
        elif i%2 == 1:
            pass

    with open('numbers4_data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        for data in all_data:
            writer.writerow(data)

get_numbers4()